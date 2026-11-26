---
title: Sample public security page for a fictional software company
description: "A public security page for a fictional seed-stage software company, with a claim check that ties every statement to a questionnaire answer."
---

# Sample public security page for Quorrel, Inc. (fictional)

> **A fictional company, a real method.** A public security page for Quorrel, Inc., the fictional seed-stage software company used in the sample security questionnaire. Every statement on the page is backed by a questionnaire answer or a policy, and the page says plainly what the company does not have yet.

[Download the PDF](downloads/JTS-Sample-Public-Security-Page.pdf){ .md-button .md-button--primary }

## About this sample

- Quorrel, Inc. is a fictional company. Its facts, dates and figures were invented for this sample. Domains use the reserved .example name.
- The page was written from scratch by Johnson Technical Systems, from the same facts as the sample security questionnaire, so the two documents agree with each other.
- A public security page makes no framework claims, so this sample cites no standards. Its only source is the sample questionnaire, and the claim check table shows which answer backs each statement.
- The page text is what a visitor would read on the company's website. The claim check and reviewer notes are working papers that go to the client, not onto the website.

## Security at Quorrel

Last updated: November 2026

Quorrel Intake reads the vendor contracts you upload and pulls out their key terms. This page explains how we protect those contracts, who can see them, and what we have not yet put in place. If you need more detail for a security review, write to `security@quorrel.example`.

### Your data

- **What we hold:** the contracts you upload, the terms extracted from them, and your users' names, work email addresses and roles. We do not hold payment card details; billing runs through our payment provider.
- **Where it is stored:** in Amazon Web Services (AWS) in Northern Virginia, across multiple availability zones. Encrypted backup copies are kept in AWS in Oregon.
- **Who can see it:** three engineers have access to production systems, for operations and incident response. Our customer success staff can view your documents only after you grant support access in the app, and every view is logged.
- **Separation:** each customer's data is kept separate from every other customer's, and automated tests that try to read across customers run on every build.
- **Deletion:** documents you delete are removed from our systems within 30 days, and backup copies expire no more than 35 days after that. When your contract ends, we delete your data within 30 days and confirm in writing on request.

### How we use AI

- To extract terms, the text of each uploaded contract is sent to one third-party large language model provider, under a commercial agreement. The provider is named on our subprocessor list.
- Your data is not used to train AI models, by us or by the provider. The agreement prohibits it.
- The provider may keep the text we send, and the results, for up to 30 days for abuse monitoring. After that they are deleted.
- Every extracted term is labelled as AI-generated and links to its source text, so that you can check it.

### How we protect it

- **Encryption:** data is encrypted at rest with AES-256 and in transit with TLS 1.2 or higher.
- **Sign-in:** every staff account requires multi-factor authentication, using security keys or an authenticator app. Text-message codes are not allowed.
- **Devices:** only company laptops can reach production systems. They are encrypted and centrally managed.
- **Changes:** every code change is reviewed by a second engineer and must pass automated tests before release.
- **Monitoring:** security alerts go to an on-call engineer, and critical alerts are answered around the clock.
- **Testing:** an independent firm tests our application and cloud configuration every year. The September 2026 test found no critical or high issues. Two medium findings were fixed in October 2026 and retested by the firm.

### If something goes wrong

We have a written incident response plan and practised it in October 2026. If a security incident affects your data, we will notify your account's admin contacts without undue delay, and no later than 72 hours after we confirm it. As of November 2026, we have had no security incidents affecting customer data since the company was founded in 2024.

### Availability and backups

The service runs across multiple availability zones. The database is backed up continuously, with recovery to any point in the last 35 days, and we restored it from backup in a test in August 2026. We aim for 99.9% monthly uptime and publish a status page. That figure is a target, not a contractual commitment, unless it is written into your agreement.

### What we do not have yet

- **A SOC 2 report.** Readiness work is in progress, and a Type I examination is planned for Q2 2027. We do not hold ISO 27001 certification.
- **Single sign-on (SAML) and admin-enforced multi-factor authentication for your users.** Planned for Q1 2027. Today your users sign in with a password and optional authenticator-app MFA, or with Google.
- **A dedicated endpoint detection and response tool on our laptops.** Planned for Q1 2027. Today the laptops rely on the operating system's built-in protection.
- **A tested failover to a second region.** Planned for Q2 2027. Today we have tested restoring the database, not moving the whole service.

### Subprocessors

The companies that process customer data for us are listed at `quorrel.example/subprocessors`. Customers who subscribe to that page are told 30 days before a new subprocessor is added.

### Documents for your security review

Under a non-disclosure agreement we can share our completed security questionnaire, our security policies, the penetration test summary letter, our data processing agreement and our certificate of cyber insurance. Write to `security@quorrel.example`.

## Claim check

Each statement on the page, the questionnaire answer or policy that backs it, and the evidence behind that answer. A statement with nothing to back it does not go on the page.

| Statement on the page | Backed by | Evidence |
| --- | --- | --- |
| Data is stored in AWS in Northern Virginia, with encrypted backups in Oregon | Q2, Q46 | Architecture and data-flow diagram; backup configuration |
| Three engineers have production access; support staff see documents only after the customer grants access | Q3, Q16; Access Control Policy 4.4 | Access list; support-access log |
| Each customer's data is kept separate and tested on every build | Q23 | Design note; cross-tenant test results |
| Deleted within 30 days; backups expire within a further 35 days | Q24 | Data Retention Policy; deletion job logs |
| Contract text goes to one LLM provider; not used for training; kept up to 30 days | Q26, Q27, Q28; AI Use Policy 6 | Provider agreement clauses; subprocessor list |
| Encrypted at rest with AES-256 and in transit with TLS 1.2 or higher | Q20, Q21 | Encryption settings; external scan result |
| Multi-factor authentication on every staff account, without text-message codes | Q15; Access Control Policy 4.2 | Enforcement settings |
| Only company laptops reach production; they are encrypted and centrally managed | Q35, Q20 | MDM compliance report |
| Every code change is reviewed and tested | Q37 | Branch protection settings; sample pull requests |
| Written incident response plan, practised in October 2026 | Q43 | Incident Response Plan; tabletop exercise report |
| Alerts go to an on-call engineer; critical alerts answered around the clock | Q32 | Alert routing; on-call schedule |
| Independent penetration test in September 2026; no critical or high findings; two medium findings fixed and retested | Q34 | Penetration test summary letter |
| Notification within 72 hours of confirming an incident affecting customer data | Q44 | Data processing agreement; Incident Response Plan |
| No incidents affecting customer data since founding | Q45 | Written confirmation from the CEO and CTO |
| Database restore tested in August 2026; region failover not yet tested | Q47 | Restore test record |
| 99.9% monthly uptime is a target, not a contractual commitment | Q48 | Status page history |
| No SOC 2 report yet; Type I examination planned for Q2 2027 | Q4 | Readiness timeline |
| Single sign-on for customers, laptop EDR and failover test are planned, with dates | Q19, Q35, Q47 | Roadmap entries |
| Subprocessor list is public, with 30 days' notice of additions | Q42 | Public subprocessor page |

## Reviewer notes

What changed between the company's first draft and this page. On real work, these notes go to the client with the draft.

| Section | What changed in review |
| --- | --- |
| Compliance | The marketing draft said "SOC 2 compliant". There is no SOC 2 report, so the page states the readiness status and the planned examination date. |
| Your data | The draft said "your data is never shared with third parties". Customer data is processed by AWS and by the LLM provider, so the page names both kinds of subprocessor and links to the list. |
| How we protect it | The draft said "bank-grade security" and "military-grade encryption". Neither phrase can be checked, so the page names the actual methods: AES-256 and TLS 1.2 or higher. |
| How we protect it | The draft said "a 24/7 security team". Quorrel has no dedicated security staff. The page says that alerts go to an on-call engineer and that critical alerts are answered around the clock. |
| Availability | The draft said "99.9% uptime guaranteed". The figure is a target unless it is written into a customer's agreement, and the page says so. |
| What we do not have yet | The draft had no such section. It was added so that a buyer's reviewer finds the gaps here first, with dates, and not later in a questionnaire. |

## Sources

- **Company facts:** Johnson Technical Systems, Sample security questionnaire for Quorrel, Inc. (fictional), version 1.0, November 2026. Question numbers in the claim check refer to that document.
- **Standards:** none cited. This page makes no framework claims.

## Want one like this for your company?

[See pricing](index.md#packages){ .md-button .md-button--primary } [Book a 15-minute call](https://cal.com/lloyd-johnson){ .md-button }

<small>Documentation and preparation services only. Not legal advice, an audit, or a SOC 2 report.</small>
