# SOP-006: Endpoint Isolation During a Suspected Compromise

Sep 29, 2026 · @Lloyd

## 1. Document Control

| Field | Value |
| --- | --- |
| Document ID | SOP-006 |
| Version | 0.2 (Draft) |
| Owner | Lloyd Johnson, Johnson Technical Systems LLC |
| Milestone | Security+ Frameworks |
| Review cycle | Every 6 months, and after every incident that uses this SOP |
| Classification | Internal / Portfolio sample |
| Related | SOP-003 Network Troubleshooting Runbook; SOP-005 VLAN Creation and Segmentation |

## 2. Purpose and Scope

This SOP contains a workstation or laptop suspected of compromise quickly and consistently. It stops spread and data exfiltration while preserving evidence for investigation.

**In scope:** organization-managed Windows, macOS, and Linux endpoints at a generic small office. Triggers include EDR or antivirus alerts, ransomware indicators, confirmed phishing payload execution, and unusual outbound traffic flagged by monitoring.

**Out of scope:** servers, cloud workloads, and mobile devices, which follow separate playbooks.

## 3. Isolation Methods

Use the first method available.

| Priority | Method | Keeps remote investigation? |
| --- | --- | --- |
| 1 | EDR network containment (host-based isolation) | Yes, console connection stays up |
| 2 | Switch port or NAC action: move to a quarantine VLAN (SOP-005) or shut the port; remove from Wi-Fi at the wireless controller | No |
| 3 | Physical disconnect: unplug Ethernet, disable Wi-Fi and Bluetooth on the device | No |

## 4. Procedure A: Contain

Run top to bottom. Do not power off or reboot the device at any point: shutdown destroys volatile evidence such as running processes, network connections, and memory-resident malware.

1. Open an incident ticket. Record the detection time, reporting source, hostname, IP and MAC address, logged-in user, and triggering alert.
2. Tell the user to stop using the device but leave it powered on.
3. Isolate the device using the highest-priority method available (Section 3).
4. Confirm the device no longer reaches internal or internet resources, other than the EDR console if used.
5. If credential theft is suspected, disable or reset the user's credentials and revoke active sessions and tokens.

## 5. Procedure B: Preserve, Scope, and Escalate

1. Following the forensic procedure, capture memory and collect relevant logs: EDR telemetry, Windows Event Logs, and proxy, DNS, and firewall logs. Keep a chain-of-custody record for everything collected.
2. Search EDR and SIEM for the same indicators of compromise (file hashes, domains, IPs) on other endpoints. Isolate any other affected host with Procedure A.
3. Notify the Incident Response Lead within the time set in the IR plan. The IR Lead decides whether legal, management, customers, or regulators must be told.
4. Do not reconnect the device until the IR Lead approves. The normal path is reimage from a known-good baseline, verify, then return to service.
5. After closure, record the timeline, actions, and lessons learned. Update detection rules and this SOP as needed.

## 6. Verification

- [ ] The device cannot reach internal or internet resources (other than the EDR console)
- [ ] The device was not powered off before evidence was collected
- [ ] The incident ticket holds the timeline, evidence list, and chain-of-custody record
- [ ] An IOC search across other endpoints was run and its result recorded
- [ ] Reconnection happened only after IR Lead approval

## 7. Responsible Parties

| Role | Responsibility |
| --- | --- |
| Help Desk / SOC Analyst | Triages the alert, isolates the endpoint, opens the ticket |
| Incident Response Lead | Owns the incident, directs evidence collection, approves reconnection, decides on notifications |
| System Owner / User's Manager | Arranges a temporary device and supports communication |
| Legal / Compliance | Advises on regulatory or contractual notification requirements |

## 8. Control Mapping

Verify each reference against the published text before changing status to Reviewed. Incident handling in this SOP follows NIST SP 800-61 Rev. 3, *Incident Response Recommendations and Considerations for Cybersecurity Risk Management* (April 2025), which organizes incident response around the NIST CSF 2.0 functions. Containment and evidence preservation fall under CSF Respond; reimaging and return to service fall under Recover.

| Procedure step | NIST SP 800-53 Rev 5 | AICPA SOC 2 (TSC 2017) |
| --- | --- | --- |
| Triage and declare (Procedure A, step 1) | IR-5 Incident Monitoring | CC7.3 Evaluation of security events |
| Contain, preserve, eradicate, recover (Procedures A and B) | IR-4 Incident Handling | CC7.4 Incident response |
| Escalate and notify (Procedure B, step 3) | IR-6 Incident Reporting | CC7.4 Incident response |
| Alerts and IOC search (Procedure B, step 2) | SI-4 System Monitoring | CC7.2 Monitoring of system components |
| Lessons learned (Procedure B, step 5) | IR-4 (incorporating lessons learned) | CC7.5 Recovery from incidents |

## 9. Revision History

| Version | Date | Change |
| --- | --- | --- |
| 0.1 | 2026-09-29 | Initial AI-assisted draft; not yet fact-checked |
| 0.2 | 2026-10-03 | Cited NIST SP 800-61 Rev. 3 by name and tied the procedures to CSF 2.0 Respond and Recover. Not yet verified against the published text |
