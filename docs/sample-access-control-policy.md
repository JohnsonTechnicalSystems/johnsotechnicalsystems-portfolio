---
title: Sample access control policy for a fictional software company
description: "One policy from a starter policy pack, written for a fictional seed-stage software company, with the evidence each requirement produces."
---

# Sample access control policy for Quorrel, Inc. (fictional)

> **A fictional company, a real method.** One policy from a starter policy pack, written for Quorrel, Inc., the fictional seed-stage software company used in the sample security questionnaire. Each requirement names who does what and the record it leaves behind.

[Download the PDF](downloads/JTS-Sample-Access-Control-Policy.pdf){ .md-button .md-button--primary }

## About this sample

- Quorrel, Inc. is a fictional company. Its setup matches the sample security questionnaire, so the two documents agree with each other.
- This is one policy of the 10 to 16 in a starter policy pack. A client's pack is written the same way, from the client's own intake answers.
- The policy was written from scratch by Johnson Technical Systems. It is not copied from any template or licensed standard.
- The SOC 2 and NIST CSF references show where each topic sits in each framework. They are not an auditor's opinion that a control meets the criteria. This is not a SOC 2 report.
- Every criterion and subcategory identifier was checked against the source documents named in section 6 in November 2026.

## Document control

| Field | Value |
| --- | --- |
| Policy owner | Chief Technology Officer (CTO) |
| Approved by | Chief Executive Officer (CEO) |
| Version | 1.0 |
| Effective date | August 2026 |
| Classification | Internal |
| Next review | August 2027, or sooner after a major change |

## 1. Purpose

This policy sets out how Quorrel decides who can access its systems and data, how that access is granted, changed and removed, and how it is checked. Its aim is that each person has only the access their job needs, and that customer data is reachable only by the people and paths named here.

## 2. Scope

This policy applies to every Quorrel employee and to any future contractor ("workforce members"). It covers these systems:

- **Identity and workforce tools:** Google Workspace (the identity provider), Slack, Linear, Datadog, 1Password and the SOC 2 readiness platform
- **Engineering and production:** AWS (accessed through AWS IAM Identity Center), GitHub, Terraform, Cloudflare
- **The Quorrel Intake product:** internal administration and the in-app support view

How customers' own users sign in to the product is covered by the Secure Development Policy, not this one.

## 3. Roles and responsibilities

| Role | Responsibility under this policy |
| --- | --- |
| CEO | Approves this policy and any exception to it. Approves the CTO's own production access, so that no one approves their own. |
| CTO | Owns this policy. Approves production access. Runs the quarterly access reviews. |
| Operations lead | Runs the onboarding and offboarding checklists and keeps the records of both. |
| Managers | Request access for their team members and confirm during each review that it is still needed. |
| All workforce members | Use only their own accounts, protect their credentials, and report any suspected account compromise to the CTO at once. |

## 4. Policy requirements

### 4.1 Accounts and sign-in

- Every workforce member has one named account per system. Accounts are not shared.
- Google Workspace is the identity provider. Any tool that supports Google sign-in must use it.
- GitHub and 1Password use individual accounts, because they do not sign in through Google Workspace. Each is tracked as a separate step in the onboarding and offboarding checklists.
- A credential that a team must share, such as a vendor account with only one login, is kept in 1Password with a named owner. It is changed when anyone who could use it leaves.

### 4.2 Multi-factor authentication and passwords

- Multi-factor authentication is required on every workforce account. Google Workspace 2-Step Verification uses security keys or an authenticator app. Text-message codes are not allowed.
- GitHub and 1Password require two-factor authentication for every member of the organization.
- Google Workspace passwords must be at least 12 characters long.
- Application secrets are stored in AWS Secrets Manager, never in code. GitHub secret scanning stays turned on for every repository.

### 4.3 Granting access

- Access is requested through a Linear ticket that names the person, the system, the role needed and the reason.
- The person's manager approves the request. The system owner then grants the smallest role that does the job.
- New starters receive their standard access through the onboarding checklist. Access is granted only after their confidentiality agreement is signed.

### 4.4 Production and customer data

- Production access is limited to named engineers approved by the CTO. Three engineers have it today.
- Production access goes through role-based permission sets in AWS IAM Identity Center. Read-only is the default. The administrator role is used only for approved changes and incidents.
- All production activity is logged in AWS CloudTrail. The database has no public endpoint and is reached only through AWS Systems Manager Session Manager.
- Customer success staff may view a customer's documents only through the in-app support view, only after that customer grants support access, and every view is logged.

### 4.5 Changing and removing access

- When someone changes role, access they no longer need is removed within 5 business days.
- When someone leaves, all access is removed within 24 hours of their last working day, or on the same day for an involuntary departure. The offboarding checklist covers suspending the Google Workspace account, removing GitHub and 1Password membership, rotating any shared credentials they could use, and wiping their laptop through the mobile device management (MDM) tool.

### 4.6 Access reviews

- Every quarter, the CTO reviews access to AWS, GitHub, Google Workspace administrator roles and the support view, together with each person's manager.
- Every account must be confirmed as still needed. Any account that is not is removed within 5 business days.
- Reviews and removals are recorded in the SOC 2 readiness platform.

### 4.7 Exceptions

An exception to this policy needs a written request that gives the reason and the risk, and the CEO's approval. An exception lasts at most 90 days and is recorded in the risk register.

## 5. Evidence this policy produces

Each requirement leaves a record. These are the records an auditor or customer reviewer can ask to see.

| Requirement | Evidence | How often |
| --- | --- | --- |
| 4.1, 4.2 Accounts, MFA and passwords | Google Workspace 2-Step Verification and password settings; GitHub and 1Password two-factor enforcement settings; secret scanning setting | Captured each quarter |
| 4.3 Granting access | Linear access tickets with the manager's approval; completed onboarding checklists | Each request |
| 4.4 Production and customer data | List of AWS permission sets and their members; CloudTrail logs; support view access log | Ongoing; list captured each quarter |
| 4.5 Changing and removing access | Completed offboarding checklists with dates; MDM wipe records | Each departure |
| 4.6 Access reviews | Review records and removal tickets in the readiness platform | Quarterly |
| 4.7 Exceptions | Approved exception requests; risk register entries | Each exception |

## 6. Framework references

| Reference | What it covers | Sections |
| --- | --- | --- |
| SOC 2 CC5.3 | Control activities deployed through policies and procedures | Whole policy |
| SOC 2 CC6.1 | Logical access security over protected information assets | 4.1, 4.2, 4.4 |
| SOC 2 CC6.2 | Registering and authorizing users before access; removing credentials when no longer needed | 4.3, 4.5 |
| SOC 2 CC6.3 | Authorizing, changing and removing access by role, with least privilege and segregation of duties | 3, 4.3 to 4.6 |
| CSF PR.AA-01 | Identities and credentials for authorized users are managed | 4.1, 4.2 |
| CSF PR.AA-03 | Users, services and hardware are authenticated | 4.2 |
| CSF PR.AA-05 | Access permissions are defined in policy, managed, enforced and reviewed, with least privilege and separation of duties | 4.3 to 4.6 |
| CSF GV.PO-01 | Cybersecurity policy is established, communicated and enforced | 7 |

Sources: AICPA, 2017 Trust Services Criteria (With Revised Points of Focus – 2022); NIST CSWP 29, The NIST Cybersecurity Framework (CSF) 2.0, February 26, 2024. The descriptions above are summaries; see the source documents for the exact wording.

## 7. Enforcement and review

Breaking this policy can lead to loss of access and to disciplinary action. Every workforce member acknowledges this policy when hired and once a year after that. The CTO reviews the policy at least once a year and after any major change to systems or team, and the CEO approves each new version.

| Version | Date | Change | Approved by |
| --- | --- | --- | --- |
| 1.0 | August 2026 | First version | CEO |

## Want a policy pack like this for your company?

[See pricing](index.md#packages){ .md-button .md-button--primary } [Book a 15-minute call](https://cal.com/lloyd-johnson){ .md-button }

<small>Documentation and preparation services only. Not legal advice, an audit, or a SOC 2 report.</small>
