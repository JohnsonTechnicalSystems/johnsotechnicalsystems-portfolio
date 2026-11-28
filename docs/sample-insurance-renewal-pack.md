---
title: Sample cyber insurance renewal pack for a fictional architecture firm
description: "A cyber insurance renewal pack for a fictional 19-person firm: 30 application answers, the evidence behind them, a gap list and a one-page incident response plan."
---

# Sample cyber insurance renewal pack for Brindlemoor Architects, LLC (fictional)

> **A fictional business, a real method.** A cyber insurance renewal pack for Brindlemoor Architects, LLC, a fictional 19-person architecture firm whose IT is run by a managed service provider (MSP). It contains 30 application questions answered from the facts, the evidence behind each answer, a list of gaps to close before signing, and a one-page incident response plan.

[Download the pack (PDF)](downloads/JTS-Sample-Cyber-Insurance-Renewal-Pack.pdf){ .md-button .md-button--primary } [Download the spreadsheet (.xlsx)](downloads/JTS-Sample-Cyber-Insurance-Renewal-Pack.xlsx){ .md-button }

## About this sample

- Brindlemoor Architects, LLC and Kestrel Ridge IT are fictional. Their facts, dates and figures were invented for this sample, and any resemblance to a real business is unintended. The phone number uses the 555-01xx range reserved for fictional use.
- The questions were written by Johnson Technical Systems in the style of common cyber insurance applications. They are not copied from any insurer's form. On real work, the answers are written against the insurer's own form, question by question.
- An answer is Yes only when the control is in place and there is evidence of it on the date shown. A control that is planned is answered No or Partial until it is done.
- The NIST CSF 2.0 references show where each topic sits in the framework, for readers who use it. Insurers do not ask for them. They are not an assessment.
- Every NIST CSF identifier, and the Windows 10 end-of-support date, was checked against the sources listed below in November 2026.
- This is preparation help. It is not legal or insurance advice, and it does not guarantee coverage or a premium. The business reviews and signs its own application and is responsible for its answers.

## 1. Business profile

This is the intake summary the answers are written from.

| Item | Detail |
| --- | --- |
| **Business** | Brindlemoor Architects, LLC (fictional). An architecture firm with one office, founded in 2009. 19 people: 2 principals, 14 architects and designers, an office manager, a bookkeeper and a marketing coordinator. |
| **IT support** | Kestrel Ridge IT (fictional), a managed service provider, under a monthly contract. This pack is delivered through the MSP, under its name. |
| **Systems** | Microsoft 365 for email, files and sign-in. 21 computers: 12 laptops, 5 desktops, 3 CAD workstations and 1 PC that drives the large-format plotter. One file server in the office that holds the project archive. Cloud accounting software and a cloud payroll provider. A managed firewall with a VPN, and separate staff and guest Wi-Fi. |
| **Information held** | Client project files, drawings and contracts. HR and payroll records for about 60 current and former employees. Business contact details for about 900 client and consultant contacts. No payment card data (clients pay by check or bank transfer) and no health records. |
| **Policy** | The current cyber policy renews on 1 February 2027. The application is due to the broker by 15 January 2027. |
| **Prepared** | November 2026, from the MSP's reports dated 10 to 13 November 2026, a 40-minute call with the office manager and one principal, and a call with the bookkeeper on 13 November 2026, with screenshots. |

## 2. Summary for the principals

Of the 30 questions, 7 are answered Yes, 12 Partial and 5 No; 5 are descriptive and 1 does not apply. Ten gaps are listed in section 5. Six are rated High, and five of those can be closed before the application is due on 15 January 2027 without new spending; the sixth, the plotter PC (G4), needs a decision on cost. The plotter PC part of G3 depends on that decision too. Five weaker answers are not listed as gaps for this renewal; see the note under section 5. Each answer in this pack describes the position in November 2026. Before signing, the answers must be updated to the position on that day: a gap that has been closed, with evidence, becomes Yes, and a gap that is still open stays as it is.

## 3. Application answers

| Status | Meaning | Count |
| --- | --- | --- |
| Yes | In place today, with evidence. | 7 |
| Partial | Partly in place; the answer says what is and is not. | 12 |
| No | Not in place on the date of this pack. | 5 |
| N/A | Does not apply, with the reason. | 1 |
| Info | A descriptive question with no yes or no answer. | 5 |

### Business and data

**1. Describe your business and the sensitive information you hold.**

An architecture firm with 19 staff and one office. We hold client project files, drawings and contracts, and HR and payroll records for our own staff. We do not hold payment card data or health records.

<div class="jts-meta" markdown>

- **Status** Info
- **Evidence** Company profile; data inventory
- **Confirmed by** Principal
- **NIST CSF 2.0** ID.AM-07

</div>

**2. About how many records containing personal information do you hold?**

HR and payroll records for about 60 current and former employees, including Social Security numbers. These are held by our payroll provider, with copies of onboarding forms in a restricted HR folder in Microsoft 365. We also hold business contact details for about 900 client and consultant contacts.

<div class="jts-meta" markdown>

- **Status** Info
- **Evidence** Payroll provider employee count; HR folder permissions report
- **Confirmed by** Office manager
- **NIST CSF 2.0** ID.AM-07

</div>

**3. Do you accept, process or store payment card data?**

No. Clients pay by check or bank transfer. We do not take card payments.

<div class="jts-meta" markdown>

- **Status** N/A
- **Evidence** Accounting software payment settings
- **Confirmed by** Bookkeeper
- **NIST CSF 2.0** None

</div>

**4. Who manages your IT and security?**

Kestrel Ridge IT, a managed service provider, under a monthly contract that covers the help desk, device management, patching, backups, the firewall and security monitoring during business hours. We have no IT staff of our own. The office manager is the MSP's main contact.

<div class="jts-meta" markdown>

- **Status** Info
- **Evidence** MSP service agreement
- **Confirmed by** MSP; office manager
- **NIST CSF 2.0** GV.SC-04, GV.RR-02

</div>

### Email and sign-in

**5. Is multi-factor authentication (MFA) required for all email accounts?**

Yes. A conditional access policy requires MFA for all 19 users, and older sign-in methods that cannot use MFA are blocked. All 19 users are registered for MFA.

<div class="jts-meta" markdown>

- **Status** Yes
- **Evidence** Conditional access policy export; MFA registration report, 12 November 2026
- **Confirmed by** MSP report
- **NIST CSF 2.0** PR.AA-03

</div>

**6. Is MFA required for all remote access to your network?**

Partly. The VPN requires a Microsoft 365 sign-in with MFA. However, the accounting software vendor's remote support tool is installed on the bookkeeper's PC and allows unattended access with a password only. See gap G1.

<div class="jts-meta" markdown>

- **Status** Partial
- **Evidence** VPN configuration; installed software report, 12 November 2026
- **Confirmed by** MSP report
- **NIST CSF 2.0** PR.AA-03

</div>

**7. Is MFA required for all administrator accounts?**

Yes. The MSP's technicians use separate, named administrator accounts with MFA. There are two global administrator accounts and one emergency account. The emergency account signs in with a FIDO2 security key, which a principal keeps offline with its password.

<div class="jts-meta" markdown>

- **Status** Yes
- **Evidence** Administrator role report, 12 November 2026
- **Confirmed by** MSP report
- **NIST CSF 2.0** PR.AA-03, PR.AA-05

</div>

**8. Is MFA required for cloud applications that hold financial or personal data?**

Partly. The payroll provider enforces MFA for every user. The accounting software offers MFA, and it is turned on for two of its three users; one principal has not enrolled. See gap G2.

<div class="jts-meta" markdown>

- **Status** Partial
- **Evidence** Payroll security settings; accounting software user list, 13 November 2026
- **Confirmed by** Bookkeeper; screenshots
- **NIST CSF 2.0** PR.AA-03

</div>

**9. Do you filter email for malicious links and attachments, and use SPF, DKIM and DMARC?**

Partly. Link and attachment scanning are turned on in Microsoft 365. SPF and DKIM are set up for our domain. DMARC is published in monitoring mode only (p=none), so messages that fail the check are still delivered. See gap G5.

<div class="jts-meta" markdown>

- **Status** Partial
- **Evidence** Email security policy export; DNS records, 10 November 2026
- **Confirmed by** MSP report
- **NIST CSF 2.0** DE.CM-01

</div>

### Computers and updates

**10. Is endpoint detection and response (EDR) installed on all computers and servers?**

Partly. EDR is installed on 20 of 22 devices (21 computers and the file server). It is missing from the plotter PC and from one CAD workstation, where it was removed during troubleshooting in August 2026 and not put back. See gap G3.

<div class="jts-meta" markdown>

- **Status** Partial
- **Evidence** EDR device list, 12 November 2026
- **Confirmed by** MSP report
- **NIST CSF 2.0** DE.CM-09

</div>

**11. Are security alerts monitored around the clock?**

Partly. The MSP reviews EDR alerts during business hours, Monday to Friday. Outside those hours the EDR tool isolates a device automatically on a high-severity alert, but no one reviews alerts until the next business day.

<div class="jts-meta" markdown>

- **Status** Partial
- **Evidence** MSP service agreement; EDR response policy
- **Confirmed by** MSP
- **NIST CSF 2.0** DE.CM-09, DE.AE-02

</div>

**12. Are critical security updates installed within 30 days?**

Partly. Windows and Microsoft 365 updates are installed by the MSP: in October 2026, all 21 supported Windows devices were updated within 30 days, 20 of them within 14 days. The plotter PC gets no Windows security updates; see question 13 and gap G4. Updates to the CAD software are installed by staff when prompted and are not tracked.

<div class="jts-meta" markdown>

- **Status** Partial
- **Evidence** Patch compliance report, October 2026
- **Confirmed by** MSP report
- **NIST CSF 2.0** ID.RA-01, PR.PS-02

</div>

**13. Is all of your software still supported by its vendor?**

No. The plotter PC runs Windows 10, which reached end of support on October 14, 2025. It is not enrolled in extended security updates and it is on the staff network. See gap G4.

<div class="jts-meta" markdown>

- **Status** No
- **Evidence** Operating system inventory, 12 November 2026
- **Confirmed by** MSP report
- **NIST CSF 2.0** PR.PS-02, ID.AM-08

</div>

**14. Are laptops encrypted?**

Yes. Full-disk encryption (BitLocker) is turned on and reported as compliant on all 12 laptops, enforced through device management.

<div class="jts-meta" markdown>

- **Status** Yes
- **Evidence** Device compliance report, 12 November 2026
- **Confirmed by** MSP report
- **NIST CSF 2.0** PR.DS-01

</div>

**15. Do staff work without administrator rights on their computers?**

Partly. 16 staff are standard users. The three CAD workstation users have local administrator rights so that they can install plug-ins.

<div class="jts-meta" markdown>

- **Status** Partial
- **Evidence** Local administrators report, 12 November 2026
- **Confirmed by** MSP report
- **NIST CSF 2.0** PR.AA-05

</div>

### Backups

**16. Do you back up critical data regularly?**

Yes. The file server is backed up every night to a storage device in the office and to a cloud backup service. Microsoft 365 mailboxes and files are backed up daily by a separate cloud backup service.

<div class="jts-meta" markdown>

- **Status** Yes
- **Evidence** Backup job history, October and November 2026
- **Confirmed by** MSP report
- **NIST CSF 2.0** PR.DS-11

</div>

**17. Is at least one backup copy offline or immutable, so that an attacker cannot change or delete it?**

Partly. The cloud copy is separate from the office network and uses its own sign-in with MFA. Its immutability setting, which stops backups being deleted before a set date, is available but not turned on. See gap G6.

<div class="jts-meta" markdown>

- **Status** Partial
- **Evidence** Cloud backup console settings, 13 November 2026
- **Confirmed by** MSP report
- **NIST CSF 2.0** PR.DS-11

</div>

**18. Are backups encrypted?**

Yes. Both the office copy and the cloud copies are encrypted, and the MSP holds the encryption keys in its password manager.

<div class="jts-meta" markdown>

- **Status** Yes
- **Evidence** Backup configuration, 13 November 2026
- **Confirmed by** MSP report
- **NIST CSF 2.0** PR.DS-11, PR.DS-01

</div>

**19. Have you tested restoring from backup in the last 12 months?**

Partly. Individual files are restored on request; the most recent was on 3 November 2026. The last full restore of the file server was tested in September 2025, which is 14 months ago. See gap G7.

<div class="jts-meta" markdown>

- **Status** Partial
- **Evidence** Restore tickets; September 2025 restore test record
- **Confirmed by** MSP report
- **NIST CSF 2.0** PR.DS-11

</div>

**20. How long would it take to recover your critical systems?**

About two business days for the file server. This estimate is based on the September 2025 test, in which the data restore took 9 hours, plus time to rebuild the server. It is an estimate, not a guarantee. Email and Microsoft 365 files do not depend on the office.

<div class="jts-meta" markdown>

- **Status** Info
- **Evidence** September 2025 restore test record
- **Confirmed by** MSP
- **NIST CSF 2.0** RC.RP-01

</div>

### Network and remote access

**21. Is your network protected by a firewall, and is remote desktop closed to the internet?**

Yes. The MSP manages the firewall. There are no inbound port forwards, and an external scan on 10 November 2026 found no remote desktop or other management ports open.

<div class="jts-meta" markdown>

- **Status** Yes
- **Evidence** Firewall rule export; external scan report, 10 November 2026
- **Confirmed by** MSP report
- **NIST CSF 2.0** PR.IR-01

</div>

**22. Is guest Wi-Fi separated from your business network?**

Yes. Guests use a separate network that cannot reach staff devices or the file server.

<div class="jts-meta" markdown>

- **Status** Yes
- **Evidence** Wireless configuration export
- **Confirmed by** MSP report
- **NIST CSF 2.0** PR.IR-01

</div>

**23. Is your internal network segmented, so that servers are separated from staff computers?**

No. The file server, staff computers, the plotter PC and the printers share one network.

<div class="jts-meta" markdown>

- **Status** No
- **Evidence** Network diagram, November 2026
- **Confirmed by** MSP
- **NIST CSF 2.0** PR.IR-01

</div>

### People and payments

**24. Do all staff complete security awareness training at least once a year?**

Partly. Training is assigned every year through the MSP's training platform, and phishing simulations run every quarter. 17 of 19 staff have completed the 2026 training; two are outstanding. See gap G8.

<div class="jts-meta" markdown>

- **Status** Partial
- **Evidence** Training completion report; phishing simulation results, 13 November 2026
- **Confirmed by** MSP report
- **NIST CSF 2.0** PR.AT-01

</div>

**25. Do you confirm requests to change bank details or to send money by calling a known number?**

Partly. The bookkeeper does call back on a number already on file, but the practice is not written down and no one else is trained to do it when she is away. See gap G9.

<div class="jts-meta" markdown>

- **Status** Partial
- **Evidence** Call with the bookkeeper, 13 November 2026
- **Confirmed by** Bookkeeper
- **NIST CSF 2.0** None

</div>

**26. Do payments above a set amount need approval from a second person?**

No. The bookkeeper can create and release bank transfers of any amount alone. See gap G9.

<div class="jts-meta" markdown>

- **Status** No
- **Evidence** Bank portal user roles, 13 November 2026
- **Confirmed by** Bookkeeper; screenshot
- **NIST CSF 2.0** PR.AA-05

</div>

### Incident response and vendors

**27. Do you have a written incident response plan?**

No. There was no written plan at the time of this review. A one-page plan was drafted as part of this pack and is included below. The answer becomes Yes once the principals adopt it and staff have been told where it is. See gap G10.

<div class="jts-meta" markdown>

- **Status** No
- **Evidence** Call with the principal, 13 November 2026
- **Confirmed by** Principal
- **NIST CSF 2.0** ID.IM-04

</div>

**28. Have you tested your incident response plan in the last 12 months?**

No. There has been no plan to test. A one-hour walk-through with the MSP is proposed under gap G10.

<div class="jts-meta" markdown>

- **Status** No
- **Evidence** Call with the principal, 13 November 2026
- **Confirmed by** Principal
- **NIST CSF 2.0** ID.IM-02

</div>

**29. Do your contracts with key vendors include security requirements, and do you review those vendors?**

Partly. The MSP agreement includes confidentiality terms and a duty to report security incidents to us. We have not reviewed the security reports of the payroll provider or the accounting software vendor.

<div class="jts-meta" markdown>

- **Status** Partial
- **Evidence** MSP service agreement
- **Confirmed by** Office manager
- **NIST CSF 2.0** GV.SC-05, GV.SC-07

</div>

### History

**30. In the past three years, have you had a security incident, a claim, or circumstances that could lead to a claim?**

Yes, one incident. In March 2025 a staff member's mailbox was accessed after a phishing email, before MFA was required for every account. It was found two days later through an alert on a new mail-forwarding rule. The MSP reset the account, removed the rule and reviewed the sign-in logs, and found no access beyond that mailbox. No claim was made. The broker was told in April 2025. MFA has been required for all accounts since April 2025.

<div class="jts-meta" markdown>

- **Status** Info
- **Evidence** MSP incident ticket, March 2025; email to the broker, April 2025
- **Confirmed by** MSP ticket; principal
- **NIST CSF 2.0** RS.MA-01, RS.CO-02

</div>

## 4. Evidence summary

What proves each group of answers, where it came from and when it was captured. The files are kept in one folder so that they can be produced if the insurer asks, or if a claim is ever made.

| Control | Evidence | Source | Captured | Questions |
| --- | --- | --- | --- | --- |
| Business, data and IT support | Company profile; data inventory; payroll provider employee count; HR folder permissions report; accounting software payment settings; MSP service agreement | Principal; office manager; bookkeeper; contract | November 2026 | 1 to 4 |
| MFA on email and administrator accounts | Conditional access policy export; MFA registration report; administrator role report | Microsoft 365 admin center, exported by the MSP | 12 November 2026 | 5, 7 |
| MFA on remote access and cloud applications | VPN configuration; installed software report; payroll and accounting user settings | MSP tools; screenshots from the bookkeeper | 12 and 13 November 2026 | 6, 8 |
| Email protection | Email security policy export; SPF, DKIM and DMARC records | Microsoft 365 admin center; public DNS | 10 November 2026 | 9 |
| EDR coverage and alert handling | EDR device list; response policy; MSP service agreement | EDR console; contract | 12 November 2026 | 10, 11 |
| Updates and supported software | Patch compliance report; operating system inventory | MSP management tool | October and November 2026 | 12, 13 |
| Encryption and administrator rights | Device compliance report; local administrators report | Device management | 12 November 2026 | 14, 15 |
| Backups | Backup job history; cloud backup console settings; backup configuration; restore tickets; September 2025 restore test record | Backup consoles; MSP tickets | 13 November 2026 | 16 to 20 |
| Network | Firewall rule export; external scan report; wireless configuration; network diagram | Firewall; external scanner | 10 November 2026 | 21 to 23 |
| Training | Training completion report; phishing simulation results | MSP training platform | 13 November 2026 | 24 |
| Payment controls | Bank portal user roles; notes of the call with the bookkeeper | Bank portal; call notes | 13 November 2026 | 25, 26 |
| Incident response plan and vendors | Notes of the call with the principal; MSP service agreement | Call notes; contract | 13 November 2026 | 27 to 29 |
| Incident history | MSP incident ticket; email to the broker | MSP ticketing system; principal's email | March and April 2025 | 30 |

## 5. Gap list

Controls the application asks about that are not fully in place. Deal with them by priority, then by target date. Priority reflects how heavily insurers commonly weigh the control and how exposed the firm is today.

| # | Gap | Questions | Priority | What to do | Owner | Target date |
| --- | --- | --- | --- | --- | --- | --- |
| G1 | Remote support tool on the bookkeeper's PC allows unattended access with a password only | 6 | High | Remove the tool, or set it to attended sessions only, started by the bookkeeper | MSP | 4 December 2026 |
| G2 | One principal has not turned on MFA in the accounting software | 8 | High | Enrol the principal; then make MFA mandatory for all users in the software's settings | Principal; bookkeeper | 4 December 2026 |
| G3 | EDR missing from the plotter PC and one CAD workstation | 10 | High | Reinstall on the CAD workstation by 4 December. For the plotter PC, see G4: replacing it with a supported PC that has EDR closes this gap; isolating it leaves question 10 at Partial | MSP | 4 December 2026 (CAD workstation) |
| G4 | Plotter PC runs Windows 10, which is out of support, on the staff network | 12, 13 | High | Replace the PC, or move it to its own network that can reach only the plotter and the print queue, with no access to the staff network or the internet. Isolation reduces the risk but does not close the gap: questions 12 and 13 stay Partial and No until the PC is replaced or enrolled in extended security updates | MSP; principal to approve cost | 8 January 2027 |
| G5 | DMARC is in monitoring mode only | 9 | Medium | Review the DMARC reports for two weeks, then move to quarantine and later to reject | MSP | 8 January 2027 |
| G6 | Cloud backup immutability is not turned on | 17 | High | Turn on immutability with a 30-day period and confirm in the console | MSP | 4 December 2026 |
| G7 | No full restore test in the last 12 months | 19, 20 | Medium | Restore the file server to a test machine, time it, and record the result | MSP | 18 December 2026 |
| G8 | Two staff have not completed the 2026 training | 24 | Low | Complete the training | Office manager | 4 December 2026 |
| G9 | Call-back check is unwritten, and one person can release any payment alone | 25, 26 | High | Write a half-page payment procedure; turn on dual approval in the bank portal above an amount the principals choose | Principals; bookkeeper | 18 December 2026 |
| G10 | No adopted or tested incident response plan | 27, 28 | Medium | Principals adopt the one-page plan below; fill in the contact numbers; hold a one-hour walk-through with the MSP | Principals; MSP | 18 December 2026 |

**Not listed as gaps for this renewal:** question 11 (no alert review outside business hours), question 12 (CAD software updates not tracked), question 15 (local administrator rights on the three CAD workstations), question 23 (no network segmentation) and question 29 (payroll and accounting vendors not reviewed). Each needs budget or a longer project. They were raised with the principals and the MSP for after the renewal, and the answers stay as written until they are fixed.

## 6. One-page incident response plan

Drafted for adoption by the principals (gap G10). Names and numbers are completed by the firm; the numbers shown are placeholders.

| Role | Who | What they do |
| --- | --- | --- |
| Incident lead | Principal (name, mobile number) | Decides, approves spending, speaks to clients |
| Deputy | Office manager (name, mobile number) | Leads if the principal cannot be reached; keeps the incident log |
| IT response | Kestrel Ridge IT help desk, 555-0100, business hours. Out of hours: the MSP's emergency number (to be confirmed with the MSP); if there is none, call the insurer's breach hotline | Contains the problem, preserves evidence, restores systems |
| Insurer | Breach hotline (number) and policy number (number), both from the policy schedule | Appoints legal counsel and forensic help. Call before hiring anyone else |
| Bank | Fraud line (number), also on the back of the bank token | Recalls or freezes a fraudulent payment |

1. **Report it at once.** Anyone who sees something wrong (a ransom note, a strange sign-in alert, a payment they did not make, a lost laptop) calls the MSP help desk and tells the incident lead. Do not wait to be sure.
2. **Disconnect, do not switch off.** Unplug the network cable or turn off Wi-Fi on the affected computer. Leave it powered on, and do not delete anything, so that evidence is kept.
3. **Contain.** The MSP isolates affected devices, resets the passwords of affected accounts, signs those accounts out everywhere, and checks for new inbox rules (forwarding, moving or deleting mail), new MFA methods, newly approved apps and new administrator accounts.
4. **Call the insurer's breach hotline** before hiring a lawyer, a forensic firm or a ransom negotiator. The policy may pay only for firms the insurer approves.
5. **If money has been sent,** call the bank's fraud line immediately and ask for a recall. Every hour matters.
6. **Work out what was affected.** With the MSP and the insurer's advisers, list the systems, the accounts and the kinds of information involved, and keep a dated log of every action.
7. **Notify.** Counsel appointed through the insurer advises whether clients, employees or regulators must be told, and by when. No one else sends notices or speaks to the press.
8. **Recover.** The MSP restores from a backup taken before the incident, after checking that the backup is clean, and confirms that the way in has been closed.
9. **Review within two weeks.** Record what happened, what worked and what did not, and update this plan and the gap list.

A printed copy is kept in the office safe and at each principal's home, because the plan may be needed when the computers are not working.

## 7. NIST CSF 2.0 references used

| Reference | What it covers |
| --- | --- |
| GV.RR-02 | Roles, responsibilities and authorities for cybersecurity risk management are established |
| GV.SC-04 | Suppliers are known and prioritized by criticality |
| GV.SC-05 | Supply chain cybersecurity requirements are integrated into contracts |
| GV.SC-07 | Supplier risks are understood, recorded and monitored |
| ID.AM-07 | Inventories of data are maintained |
| ID.AM-08 | Systems, hardware, software, services and data are managed throughout their life cycles |
| ID.RA-01 | Vulnerabilities in assets are identified, validated and recorded |
| ID.IM-02 | Improvements are identified from security tests and exercises |
| ID.IM-04 | Incident response plans are established, communicated, maintained and improved |
| PR.AA-03 | Users, services and hardware are authenticated |
| PR.AA-05 | Access permissions are managed with least privilege and separation of duties |
| PR.AT-01 | Personnel are given awareness and training |
| PR.DS-01 | Data-at-rest is protected |
| PR.DS-11 | Backups of data are created, protected, maintained and tested |
| PR.PS-02 | Software is maintained, replaced and removed commensurate with risk |
| PR.IR-01 | Networks and environments are protected from unauthorized logical access and usage |
| DE.CM-01 | Networks and network services are monitored to find potentially adverse events |
| DE.CM-09 | Computing hardware and software are monitored to find potentially adverse events |
| DE.AE-02 | Potentially adverse events are analyzed |
| RS.MA-01 | The incident response plan is executed once an incident is declared |
| RS.CO-02 | Internal and external stakeholders are notified of incidents |
| RC.RP-01 | The recovery portion of the incident response plan is executed |

The descriptions above are summaries; see the source document for the exact wording.

## Reviewer notes

Answers that changed during review. On real work, these notes go to the MSP or the business with the draft, so that nothing is overstated on a signed application.

| Question | What changed in review |
| --- | --- |
| Q6 | The MSP's first draft answered Yes, because the VPN requires MFA. The installed software report showed a vendor's remote support tool with unattended, password-only access. The answer was changed to Partial and the tool became gap G1. |
| Q10 | The draft said EDR was on "all endpoints". The device list showed 20 of 22, so the answer gives the count and names the two devices. |
| Q13 | The plotter PC was missing from the first inventory because it is not used for email. It was added after the EDR device list and the network diagram were compared. |
| Q17 | The draft said backups were "immutable". The cloud copy is separate and protected by MFA, but the immutability setting was off. The answer says exactly that. |
| Q19 | The draft said restores are "tested regularly". File restores are routine, but the last full restore test was 14 months ago. The answer gives both dates. |
| Q27 | The plan in this pack was written during the engagement. The answer stays No until the principals adopt it, because the application asks about the position on the day it is signed. |
| Q30 | The principal's first answer was "no incidents". The MSP's ticket history showed the March 2025 mailbox compromise. It is disclosed, with what was done about it. |

## Sources

- **NIST CSF references:** NIST CSWP 29, The NIST Cybersecurity Framework (CSF) 2.0, February 26, 2024.
- **Windows 10 end of support:** Microsoft Lifecycle, Windows 10 Home and Pro, which gives the end of support date as October 14, 2025 (learn.microsoft.com/lifecycle/products/windows-10-home-and-pro).

## Want one like this for your business or your clients?

[See renewal packs](insurance-pack.md){ .md-button .md-button--primary } [Book a 15-minute call](https://cal.com/lloyd-johnson){ .md-button }

<small>Documentation and preparation services only. Not legal or insurance advice, and not a guarantee of coverage or premium.</small>
