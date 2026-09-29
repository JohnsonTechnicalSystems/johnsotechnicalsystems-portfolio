# SOP-002: Local LLM Inference Stack: Operation & Troubleshooting

Sep 29, 2026 · @Lloyd

## 1. Document Control

| Field | Value |
| --- | --- |
| Document ID | SOP-002 |
| Version | 0.1 (Draft) |
| Owner | Lloyd Johnson, johnsontechnicalsystems LLC |
| Milestone | Network Operations & Troubleshooting |
| Review cycle | Every 6 months, or after any stack upgrade or new failure mode |
| Classification | Internal / Portfolio sample |
| Related | SOP-001 Secure Remote Access to Windows Workstations |

## 2. Purpose and Scope

This SOP keeps local AI inference running, recoverable, and private. It covers startup checks, parameter tuning, backup before upgrades, and diagnosis of known failures.

**In scope:** the Windows desktop running Ollama and the Open WebUI Docker container, plus access to it over Tailscale.

**Out of scope:** remote desktop access (see SOP-001), model training, and any processing of client data. No client data enters this stack unless a contract permits it.

## 3. System Description

Ollama serves models on the host GPU; Open WebUI runs in Docker and reaches Ollama through `host.docker.internal:11434`. Remote clients reach the UI over Tailscale only.

| Component | Detail |
| --- | --- |
| Host | Windows 11 Pro, Ryzen 7 7800X3D, RTX 5080 (16 GB) |
| Inference engine | Ollama, native on host, port 11434 |
| Interface | Open WebUI container `open-webui`, host port 3001 to container 8080, volume `open-webui` |
| Primary model | gpt-oss:20b (custom SOP Drafter and Network+ Tutor models built on it) |
| Remote access | Tailscale overlay; UI at `http://<host Tailscale IP>:3001` |
| Auto-start | Docker Desktop at login; container `--restart always`; host power plan never sleeps |

## 4. Procedure A: Startup and Health Check

Run top to bottom; stop at the first failed check and go to Section 8.

1. Confirm no consumer VPN (NordVPN or similar) is active on the host, or that Ollama and Docker are excluded from it.
2. Confirm the GPU and driver respond: `nvidia-smi` lists the RTX 5080 with no errors.
3. Confirm Ollama is running: `ollama list` returns installed models.
4. Test the engine directly, bypassing the UI: `ollama run gpt-oss:20b "Reply with OK"`.
5. Confirm the container is up: `docker ps` shows `open-webui` with `0.0.0.0:3001->8080/tcp`.
6. Open `http://localhost:3001` on the host and send a short prompt.
7. From a remote client on Tailscale, open the UI at the host's Tailscale address, port 3001.

## 5. Procedure B: Model Parameter Tuning

Reasoning models spend output tokens on hidden reasoning before answering, so default limits truncate long responses. Set both values per custom model in Open WebUI under Advanced Params.

| Parameter | Controls | Default | Set to (long-form output) |
| --- | --- | --- | --- |
| Max Tokens (`num_predict`) | Output cap, reasoning included | Low or unset | 8192 |
| Context Length (`num_ctx`) | Prompt + reasoning + answer | 4096 | 16384 |

Raise `num_ctx` in steps and watch VRAM in `nvidia-smi`; if the model spills out of the 16 GB card, speed drops sharply. Record every change in Section 10.

## 6. Procedure C: Backup and Open WebUI Upgrade

Back up before every upgrade; the container is disposable, the `open-webui` volume is not.

1. Copy the database out of the container: `docker cp open-webui:/app/backend/data/webui.db C:\Users\<user>\webui-backup.db`. Copy the single file, not the whole data folder (see Section 8).
2. Confirm the backup file exists and is not zero bytes.
3. Record the current run configuration: `docker inspect open-webui --format "{{json .HostConfig}}"`.
4. Pull the new image: `docker pull ghcr.io/open-webui/open-webui:main`.
5. Stop and remove the old container: `docker stop open-webui` then `docker rm open-webui`. The volume is kept.
6. Recreate it:

```
docker run -d -p 3001:8080 -v open-webui:/app/backend/data --add-host=host.docker.internal:host-gateway --name open-webui --restart always ghcr.io/open-webui/open-webui:main
```

7. Watch `docker logs -f open-webui` until database migrations complete without errors, then run Section 7.

## 7. Verification

The stack passes only when every check holds.

- [ ] Existing chats, custom models, and knowledge bases are present after any upgrade
- [ ] A 10-question quiz prompt to the Network+ Tutor returns all 10 questions, fully formatted
- [ ] The same prompt works from a remote client over cellular data (Tailscale path, not LAN)
- [ ] Port 3001 is not reachable from the public internet (no router port forward exists)
- [ ] A current `webui.db` backup exists and is newer than the last upgrade

## 8. Known Failure Modes

Observed during operation of this stack. The first row matters most: the error message pointed at the wrong component.

| Symptom | Cause | Resolution |
| --- | --- | --- |
| UI shows brief "thinking" then no answer, or long jumbled unformatted text; logs report a CUDA initialization error | NordVPN network filter driver interfering with Ollama runtime startup. GPU and driver were healthy (`nvidia-smi` clean) | Disconnect the VPN and retest with `ollama run`. For permanent coexistence, exclude `ollama.exe` and Docker via split tunneling and retest |
| Long output stops early (quiz ended at question 9 of 10) | Output cap reached; reasoning tokens consumed the budget | Raise `num_predict` to 8192 and `num_ctx` to 16384 (Section 5) |
| `docker cp` of the whole data folder fails with a symlink error | Model cache inside the container uses symlinks that Windows cannot create without admin rights or Developer Mode | Copy only `webui.db`; the cache re-downloads if needed |
| PowerShell errors on a `docker inspect --format` template containing `\n` | PowerShell escapes differ from bash | Use `{{json ...}}` output instead of a hand-built template |
| UI unreachable remotely but works on the host | Port bound to `127.0.0.1:3001` instead of all interfaces, or host asleep | Rebind as `-p 3001:8080`; set power plan to never sleep |

## 9. Control Mapping

Verify each reference against the published framework text before changing status to Reviewed.

| Procedure step | NIST SP 800-53 Rev 5 | ISO/IEC 27001:2022 Annex A |
| --- | --- | --- |
| Documented system configuration (Section 3) | CM-2 Baseline Configuration | 8.9 Configuration management |
| Backup before upgrade (Procedure C) | CP-9 System Backup | 8.13 Information backup |
| Controlled upgrade with rollback path (Procedure C) | CM-3 Configuration Change Control | 8.32 Change management |
| Keeping the container image current | SI-2 Flaw Remediation | 8.8 Management of technical vulnerabilities |
| Tailscale-only access, no public port | SC-7 Boundary Protection; AC-17 Remote Access | 8.20 Networks security |

## 10. Revision History

| Version | Date | Change |
| --- | --- | --- |
| 0.1 | 2026-09-29 | Initial draft from observed operation: NordVPN conflict, output truncation, Open WebUI upgrade |
