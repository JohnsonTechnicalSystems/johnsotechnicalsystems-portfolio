---
title: Sample written information security plan (WISP) for a fictional tax practice
description: "A written information security plan for a fictional four-person tax and bookkeeping firm, covering each element of the FTC Safeguards Rule."
---

# Sample written information security plan (WISP) for Cobbleton Tax & Bookkeeping, LLC (fictional)

> **A fictional firm, a real method.** A written information security plan for Cobbleton Tax & Bookkeeping, LLC, a fictional four-person tax and bookkeeping firm. It covers each element of the FTC Safeguards Rule and shows which parts a firm with fewer than 5,000 consumers is exempt from, and what it keeps anyway in a lighter form.

[Download the PDF](downloads/JTS-Sample-WISP-Tax-Practice.pdf){ .md-button .md-button--primary }

## About this sample

- Cobbleton Tax & Bookkeeping, LLC is a fictional firm. Its facts, dates and figures were invented for this sample.
- The plan follows the outline in IRS Publication 5708 and was written from scratch by Johnson Technical Systems. A client's plan is written the same way, from the client's own intake answers.
- Section 11 lists each paragraph of 16 CFR 314.4 with its status for this firm: required and in place, or exempt under § 314.6.
- Every citation was checked against the regulation text and the IRS sources named in section 11 in November 2026.
- Breach notification duties depend on federal and state law. A real plan should be reviewed by counsel.

## Document control

| Field | Value |
| --- | --- |
| Qualified Individual | Owner and Enrolled Agent |
| Approved by | Owner (sole member of the LLC) |
| Version | 1.2 |
| Status | Approved |
| Effective date | October 2026 |
| Classification | Internal |
| Next review | October 2027, before filing season, or sooner after a security event or major change |

## 1. Objective, purpose and scope

This plan sets out the administrative, technical and physical safeguards Cobbleton uses to protect client information, as the FTC Safeguards Rule (16 CFR Part 314) requires of tax preparers. It applies to everyone who works for the firm, including seasonal preparers, and to client information in every form: paper, electronic and spoken.

Client information here means anything a client gives us or we create for them, such as names with Social Security numbers, dates of birth, bank account and routing numbers for refunds, W-2s, 1099s, prior-year returns, copies of identity documents and bookkeeping records.

**The firm:** one office, the owner, one office manager and two seasonal preparers (January to April, and again before the October extension deadline). About 1,400 individual and small business clients.

## 2. Qualified Individual and authorized users

The owner is the Qualified Individual, responsible for overseeing, carrying out and enforcing this plan. An outside IT provider sets up and maintains the firm's computers and Microsoft 365 under contract; the owner remains responsible for the plan and reviews the provider's work.

| Role | Access | Responsibilities under this plan |
| --- | --- | --- |
| Owner (Qualified Individual) | All systems; administrator in the tax software, and in Microsoft 365 through a separate administrator account | Approves access and changes, reviews logs, runs the yearly risk review, leads incident response |
| Office manager | Microsoft 365, client portal, and scheduling and billing in the tax software; no administrator rights | Onboards and offboards staff from the checklist, keeps the training and visitor records, handles paper files |
| Seasonal preparers (2) | Microsoft 365; tax software and client portal for assigned clients only | Follow the code of conduct in section 10; report anything suspicious at once |
| Outside IT provider | Microsoft 365 and device management, through a separate named administrator account with multi-factor authentication | Maintains devices, updates and backups; reports security alerts to the owner the same day |

## 3. Risk assessment

The owner reviews these risks every October before filing season, and again after any security event or major change, such as new software or a new office. The firm keeps this written assessment even though firms with fewer than 5,000 consumers are exempt from the written-assessment requirements in § 314.4(b)(1). Each October the owner also confirms the firm is still under 5,000 consumers, counting spouses on joint returns and former clients whose records are still kept. The October 2026 count was about 3,100.

| Risk | Rating | Main safeguards (section) |
| --- | --- | --- |
| Phishing email steals a staff password, often posing as a client or the IRS | High | Multi-factor authentication everywhere, training before each season, email filtering (5.1, 5.4, 7) |
| Lost or stolen laptop | Medium | Full-disk encryption, remote wipe, no client files saved locally (5.2, 5.4) |
| Ransomware or malware | Medium | Endpoint protection, automatic updates, no administrator rights for daily work, cloud backups (5.4, 6) |
| Client documents sent by plain email | Medium | Client portal for all uploads; encrypted email when email is unavoidable (5.2) |
| Former seasonal staff keep access | Medium | Accounts disabled at the end of the last shift (7) |
| Paper files seen or taken from the office | Low | Locked cabinets, clean desk, visitors escorted, shredding service (5.3, 5.4) |
| A vendor is breached | Low | Vendors chosen and reviewed against section 8; contracts require safeguards |

## 4. Information and hardware inventory

| Item | Location | Client information it holds or processes |
| --- | --- | --- |
| Cloud tax software | Vendor-hosted | Returns, workpapers, e-file records |
| Client portal (part of the tax software) | Vendor-hosted | Documents clients upload; signed engagement letters and e-file authorizations |
| Microsoft 365 Business Premium | Microsoft-hosted | Email, scanned documents in OneDrive, bookkeeping files |
| Four laptops (owner, office manager, two preparers) | Office; owner's laptop also at home | Access to the systems above; nothing stored locally by policy |
| Office scanner and printer | Office | Passes scans to OneDrive; its memory is wiped before disposal |
| Locked file cabinets | Office back room | Paper documents from clients who do not use the portal, kept until scanned and returned or shredded |
| Cloud backup service | Vendor-hosted | Encrypted daily copies of Microsoft 365 email and OneDrive |
| Office router and firewall | Office | Separate staff and guest Wi-Fi networks |

## 5. Safeguards

### 5.1 Access control and multi-factor authentication

- Each person has their own account in every system. Accounts are never shared, and each person gets only the access their role needs (section 2). The only exception is the router's single administrator login (5.4).
- Multi-factor authentication is required on Microsoft 365, laptop sign-in (Windows Hello for Business), the tax software, the client portal, the cloud backup service, the IRS e-Services account and the firm's bank. Authenticator apps or security keys are used, not text messages, where the service allows it. Where a system cannot use multi-factor authentication, such as the router, the owner approves in writing an alternative control that is reasonably equivalent or more secure, as § 314.4(c)(5) allows.
- The owner reviews who has access to each system every January and every October.

### 5.2 Encryption and sending client information

- Laptops use full-disk encryption (BitLocker), enforced through Microsoft Intune. Data in the tax software, client portal and Microsoft 365 is encrypted by those services at rest and in transit.
- Clients send documents through the client portal. Staff never ask for, or send, client information, such as Social Security numbers or bank details, by plain email or text. When email is unavoidable, staff use Microsoft 365 message encryption.

### 5.3 Retention and disposal

- Returns and workpapers are kept for seven years after filing, because clients regularly need them for amended returns, notices and loan applications. This is the firm's recorded business reason for keeping them past the two-year disposal limit in § 314.4(c)(6).
- Records of current and former clients are deleted, or shredded if on paper, within 90 days after their seven years end, unless a legal hold applies. This applies in every place they are kept: the tax software, the client portal, and Microsoft 365 email and OneDrive. Copies in the cloud backups expire within one year after that, when the backup history rolls over (5.4). Paper from clients is scanned and returned or shredded within 30 days.
- The owner reviews this retention schedule every October and removes anything kept without a business reason, as § 314.4(c)(6)(ii) requires.
- Shredding is done by a bonded service, which provides a certificate for each pickup. Laptops and the scanner are wiped by the IT provider before re-use or disposal.

### 5.4 Devices, network and remote work

- Only firm laptops managed through Intune may access client information. Each runs Microsoft Defender for Business, installs updates automatically and locks after 5 minutes. A lost laptop can be wiped remotely through Intune. Staff do daily work without administrator rights.
- Incoming email is filtered for phishing and malware by the email protection included in the firm's Microsoft 365 plan.
- The IT provider backs up Microsoft 365 email and OneDrive every day to a separate cloud backup service. Backups are encrypted, use their own sign-in with multi-factor authentication, cannot be deleted from the firm's Microsoft 365 accounts, and keep one year of history. The tax software vendor backs up the returns and portal data it hosts, under the license agreement.
- Clients and visitors use the guest Wi-Fi, which cannot reach the staff network. The router's administrator password is unique, held by the IT provider and the owner, and changed when IT provider staff change. The router can be managed only from the staff network, not from the internet, and its firmware is kept up to date.
- Remote work is allowed only on a firm laptop over a home network or a phone hotspot, never on public Wi-Fi.
- Paper files stay in locked cabinets when not in use. Visitors are escorted and signed in.

### 5.5 Monitoring, logging and change management

- Every week the IT provider checks each mailbox for forwarding rules the firm did not set up and reviews the Microsoft 365 sign-in logs and the audit log, which the IT provider has turned on, for bulk downloads, outside sharing and unusual mailbox access, and tells the owner the same day if anything looks wrong. Security alerts that the firm's Microsoft 365 plan provides go to the owner and the IT provider.
- The owner reviews the tax software's user activity report every week during filing season and the October extension period, and every month the rest of the year.
- Any change to systems, such as new software, a new user or a firewall change, is approved by the owner and recorded in the change log before it is made.

### 5.6 Software the firm uses

The firm does not develop its own software. Before adopting any new software that would hold client information, the owner checks that it supports multi-factor authentication and encryption, and that the vendor will sign a contract committing to safeguards (section 8). Each October the owner also reviews the vendor security reports and advisories for software already in use.

## 6. Testing and monitoring

The owner and the IT provider check the key safeguards every October: multi-factor authentication is on for every account, laptops are encrypted and updated, backups restore, and former staff accounts are disabled. Firms of this size are exempt from the penetration testing and six-monthly vulnerability assessments in § 314.4(d)(2), but Defender for Business reports missing updates and known weaknesses on each laptop continuously, and the IT provider reviews that report every month.

## 7. Staff training and access

- Every staff member completes security training at hire and before each filing season, covering phishing, the IRS's warnings on scams aimed at tax professionals, the risks found in the October review, and this plan. Each person signs and dates a record of the training.
- Seasonal preparers sign a confidentiality agreement and the code of conduct before they receive access.
- Access is removed at the end of a person's last shift, or at once when someone is let go. The office manager starts the checklist; the owner disables tax software and portal accounts and the IT provider disables Microsoft 365. Seasonal accounts are disabled after the April and October deadlines and re-enabled only when the person returns.
- The owner keeps current on threats through IRS e-News for Tax Professionals and the IRS Security Summit alerts.

## 8. Service providers

| Provider | Service | How it is checked |
| --- | --- | --- |
| Tax software vendor | Tax preparation, e-file and client portal | Security terms in the license agreement; multi-factor authentication enforced; reviewed every October |
| Microsoft | Microsoft 365 email, storage and device management | Microsoft's Data Protection Addendum commits it to safeguards; published security and compliance reports; reviewed every October |
| Outside IT provider | Device and Microsoft 365 administration | Contract requires safeguards, confidentiality, same-day alert reporting and security-trained staff; staff qualifications and ongoing training confirmed at selection and each October; access reviewed each January and October |
| Cloud backup service | Daily backup of Microsoft 365 | Chosen and managed by the IT provider; its contract requires safeguards; encryption confirmed; reviewed every October |
| Shredding service | On-site shredding | Bonded; contract requires confidentiality and secure destruction; certificate of destruction for each pickup; reviewed every October |

## 9. Responding to a security incident

Firms of this size are exempt from the written incident response plan in § 314.4(h), but the IRS urges tax professionals to know these steps before they are needed. The owner leads the response.

1. **Contain:** disconnect affected devices from the network, change passwords from a clean device, sign out all active sessions, record and then remove any sign-in methods, app permissions or mail-forwarding rules the firm did not set up, and call the IT provider. Do not wipe anything until the cause is known.
2. **Report to the IRS** through the local IRS Stakeholder Liaison, no later than the next business day after the incident is confirmed, so the IRS can protect clients' accounts from fraudulent returns. Also contact the local FBI office, and the Secret Service if directed, and file a report with the local police.
3. **Report to the states** where the firm prepares returns, using the contacts listed by the Federation of Tax Administrators, and the state attorneys general where state law requires it.
4. **Tell the insurer** before hiring outside response firms, since the policy may require its approved vendors.
5. **Notify the FTC** if unencrypted information about 500 or more consumers was acquired without authorization: as soon as possible, and no later than 30 days after discovery, through the FTC's online form. Under § 314.2(m), unauthorized access to unencrypted information counts as acquisition unless the firm has reliable evidence that the information was not, or could not reasonably have been, acquired. Encrypted information counts as unencrypted if the key was also accessed. This applies to firms of every size.
6. **Notify affected clients** under state breach notification laws, as advised by counsel.
7. **Learn:** record what happened and what was done, fix the weakness, and update this plan.

## 10. Employee code of conduct

- Use client information only to serve that client. Never discuss it outside the firm.
- Never share passwords or approve a sign-in prompt you did not start.
- Verify any request to change a client's bank details or address by calling the number on file, not one in the message.
- Keep paper files in locked cabinets when you step away, and lock your screen.
- Report a lost device, suspicious email or possible mistake to the owner at once. Reporting early is never held against you.

## 11. FTC Safeguards Rule checklist

| 16 CFR | Requirement | Status for this firm | Section |
| --- | --- | --- | --- |
| § 314.4(a) | Qualified Individual | Required; in place | 2 |
| § 314.4(b) | Risk assessment | Required; (b)(1) written criteria exempt; done anyway in short form | 3 |
| § 314.4(c) | Safeguards: access, inventory, encryption, software, MFA, disposal, change management, monitoring | Required; in place | 4, 5 |
| § 314.4(d) | Testing and monitoring | (d)(1) required; (d)(2) exempt; continuous laptop scanning in place | 6 |
| § 314.4(e) | Training and qualified security personnel | Required; in place | 2, 7, 8 |
| § 314.4(f) | Overseeing service providers | Required; in place | 8 |
| § 314.4(g) | Adjusting the program | Required; in place | 3, 12 |
| § 314.4(h) | Written incident response plan | Exempt; short plan kept anyway | 9 |
| § 314.4(i) | Annual written report to the board | Exempt under § 314.6 (fewer than 5,000 consumers) | 12 |
| § 314.4(j) | Notifying the FTC of a notification event | Required for every firm | 9 |

The exemptions come from § 314.6, which applies to financial institutions that maintain customer information about fewer than 5,000 consumers. Under § 314.2, a tax preparation service that completes income tax returns is a financial institution. Sources: 16 CFR Part 314 (eCFR, checked November 2026); IRS Publication 5708 (Rev. 8-2024); IRS Publication 4557 (Rev. 6-2024); IRS Publication 1345 (Rev. 10-2026); Form W-12 (Rev. October 2026), line 11; IRS, Data theft information for tax professionals (irs.gov, checked November 2026). Sample by Johnson Technical Systems for a fictional company, November 2026. Not legal or tax advice, and not an audit; a real plan should be reviewed by counsel.

## 12. Review and implementation

The owner reviews this plan every October before filing season, after any security event, and after any major change, and records the review in the version history. Staff must follow this plan; breaking it can lead to loss of access and to dismissal. Each version takes effect on the effective date in Document control, once the owner approves it.

| Version | Date | Change |
| --- | --- | --- |
| 1.0 | October 2024 | First version |
| 1.1 | October 2025 | Moved client uploads to the portal; stopped accepting documents by email |
| 1.2 | October 2026 | Annual review; seasonal accounts now disabled after each deadline |

## Want a plan like this for your firm?

[See WISP packs](wisp.md){ .md-button .md-button--primary } [Book a 15-minute call](https://cal.com/lloyd-johnson){ .md-button }

<small>Documentation and preparation services only. Not legal or tax advice, and not an audit or an FTC or IRS approval.</small>
