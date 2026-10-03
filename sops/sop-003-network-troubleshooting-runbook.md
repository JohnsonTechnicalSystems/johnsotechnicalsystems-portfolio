# SOP-003: Network Troubleshooting Runbook

Sep 29, 2026 · @Lloyd

## 1. Document Control

| Field | Value |
| --- | --- |
| Document ID | SOP-003 |
| Version | 0.2 (Draft) |
| Owner | Lloyd Johnson, johnsontechnicalsystems LLC |
| Milestone | Network Operations & Troubleshooting |
| Review cycle | Every 6 months, and after every new incident worth a case entry |
| Classification | Internal / Portfolio sample |
| Related | SOP-001 Secure Remote Access; SOP-002 Local LLM Inference Stack |
| Exam alignment | CompTIA Network+ N10-009, Objective 5.1 |

## 2. Purpose and Scope

This runbook applies one repeatable method to every network fault, so diagnosis follows evidence instead of guesses. It covers the home office network, the Windows workstation, remote access over Tailscale, and the ISP uplink.

Each case in Sections 5 to 7 is a real incident, recorded in the method's own seven steps. New incidents are added the same way.

## 3. The Seven-Step Method

Follow the steps in order. If a theory fails at step 3, return to step 2; if no theory holds, escalate.

1. **Identify the problem.** Gather information, question users, identify symptoms, determine what changed, duplicate the problem, and approach multiple problems one at a time.
2. **Establish a theory of probable cause.** Question the obvious; work top-to-bottom or bottom-to-top through the OSI model, or divide and conquer.
3. **Test the theory.** If confirmed, move on; if not, form a new theory or escalate.
4. **Establish a plan of action** and identify potential effects of the fix.
5. **Implement the solution** or escalate as necessary.
6. **Verify full system functionality** and, if applicable, implement preventive measures.
7. **Document findings, actions, outcomes, and lessons learned.**

Source: CompTIA Network+ N10-009 exam objectives, 5.1. Verify wording against the current objectives PDF before marking Reviewed.

## 4. Diagnostic Commands by Layer

Work bottom-up by default: each layer that passes rules out everything beneath it.

| OSI layer | Question | Windows command or check |
| --- | --- | --- |
| 1 Physical | Is there link and signal? | Router PON and LAN lights; adapter status in `ipconfig /all` |
| 2 Data link | Right MAC, right network? | `arp -a`; router DHCP client list |
| 3 Network | Do I have an address and a route? | `ipconfig`; `ping <gateway>`; `ping 8.8.8.8`; `tracert 8.8.8.8` |
| 3 Network (overlay) | Is the Tailscale path up? | `tailscale status`; `tailscale ping <host>` |
| 4 Transport | Is the port listening and reachable? | `netstat -ano \| findstr :3389`; `Test-NetConnection <host> -Port 3389` |
| 7 Application | Does name resolution and the service work? | `nslookup <name>`; service status; application logs |
| Host policy | Is the firewall profile correct? | `Get-NetConnectionProfile` (Private vs Public) |

## 5. Case 1: ISP WAN Outage After Power Interruption

Outcome: fault was upstream at the ISP; no local configuration was changed.

| Step | What happened |
| --- | --- |
| 1 Identify | Every device joined Wi-Fi but no traffic passed. Change: a power interruption. Router showed PON green, INTERNET red, WAN status unconnected |
| 2 Theory | Layer 1 fibre link is up (PON green), so the fault sits above it: WAN session not reissued by the ISP |
| 3 Test | Local LAN worked between devices; WAN IP field on the router was empty. Theory confirmed |
| 4 Plan | Power cycle router for a full five minutes; if unresolved, escalate. Effect: brief loss of LAN too |
| 5 Implement | Power cycled; then escalated to the ISP, stating "PON online, no WAN address" to skip tier-1 scripts |
| 6 Verify | WAN IP populated, INTERNET light green, Tailscale reconnected, remote RDP test passed |
| 7 Document | Lesson: do not change local settings during an upstream outage; it only adds variables |

## 6. Case 2: RDP Session Hangs at "Securing connection"

Outcome: two stacked causes, found one at a time. Fixing the first did not clear the symptom, which is why step 3 loops back to step 2.

| Step | What happened |
| --- | --- |
| 1 Identify | RDP client stalled indefinitely at "Securing connection" with no error. Credentials were not yet rejected, so the fault was below authentication |
| 2 Theory A | Host firewall dropping traffic mid-negotiation because the network profile is Public |
| 3 Test A | `Get-NetConnectionProfile` showed Public. Changed to Private. Hang persisted: theory partially true, not sufficient |
| 2 Theory B | Layer 4: RDP negotiating over UDP, and that path is partially blocked |
| 3 Test B | Forced TCP-only transport (`SelectTransport` = 1 under the Terminal Services policy key) and restarted `TermService`. Session connected |
| 4 Plan | Keep both changes; note that TCP-only removes UDP performance benefits |
| 5 Implement | Both changes left in place on the host |
| 6 Verify | Connected from LAN, then from a phone hotspot over Tailscale to prove the off-network path |
| 7 Document | Added both causes to SOP-001's failure modes table |

## 7. Case 3: VPN Client Breaks Local Inference

Outcome: the error message named the wrong component. Questioning the obvious (step 2) found the real cause.

| Step | What happened |
| --- | --- |
| 1 Identify | Open WebUI showed brief "thinking" then nothing, or jumbled text. Logs reported a CUDA initialization error |
| 2 Theory A | GPU driver failure, as the error message suggested |
| 3 Test A | `nvidia-smi` showed GPU and driver healthy. Theory rejected |
| 2 Theory B | Something on the host interfering with Ollama's runtime startup. Recent change: NordVPN active with its network filter driver |
| 3 Test B | Disconnected NordVPN; `ollama run` produced clean output immediately. Confirmed |
| 4 Plan | Short term: VPN off during inference. Long term: split tunneling to exclude `ollama.exe` and Docker |
| 5 Implement | VPN disabled; split tunneling pending test |
| 6 Verify | Full prompt in Open WebUI returned correct, formatted output |
| 7 Document | Recorded in SOP-002 failure modes. Lesson: verify the component an error names before trusting it |

## 8. Escalation and Case Template

Escalate when the fault is outside your control (ISP, vendor, client-owned systems) or no tested theory holds. When escalating, give the evidence, not the guess: what layer passes, what fails, and what you already ruled out.

Record each new incident in this format:

```markdown
## Case N: <symptom in plain words>

Outcome: <one sentence>

| Step | What happened |
| --- | --- |
| 1 Identify | Symptoms, what changed, can it be reproduced |
| 2 Theory | Probable cause and the OSI layer |
| 3 Test | Command or check run, and the result |
| 4 Plan | Fix and its side effects |
| 5 Implement | What was changed, or who it was escalated to |
| 6 Verify | Tests passed; preventive measure added |
| 7 Document | Lesson learned; which SOP was updated |
```

## 9. Control Mapping and Revision History

These cases are operational faults, not security incidents, so the mapping is to documented operating procedures and maintenance records rather than to incident response controls. If a case turns out to be a security incident, hand it off to the incident response process (see SOP-006). Verify each reference against the published text before marking Reviewed.

| Runbook element | NIST SP 800-53 Rev 5 | ISO/IEC 27001:2022 Annex A |
| --- | --- | --- |
| One documented diagnostic method for every fault (Sections 3 and 4) | No direct equivalent | 5.37 Documented operating procedures |
| Case log of each fault, its cause, and the repair (Sections 5 to 8) | MA-2 Controlled Maintenance (maintenance and repair records) | 5.37 Documented operating procedures |
| Lessons fed back into the affected SOPs (step 7) | No direct equivalent | 5.37 Documented operating procedures (procedures kept current) |
| Planned fixes with known effects (step 4) | CM-3 Configuration Change Control | 8.32 Change management |
| Escalation to the ISP with evidence (Section 8) | No direct equivalent | 5.22 Monitoring, review and change management of supplier services |

| Version | Date | Change |
| --- | --- | --- |
| 0.1 | 2026-09-29 | Initial draft with three recorded cases |
| 0.2 | 2026-10-03 | Remapped from incident response controls (IR-4, IR-5, ISO 5.25 to 5.27) to operating procedure and maintenance controls, since the cases are operational faults |
