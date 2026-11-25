# SOP-006: Endpoint Isolation During a Suspected Compromise

Nov 26, 2026 · @Lloyd

## 1. Document Control

| Field | Value |
| --- | --- |
| Document ID | SOP-006 |
| Version | 1.0 |
| Status | Approved |
| Owner | Lloyd Johnson, johnsontechnicalsystems LLC |
| Effective date | 2026-11-26 |
| Next scheduled review | 2027-05-26 |
| Review cycle | Every 6 months, and after every incident that uses this SOP |
| Classification | Internal / Portfolio sample |
| Related | SOP-003 Network Troubleshooting Runbook; SOP-005 VLAN Creation and Segmentation |
| References | NIST SP 800-61 Rev. 3; CISA #StopRansomware Guide; NIST SP 800-86; IETF RFC 3227 |

## 2. Purpose and Scope

This SOP contains a workstation or laptop suspected of compromise quickly and consistently. It stops spread and data exfiltration while preserving evidence for investigation.

**In scope:** organization-managed Windows, macOS, and Linux endpoints at a generic small office. Triggers include EDR or antivirus alerts, ransomware indicators, confirmed phishing payload execution, and unusual outbound traffic flagged by monitoring.

**Out of scope:** servers, cloud workloads, and mobile devices, which follow separate playbooks.

**Assumptions:** the organization has an incident response plan that names an Incident Response Lead, sets reporting times, and names the forensic tools to be used. This SOP is a containment playbook under that plan and does not replace it. If no incident response plan exists, the business owner acts as Incident Response Lead, contacts the organization's IT provider, or its cyber insurer's breach hotline if a policy is held, before any action beyond containment, and follows the evidence steps in Procedure B.

## 3. Isolation Methods

Use the first method available.

| Priority | Method | Keeps remote investigation? |
| --- | --- | --- |
| 1 | EDR network containment (host-based isolation) | Yes, if the EDR product keeps its console connection open during containment. Confirm this for the product in use before an incident |
| 2 | Switch or wireless action: move the switch port to the parking VLAN 999 defined in SOP-005, or shut the port; for Wi-Fi, block the device at the wireless controller | No |
| 3 | Physical disconnect: unplug Ethernet, disable Wi-Fi and Bluetooth on the device | No |

Isolation is not risk-free. RFC 3227 notes that some malware reacts to losing its network connection by destroying evidence. Where the device shows ransomware or active spread, isolate immediately, as CISA directs. Otherwise the Incident Response Lead may choose to collect volatile data (Procedure B, step 1) before isolating. If that collection cannot start within 15 minutes of detection, isolate. The 15-minute limit is this organization's own choice, set to keep the evidence-first option from delaying containment; adjust it in the incident response plan if needed.

## 4. Procedure A: Contain

Run top to bottom. Do not power off, reboot, or log off the device. Shutting down destroys volatile evidence such as running processes, network connections, and memory-resident malware, and NIST SP 800-86 gives volatile data priority over non-volatile data.

The one exception: if the device cannot be isolated by any method in Section 3, power it down to stop the spread, as the CISA #StopRansomware Guide advises. CISA notes that this loses evidence held in volatile memory. Record the decision, the reason, and the time in the ticket.

1. Open an incident ticket. Record the detection time, reporting source, hostname, IP and MAC address, logged-in user, and triggering alert. If the alert indicates ransomware or active spread, perform step 3 first and complete the ticket immediately afterwards.
2. Tell the user to stop using the device, leave it powered on, and stay signed in. If the user's email or chat account may be compromised, use a phone call or another out-of-band channel.
3. Isolate the device using the highest-priority method available (Section 3). If the Incident Response Lead chose to collect volatile data first, isolate as soon as that collection ends, and in any case if it has not started within 15 minutes of detection.
4. Confirm the device no longer reaches internal or internet resources, other than the EDR console if used. For example, check the containment status in the EDR console, or confirm the switch port is down or in VLAN 999.
5. If credential theft is suspected, disable or reset the user's credentials and revoke active sessions and tokens. Do this from a known-clean device, not from the isolated one.

## 5. Procedure B: Preserve, Scope, and Escalate

1. Collect evidence with the tools and method named in the incident response plan. Collect volatile data first, in the order NIST SP 800-86 gives: network connections, login sessions, contents of memory, running processes, open files, network configuration, and operating system time. Then collect relevant logs: EDR telemetry; operating system logs, such as Windows Event Logs, macOS unified logs, or Linux syslog and systemd journal; and proxy, DNS, and firewall logs. For each item, record what was collected, by whom, when, and its hash, and keep a chain-of-custody record. With EDR containment this can often be done remotely through the EDR console; with switch or physical isolation it must be done at the device.
2. Search EDR and SIEM for the same indicators of compromise (file hashes, domains, IPs) on other endpoints, and record the result. Isolate any other affected host with Procedure A.
3. Notify the Incident Response Lead within the time set in the incident response plan. The Incident Response Lead decides whether legal, management, customers, or regulators must be told.
4. Do not reconnect the device until the Incident Response Lead approves. The normal path is to reimage from a known-good baseline, restore data only from backups verified to be clean, confirm the device operates normally, and return it to service with heightened monitoring.
5. After closure, record the timeline, actions, root cause, and lessons learned. Update detection rules, the incident response plan, and this SOP as needed.

## 6. Verification

- [ ] The device cannot reach internal or internet resources (other than the EDR console)
- [ ] The device was not powered off before volatile evidence was collected, or the power-off decision and reason are recorded
- [ ] If isolation waited for evidence collection, the decision and the detection, collection, and isolation times are recorded
- [ ] The incident ticket holds the timeline, evidence list, and chain-of-custody record
- [ ] An IOC search across other endpoints was run and its result recorded
- [ ] Reconnection happened only after Incident Response Lead approval, and restored data came from backups verified to be clean

## 7. Responsible Parties

| Role | Responsibility |
| --- | --- |
| Help Desk / SOC Analyst | Triages the alert, isolates the endpoint, opens the ticket |
| Incident Response Lead | Owns the incident, directs evidence collection, approves reconnection, decides on notifications |
| System Owner / User's Manager | Arranges a temporary device and supports communication |
| Legal / Compliance | Advises on regulatory or contractual notification requirements |

## 8. Control Mapping

Incident handling in this SOP follows NIST SP 800-61 Rev. 3, *Incident Response Recommendations and Considerations for Cybersecurity Risk Management: A CSF 2.0 Community Profile* (April 2025). Rev. 3 supersedes Rev. 2 and organizes its recommendations by the NIST CSF 2.0 Functions, Categories, and Subcategories. It maps the earlier life cycle's containment, eradication, and recovery phase to the Respond and Recover Functions, with improvement under Identify. The SOP's containment, evidence preservation, and escalation steps fall under Respond; reimaging and return to service fall under Recover; lessons learned fall under Identify (Improvement).

| Procedure step | NIST SP 800-53 Rev. 5 | NIST CSF 2.0 | AICPA SOC 2 (2017 TSC) |
| --- | --- | --- | --- |
| Declare and record the incident (Procedure A, step 1) | IR-5 Incident Monitoring | DE.AE-08, RS.MA-02 | CC7.3 |
| Isolate and confirm (Procedure A, steps 2 to 4) | IR-4 Incident Handling | RS.MI-01 | CC7.4 |
| Disable credentials and revoke sessions (Procedure A, step 5) | AC-2 Account Management | RS.MI-01 | CC7.4 |
| Collect evidence with chain of custody (Procedure B, step 1) | IR-4 Incident Handling | RS.AN-06, RS.AN-07 | CC7.4 |
| IOC search across endpoints (Procedure B, step 2) | SI-4 System Monitoring | RS.AN-03, RS.AN-08 | CC7.2 |
| Escalate and notify (Procedure B, step 3) | IR-6 Incident Reporting | RS.MA-04, RS.CO-02 | CC7.4, CC2.3 |
| Reimage, restore, and return to service (Procedure B, step 4) | CP-10 System Recovery and Reconstitution | RC.RP-02, RC.RP-03, RC.RP-05 | CC7.5 |
| Lessons learned (Procedure B, step 5) | IR-4 Incident Handling (part c, lessons learned) | ID.IM-03, ID.IM-04 | CC7.5 |

The AICPA criteria have no official short titles. In brief: CC2.3 covers communication with external parties; CC7.2 monitoring of system components for anomalies; CC7.3 evaluation of security events to decide whether they are incidents; CC7.4 response to security incidents (understand, contain, remediate, communicate); and CC7.5 recovery from security incidents.

Mappings are the author's assertion of intent. They are not a substitute for an assessor's independent determination.

## 9. Revision History

| Version | Date | Change |
| --- | --- | --- |
| 0.1 | 2026-09-29 | Initial draft |
| 0.2 | 2026-10-03 | Cited NIST SP 800-61 Rev. 3 by name and tied the procedures to CSF 2.0 Respond and Recover. Not yet verified against the published text |
| 0.3 | 2026-11-26 | Verified against NIST SP 800-61 Rev. 3, CSF 2.0, the SP 800-53 Rev. 5 catalog, the CISA #StopRansomware Guide, NIST SP 800-86, RFC 3227, and the AICPA 2017 TSC. Corrected the SP 800-61 Rev. 3 title and its mapping to CSF Functions. Replaced the absolute no-power-off rule with CISA's exception. Added the order of volatility, out-of-band contact, clean-backup restore, and a CSF 2.0 column. Mapped credential revocation to AC-2 and recovery to CP-10. Replaced the nonexistent quarantine VLAN with SOP-005's parking VLAN. Added a 15-minute limit on the evidence-first option and a fallback for offices with no incident response plan. Named macOS and Linux log sources to match the scope. Added status, effective date, and next review rows. Removed the milestone row |
| 1.0 | 2026-11-26 | Approved by the owner. Every step, NIST SP 800-61 Rev. 3 reference, and control mapping checked against primary sources, with the owner's decisions on isolation order, the parking VLAN, and the no-plan fallback |
