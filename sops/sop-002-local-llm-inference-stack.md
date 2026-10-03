# SOP-002: Local LLM Inference Stack: Operation & Troubleshooting

Sep 29, 2026 · @Lloyd

## 1. Document Control

| Field | Value |
| --- | --- |
| Document ID | SOP-002 |
| Version | 0.2 (Draft) |
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

Ollama serves models on the host GPU; Open WebUI runs in Docker and reaches Ollama through `host.docker.internal:11434`. The container publishes its port on the host loopback address only, and Tailscale Serve publishes that port to the tailnet over HTTPS. Devices on the local network that are not on the tailnet cannot reach the UI.

| Component | Detail |
| --- | --- |
| Host | Windows 11 Pro, Ryzen 7 7800X3D, RTX 5080 (16 GB) |
| Inference engine | Ollama, native on host, port 11434 |
| Interface | Open WebUI container `open-webui`, image pinned to a release tag (record it here), host `127.0.0.1:3001` to container 8080, volume `open-webui` |
| Primary model | gpt-oss:20b (custom SOP Drafter and Network+ Tutor models built on it) |
| Remote access | Tailscale Serve (`tailscale serve --bg 3001`); UI at `https://<host>.<tailnet>.ts.net` |
| Auto-start | Docker Desktop at login; container `--restart always`; host power plan never sleeps |

## 4. Procedure A: Startup and Health Check

Run top to bottom; stop at the first failed check and go to Section 8.

1. Confirm no consumer VPN (NordVPN or similar) is active on the host, or that Ollama and Docker are excluded from it.
2. Confirm the GPU and driver respond: `nvidia-smi` lists the RTX 5080 with no errors.
3. Confirm Ollama is running: `ollama list` returns installed models.
4. Test the engine directly, bypassing the UI: `ollama run gpt-oss:20b "Reply with OK"`.
5. Confirm the container is up: `docker ps` shows `open-webui` with `127.0.0.1:3001->8080/tcp`. If it shows `0.0.0.0:3001`, the UI is exposed to the whole local network; recreate it with Procedure C, step 7.
6. Open `http://localhost:3001` on the host and send a short prompt.
7. Confirm Tailscale Serve is publishing the UI: `tailscale serve status` lists port 3001.
8. From a remote client on Tailscale, open `https://<host>.<tailnet>.ts.net` and send a short prompt.

## 5. Procedure B: Model Parameter Tuning

Reasoning models spend output tokens on hidden reasoning before answering, so default limits truncate long responses. Set both values per custom model in Open WebUI under Advanced Params.

| Parameter | Controls | Default | Set to (long-form output) |
| --- | --- | --- | --- |
| Max Tokens (`num_predict`) | Output cap, reasoning included | Low or unset | 8192 |
| Context Length (`num_ctx`) | Prompt + reasoning + answer | 4096 | 16384 |

Raise `num_ctx` in steps and watch VRAM in `nvidia-smi`; if the model spills out of the 16 GB card, speed drops sharply. Record every change in Section 10.

## 6. Procedure C: Backup and Open WebUI Upgrade

Back up before every upgrade; the container is disposable, the `open-webui` volume is not. Upgrades move from one pinned release tag to the next. Do not run the `:main` tag, which changes without notice and leaves no known version to roll back to.

1. Record the current run configuration and image tag: `docker inspect open-webui --format "{{json .HostConfig}}"` and `docker inspect open-webui --format "{{.Config.Image}}"`.
2. Stop the container so the database is not written to during the copy: `docker stop open-webui`.
3. Copy the database out of the stopped container: `docker cp open-webui:/app/backend/data/webui.db C:\Users\<user>\webui-backup-<date>.db`. Copy the single file, not the whole data folder (see Section 8).
4. Confirm the backup file exists and is not zero bytes.
5. Choose the target release from the Open WebUI releases page, read its release notes for breaking changes, and pull it: `docker pull ghcr.io/open-webui/open-webui:<release tag>`.
6. Remove the old container: `docker rm open-webui`. The volume is kept.
7. Recreate it with the port bound to loopback only:

```
docker run -d -p 127.0.0.1:3001:8080 -v open-webui:/app/backend/data --add-host=host.docker.internal:host-gateway --name open-webui --restart always ghcr.io/open-webui/open-webui:<release tag>
```

8. Watch `docker logs -f open-webui` until database migrations complete without errors, then run Section 7.
9. Record the new release tag in Section 3 and in Section 10.

**Rollback.** If migrations fail or the verification checks do not pass, stop and remove the new container, restore the backup into the volume, and recreate the container on the previous tag recorded in step 1:

```
docker stop open-webui
docker rm open-webui
docker create -v open-webui:/app/backend/data --name owui-restore alpine
docker cp C:\Users\<user>\webui-backup-<date>.db owui-restore:/app/backend/data/webui.db
docker rm owui-restore
```

Then rerun step 7 with the previous release tag.

## 7. Verification

The stack passes only when every check holds.

- [ ] Existing chats, custom models, and knowledge bases are present after any upgrade
- [ ] A 10-question quiz prompt to the Network+ Tutor returns all 10 questions, fully formatted
- [ ] The same prompt works from a remote client over cellular data (Tailscale path, not LAN)
- [ ] Port 3001 is not reachable from another device on the local network that is not on the tailnet
- [ ] Port 3001 is not reachable from the public internet (no router port forward exists)
- [ ] The running image tag matches the tag recorded in Section 3
- [ ] A current `webui.db` backup exists and is newer than the last upgrade

## 8. Known Failure Modes

Observed during operation of this stack. The first row matters most: the error message pointed at the wrong component.

| Symptom | Cause | Resolution |
| --- | --- | --- |
| UI shows brief "thinking" then no answer, or long jumbled unformatted text; logs report a CUDA initialization error | NordVPN network filter driver interfering with Ollama runtime startup. GPU and driver were healthy (`nvidia-smi` clean) | Disconnect the VPN and retest with `ollama run`. For permanent coexistence, exclude `ollama.exe` and Docker via split tunneling and retest |
| Long output stops early (quiz ended at question 9 of 10) | Output cap reached; reasoning tokens consumed the budget | Raise `num_predict` to 8192 and `num_ctx` to 16384 (Section 5) |
| `docker cp` of the whole data folder fails with a symlink error | Model cache inside the container uses symlinks that Windows cannot create without admin rights or Developer Mode | Copy only `webui.db`; the cache re-downloads if needed |
| PowerShell errors on a `docker inspect --format` template containing `\n` | PowerShell escapes differ from bash | Use `{{json ...}}` output instead of a hand-built template |
| UI unreachable remotely but works on the host | Tailscale Serve not running, or host asleep | Run `tailscale serve status`; if port 3001 is missing, run `tailscale serve --bg 3001`. Set power plan to never sleep. Do not rebind the container to all interfaces |
| UI reachable from other devices on the local network | Container published on `0.0.0.0:3001` instead of loopback | Recreate the container with `-p 127.0.0.1:3001:8080` (Procedure C, step 7) |

## 9. Control Mapping

Verify each reference against the published framework text before changing status to Reviewed.

| Procedure step | NIST SP 800-53 Rev 5 | ISO/IEC 27001:2022 Annex A |
| --- | --- | --- |
| Documented system configuration with pinned image tag (Section 3) | CM-2 Baseline Configuration | 8.9 Configuration management |
| Backup before upgrade (Procedure C) | CP-9 System Backup | 8.13 Information backup |
| Controlled upgrade with rollback path (Procedure C) | CM-3 Configuration Change Control | 8.32 Change management |
| Keeping the container image current | SI-2 Flaw Remediation | 8.8 Management of technical vulnerabilities |
| Loopback-only port, published to the tailnet only, no public port | SC-7 Boundary Protection; AC-17 Remote Access | 8.20 Networks security |

## 10. Revision History

| Version | Date | Change |
| --- | --- | --- |
| 0.1 | 2026-09-29 | Initial draft from observed operation: NordVPN conflict, output truncation, Open WebUI upgrade |
| 0.2 | 2026-10-03 | Bound the UI to loopback and published it with Tailscale Serve, so it is no longer exposed to the local network. Pinned the image to a release tag. Stop the container before backing up the database. Added a rollback procedure |
