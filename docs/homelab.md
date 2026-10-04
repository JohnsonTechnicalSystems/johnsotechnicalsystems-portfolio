# Homelab

> **Work in progress: every document is a Draft.** Nothing on this site has been verified yet. Commands, steps, and control references have not been checked against primary sources or retested in the lab. Do not rely on any document as authoritative until its status reads Reviewed. See [Review Process](about/review-process.md).

The systems behind the documents. Each lab produces three things: the working configuration and evidence, a procedure that documents it, and the controls it satisfies.

## Built and documented

| System | What was built | Documented in |
| --- | --- | --- |
| Remote access to a Windows workstation | RDP reachable only over a mesh VPN, with NLA, a dedicated least-privilege account, account lockout, and no public listener | [SOP-001](sops/sop-001-secure-remote-access.md) |
| Local AI inference stack | Ollama on the host GPU, Open WebUI in Docker, reachable only over the tailnet | [SOP-002](sops/sop-002-local-llm-inference-stack.md) |
| Fault diagnosis | An ISP WAN outage, an RDP session hang with two stacked causes, and a VPN driver that broke GPU inference | [SOP-003](sops/sop-003-network-troubleshooting-runbook.md) |

## Planned labs

| Lab | Hands-on output | Documentation output | Compliance output |
| --- | --- | --- | --- |
| LAB-01: Firewall and VLAN segmentation | Firewall and managed switch configuration, rule table, inter-VLAN allow and deny test results | Updated SOP-005 and a new firewall rule review SOP | Control matrix rows for SC-7, AC-4, CM-3, CC6.1, CC8.1 |
| LAB-02: Vulnerability scan and remediation | Scan before hardening, fixes, and a rescan showing the difference | Remediation report written for a non-technical owner | RA-5 and SI-2 evidence |
| LAB-03: Packet capture analysis | Captures of DHCP, DNS, the TCP handshake, and a cleartext credential finding | Analysis write-up with display filters | SC-8 finding and recommendation |
| LAB-04: Email authentication | SPF, DKIM, and DMARC on the business domain, with DNS evidence | Step-by-step setup guide | Evidence for email spoofing protection |

## Evidence handling

Published evidence is redacted before it is committed. Public IP addresses are replaced with documentation ranges (192.0.2.0/24, 198.51.100.0/24, 203.0.113.0/24), and serial numbers, wireless keys, account names, and hostnames that identify a real location are removed.
