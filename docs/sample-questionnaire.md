---
title: Sample security questionnaire for a fictional seed-stage SaaS company
---

# Sample security questionnaire: Quorrel, Inc.

> **A fictional company, a real method.** 50 questions from a typical customer security review, answered for Quorrel, Inc., a fictional seed-stage software company. Each answer says plainly what is in place, what is partial and what is planned, lists the evidence behind it, and points to the related SOC 2 and NIST CSF 2.0 references.

[Download the spreadsheet (.xlsx)](downloads/JTS-Sample-Security-Questionnaire.xlsx){ .md-button .md-button--primary } [Download the PDF](downloads/JTS-Sample-Security-Questionnaire.pdf){ .md-button }

## About this sample

- Quorrel, Inc. is a fictional company. Its facts, dates and figures were invented for this sample. Domains use the reserved .example name.
- The questions were written by Johnson Technical Systems in the style of common customer security questionnaires. They are not copied from SIG, CAIQ or any other licensed questionnaire.
- The SOC 2 and NIST CSF references show where each topic sits in each framework, to help a reviewer find the related criteria. They are not an auditor's opinion that a control meets the criteria. This is not a SOC 2 report.
- Every criterion and subcategory ID was checked against the source documents listed below in November 2026.

## Company profile

This is the intake summary the answers are written from.

| Item | Detail |
| --- | --- |
| **Company** | Quorrel, Inc. (fictional). Delaware corporation, founded 2024, seed stage. |
| **Product** | Quorrel Intake: a web app that reads vendor contracts uploaded by procurement teams and pulls out key terms such as renewal dates, liability caps and data-protection clauses, using a third-party large language model (LLM) API. |
| **Team** | 11 employees, all in the United States and fully remote: 7 engineering, 2 customer success, the CEO and an operations lead. No contractors with access to customer data. |
| **Infrastructure** | AWS us-east-1 (containers on ECS Fargate, PostgreSQL on RDS, S3, KMS), Cloudflare for DNS and web application firewall, GitHub, Terraform. |
| **Workforce tools** | Google Workspace (email and identity provider), Slack, Linear, 1Password, Datadog, a mobile device management (MDM) tool for company laptops, a SOC 2 readiness platform. |
| **Customer data** | Uploaded contracts and the terms extracted from them, which can include business contact details that appear in contracts; user account details (name, work email, role). No payment card data (billing runs through Stripe), no health information, no consumer data. |
| **Compliance status** | SOC 2 readiness in progress; Type I examination planned for Q2 2027. Annual third-party penetration test, last completed September 2026. |

## Status key

| Status | Meaning | Count in this sample |
| --- | --- | --- |
| Yes | In place today. | 39 |
| Partial | Partly in place; the answer says what is and is not. | 3 |
| Planned | Not in place yet; the answer gives a target date. | 1 |
| No | Not in place and not planned. | 0 |
| N/A | Does not apply, with the reason. | 1 |
| Info | A descriptive question with no yes or no answer. | 6 |

## Company and scope

### 1. Describe your product and the customer data it processes

Quorrel Intake reads vendor contracts that customers upload (PDF or Word) and extracts key terms for review. We process the uploaded documents, the extracted terms, and user account details (name, work email, role). Contracts can contain business contact details such as names, email addresses and signatures. We do not process payment card data (billing runs through Stripe, and card details never reach our systems), health information or consumer data.

**Status:** Info · **Evidence available:** System description; data inventory · **SOC 2:** C1.1 · **NIST CSF 2.0:** ID.AM-07

### 2. Where is customer data stored and processed?

In AWS us-east-1 (Northern Virginia), across multiple availability zones. Encrypted backup copies are kept in AWS us-west-2 (Oregon). Our LLM API provider processes extraction requests in the United States under our agreement. All staff are based in the United States.

**Status:** Info · **Evidence available:** Architecture and data-flow diagram; subprocessor list · **SOC 2:** CC6.7 · **NIST CSF 2.0:** ID.AM-03

### 3. How many people can access customer data, and how?

Three engineers have production access for operations and incident response. Our two customer success staff can view a customer's documents only through the in-app support view, only after that customer grants support access, and every view is logged. No contractors have access.

**Status:** Info · **Evidence available:** Access list; support-access log sample · **SOC 2:** CC6.3 · **NIST CSF 2.0:** PR.AA-05

### 4. Do you have a SOC 2 report or ISO 27001 certificate?

Not yet. SOC 2 readiness work is in progress, and a Type I examination is planned for Q2 2027, followed by a Type II observation period. We do not hold ISO 27001 certification. Until then we can share this questionnaire, our policies and our penetration test summary under NDA.

**Status:** Planned · **Evidence available:** Readiness timeline; auditor engagement letter when signed · **SOC 2:** None · **NIST CSF 2.0:** None

## Governance and policies

### 5. Do you have documented information security policies approved by management?

Yes. We maintain 12 policies, including Information Security, Acceptable Use, Access Control, Data Classification, Vulnerability Management, Incident Response, Business Continuity and Vendor Management. The CEO approved them in August 2026. They are reviewed at least once a year, and every employee acknowledges them at hire and annually.

**Status:** Yes · **Evidence available:** Policy set; approval record; acknowledgement records · **SOC 2:** CC5.3, CC2.2 · **NIST CSF 2.0:** GV.PO-01

### 6. Who is responsible for information security?

Our CTO is accountable for the security program and reports to the CEO. The board receives a security update every quarter. We do not have dedicated security staff; we use an independent penetration testing firm and a SOC 2 readiness platform to support the program.

**Status:** Yes · **Evidence available:** Org chart; board update agenda · **SOC 2:** CC1.2, CC1.3 · **NIST CSF 2.0:** GV.RR-01, GV.RR-02

### 7. Do you perform security risk assessments?

Yes, at least annually. The first formal assessment was completed in September 2026. Risks are tracked in a risk register with an owner and a treatment plan for each, and the CTO and CEO review the register every quarter.

**Status:** Yes · **Evidence available:** Risk assessment report; risk register · **SOC 2:** CC3.2 · **NIST CSF 2.0:** ID.RA-05, ID.RA-06

### 8. Do you maintain an inventory of systems and assets?

Yes. Company laptops are tracked in our MDM tool, cloud infrastructure is defined in Terraform and tracked through AWS, and SaaS tools are listed in a maintained inventory with an owner for each.

**Status:** Yes · **Evidence available:** MDM device list; Terraform repository; SaaS inventory · **SOC 2:** CC6.1 · **NIST CSF 2.0:** ID.AM-01, ID.AM-02

### 9. Do you classify data?

Yes. Our Data Classification Policy defines three levels: Public, Internal and Confidential. All customer data is classified as Confidential, which sets the handling, access and deletion rules that apply to it.

**Status:** Yes · **Evidence available:** Data Classification Policy · **SOC 2:** C1.1 · **NIST CSF 2.0:** ID.AM-05

## People

### 10. Do you run background checks on personnel?

Yes. All employees are background checked before their start date, where local law allows. Checks cover identity, employment history and criminal records. We have no contractors with access to customer data.

**Status:** Yes · **Evidence available:** Background check records (summary only) · **SOC 2:** CC1.4 · **NIST CSF 2.0:** GV.RR-04

### 11. Do personnel sign confidentiality agreements?

Yes. Every employee signs a confidentiality and invention assignment agreement before starting.

**Status:** Yes · **Evidence available:** Signed agreement template; signature records · **SOC 2:** CC1.1 · **NIST CSF 2.0:** GV.RR-04

### 12. Do you provide security awareness training?

Yes, at onboarding and annually after that, with completion tracked. All staff completed the 2026 training. Phishing simulations are planned to start in Q1 2027.

**Status:** Yes · **Evidence available:** Training completion report · **SOC 2:** CC2.2 · **NIST CSF 2.0:** PR.AT-01

### 13. How quickly is access removed when someone leaves?

Within 24 hours of the last working day, and on the same day for involuntary departures, following an offboarding checklist. Suspending the Google Workspace account removes access to every tool that signs in through it. GitHub and 1Password memberships are removed separately, as steps on the same checklist. Laptops are returned and wiped through MDM.

**Status:** Yes · **Evidence available:** Offboarding checklist; completed tickets · **SOC 2:** CC6.2, CC6.3 · **NIST CSF 2.0:** PR.AA-05

## Access control

### 14. Do you use single sign-on (SSO) for internal systems?

Yes. Google Workspace is our identity provider. AWS access goes through AWS IAM Identity Center, federated to Google Workspace, and Slack, Linear and Datadog use Google sign-in. GitHub and 1Password do not use SSO; each uses individual accounts with two-factor authentication enforced for the whole organization.

**Status:** Yes · **Evidence available:** Identity provider configuration screenshots · **SOC 2:** CC6.1 · **NIST CSF 2.0:** PR.AA-01

### 15. Is multi-factor authentication (MFA) enforced for all workforce accounts?

Yes. Google Workspace 2-Step Verification is enforced for every account, using security keys or an authenticator app; text-message codes are not allowed. GitHub and 1Password require two-factor authentication for every member, and AWS access requires a Google sign-in with MFA.

**Status:** Yes · **Evidence available:** Google Workspace and GitHub enforcement settings · **SOC 2:** CC6.1 · **NIST CSF 2.0:** PR.AA-03

### 16. How is production access limited?

Only three engineers have production access, through role-based permission sets in AWS IAM Identity Center. Read-only access is the default; an administrator role is used only for changes and incidents, and all activity is logged in AWS CloudTrail. The database has no public endpoint. Engineers reach it only through AWS Systems Manager Session Manager port forwarding, so no inbound ports are open to the internet.

**Status:** Yes · **Evidence available:** Permission set list; CloudTrail sample · **SOC 2:** CC6.1, CC6.3 · **NIST CSF 2.0:** PR.AA-05

### 17. Do you review user access periodically?

Yes, every quarter for AWS, GitHub, Google Workspace administrators and the support tool. The first review was completed in October 2026, and reviews are recorded in our SOC 2 readiness platform.

**Status:** Yes · **Evidence available:** Access review records · **SOC 2:** CC6.3 · **NIST CSF 2.0:** PR.AA-05

### 18. How do you manage passwords and secrets?

Workforce accounts use SSO, with a 12-character minimum password set in Google Workspace. Shared team credentials are kept in 1Password. Application secrets are stored in AWS Secrets Manager, never in code, and GitHub secret scanning is turned on for every repository.

**Status:** Yes · **Evidence available:** Password policy setting; Secrets Manager inventory; secret scanning setting · **SOC 2:** CC6.1 · **NIST CSF 2.0:** PR.AA-01

### 19. How do your customers' users sign in to the product?

With email and password plus optional authenticator-app MFA, or with Sign in with Google. SAML single sign-on and admin-enforced MFA are planned for Q1 2027.

**Status:** Partial · **Evidence available:** Product authentication settings; roadmap entry · **SOC 2:** CC6.1 · **NIST CSF 2.0:** PR.AA-03

## Data protection

### 20. Is customer data encrypted at rest?

Yes. The database (RDS) and file storage (S3) are encrypted with AES-256 using keys managed in AWS Key Management Service (KMS). Company laptops use full-disk encryption (FileVault), enforced by MDM.

**Status:** Yes · **Evidence available:** RDS and S3 encryption settings; MDM compliance report · **SOC 2:** CC6.1 · **NIST CSF 2.0:** PR.DS-01

### 21. Is customer data encrypted in transit?

Yes. All public endpoints require TLS 1.2 or higher, HTTP requests are redirected to HTTPS, and HSTS is enabled. Connections from the application to the database also use TLS.

**Status:** Yes · **Evidence available:** TLS configuration; external scan result · **SOC 2:** CC6.7 · **NIST CSF 2.0:** PR.DS-02

### 22. How are encryption keys managed?

Keys are created and stored in AWS KMS, with automatic annual rotation turned on. Only the application's service roles can use them. We do not currently offer customer-managed keys.

**Status:** Yes · **Evidence available:** KMS key policy and rotation setting · **SOC 2:** CC6.1 · **NIST CSF 2.0:** PR.DS-01

### 23. How is each customer's data kept separate from other customers'?

Quorrel is multi-tenant. Every record carries a tenant ID, and separation is enforced in the data-access layer and by PostgreSQL row-level security. Automated tests that try to read across tenants run on every build. Files in S3 are stored under per-tenant paths and reached only through the application.

**Status:** Yes · **Evidence available:** Design note; cross-tenant test results · **SOC 2:** CC6.1 · **NIST CSF 2.0:** PR.AA-05

### 24. How do you retain and delete customer data?

Customers control their data. Documents deleted in the app are removed from production, along with the terms extracted from them, within 30 days. Backup copies expire no more than 35 days after that. When a contract ends, all of that customer's data is deleted within 30 days, and we confirm deletion in writing on request.

**Status:** Yes · **Evidence available:** Data Retention Policy; deletion job logs · **SOC 2:** C1.2 · **NIST CSF 2.0:** None

### 25. Do you keep customer data out of development and test environments?

Yes. Development and staging environments use synthetic test data only. Customer data stays in production.

**Status:** Yes · **Evidence available:** Environment data policy; staging seed data · **SOC 2:** C1.1 · **NIST CSF 2.0:** None

## AI and LLM use

### 26. Do you use AI or LLMs to process customer data?

Yes. To extract terms, the text of an uploaded document is sent to a third-party LLM API under a commercial agreement. We send only the document text needed for the extraction. The provider is named on our subprocessor list.

**Status:** Info · **Evidence available:** Subprocessor list; provider agreement (summary on request) · **SOC 2:** CC9.2 · **NIST CSF 2.0:** GV.SC-05

### 27. Is customer data used to train AI models?

No. We do not train or fine-tune models on customer data, and our agreement with the LLM provider prohibits it from using our API inputs and outputs to train its models. Any future change would require the customer's opt-in.

**Status:** Yes · **Evidence available:** Provider agreement clause; AI Use Policy · **SOC 2:** C1.1 · **NIST CSF 2.0:** GV.SC-05

### 28. How long does your LLM provider retain the data you send?

Under our agreement, the provider may retain API inputs and outputs for up to 30 days for abuse monitoring, after which they are deleted. It does not use them for any other purpose.

**Status:** Info · **Evidence available:** Provider agreement clause · **SOC 2:** CC9.2 · **NIST CSF 2.0:** GV.SC-05

### 29. How do you manage AI-specific risks such as prompt injection and incorrect output?

Document text is treated as untrusted data, never as instructions. Each request contains a single customer's document, and the model has no tools and no access to other data. Outputs are checked against a fixed schema. In the product, every extracted term links to its source text and is labelled AI-generated for the user to review. Before any model or prompt change goes live, we test extraction accuracy against a fixed test set.

**Status:** Yes · **Evidence available:** AI risk entry in risk register; evaluation results · **SOC 2:** CC3.2, CC8.1 · **NIST CSF 2.0:** ID.RA-03

## Infrastructure and operations

### 30. How is your network protected?

The application and database run in private subnets of an AWS VPC; only the load balancer is public. Security groups deny traffic by default. Cloudflare's web application firewall and DDoS protection sit in front of the application.

**Status:** Yes · **Evidence available:** Network diagram; security group rules; WAF settings · **SOC 2:** CC6.6 · **NIST CSF 2.0:** PR.IR-01

### 31. What do you log, and for how long?

AWS CloudTrail is on in all regions and writes to a restricted S3 bucket, kept for one year. Application and access logs go to Datadog and are kept for 90 days. Google Workspace and GitHub audit logs are kept for the period each vendor provides.

**Status:** Yes · **Evidence available:** CloudTrail configuration; log retention settings · **SOC 2:** CC7.2 · **NIST CSF 2.0:** PR.PS-04

### 32. How do you detect and respond to security alerts?

AWS GuardDuty and Datadog monitors send alerts to the on-call engineer. The three engineers with production access share an on-call rotation, and critical alerts are answered around the clock.

**Status:** Yes · **Evidence available:** GuardDuty settings; alert routing; on-call schedule · **SOC 2:** CC7.2 · **NIST CSF 2.0:** DE.CM-01, DE.CM-09

### 33. How do you manage vulnerabilities?

Dependabot and container image scanning run on every build. Our fix targets are 7 days for critical, 30 days for high and 90 days for medium findings, tracked in Linear.

**Status:** Yes · **Evidence available:** Vulnerability Management Policy; scan results; ticket history · **SOC 2:** CC7.1 · **NIST CSF 2.0:** ID.RA-01

### 34. Do you perform penetration testing?

Yes, every year, by an independent firm. The September 2026 test covered the web application, the API and an AWS configuration review. The test found no critical or high issues. The two medium findings were fixed in October 2026 and retested by the firm. A summary letter is available under NDA.

**Status:** Yes · **Evidence available:** Pen test summary letter; remediation tickets · **SOC 2:** CC4.1 · **NIST CSF 2.0:** ID.IM-02

### 35. How are company laptops secured?

Only company-issued laptops can access production. MDM enforces full-disk encryption, a screen lock after 5 minutes, the built-in firewall and operating system updates within 14 days. Laptops rely on the operating system's built-in malware protection; a dedicated endpoint detection and response (EDR) tool is planned for Q1 2027.

**Status:** Partial · **Evidence available:** MDM compliance report · **SOC 2:** CC6.8 · **NIST CSF 2.0:** PR.PS-01, DE.CM-09

### 36. What physical security controls protect your systems?

We have no offices or servers of our own. All staff work remotely, and our systems run in AWS data centers. We rely on AWS physical security controls, which are covered in AWS's SOC 2 report; we review that report every year.

**Status:** N/A · **Evidence available:** AWS SOC 2 report review record · **SOC 2:** CC6.4 · **NIST CSF 2.0:** PR.AA-06

## Secure development and change management

### 37. Describe your secure development process

All code lives in GitHub. The main branch is protected: every change needs a pull request, an approving review from someone other than the author, and passing automated tests and static analysis. Direct pushes to main are blocked.

**Status:** Yes · **Evidence available:** Branch protection settings; sample pull requests · **SOC 2:** CC8.1 · **NIST CSF 2.0:** PR.PS-06

### 38. How are infrastructure changes controlled?

Infrastructure is defined in Terraform, kept in GitHub and reviewed like application code, then applied through the deployment pipeline. Manual changes in the AWS console are allowed only in emergencies, and each one is logged and reviewed afterwards.

**Status:** Yes · **Evidence available:** Terraform repository; pipeline logs; emergency change log · **SOC 2:** CC8.1 · **NIST CSF 2.0:** ID.RA-07, PR.PS-01

### 39. Are development, staging and production separated?

Yes. Each runs in its own AWS account, and production deploys happen only through the pipeline.

**Status:** Yes · **Evidence available:** AWS account structure · **SOC 2:** CC8.1 · **NIST CSF 2.0:** PR.IR-01

### 40. Do engineers receive secure coding training?

Yes. Engineers complete secure coding training based on the OWASP Top 10 at onboarding and every year after that.

**Status:** Yes · **Evidence available:** Training completion records · **SOC 2:** CC1.4 · **NIST CSF 2.0:** PR.AT-02

## Vendors

### 41. How do you manage vendor and subprocessor risk?

We keep an inventory of vendors that handle customer data. Before onboarding, and every year for critical vendors, we review their security reports (such as SOC 2) and sign a data processing agreement where needed.

**Status:** Yes · **Evidence available:** Vendor inventory; vendor review records · **SOC 2:** CC9.2 · **NIST CSF 2.0:** GV.SC-04, GV.SC-06

### 42. Do you publish a subprocessor list and give notice of changes?

Yes. The list is published at quorrel.example/subprocessors. Customers who subscribe get 30 days' notice before a new subprocessor is added.

**Status:** Yes · **Evidence available:** Public subprocessor page · **SOC 2:** CC2.3 · **NIST CSF 2.0:** GV.SC-04

## Incident response

### 43. Do you have a documented incident response plan, and is it tested?

Yes. The written plan covers roles, severity levels, contacts, evidence handling and customer notification, and it is reviewed every year. We ran a tabletop exercise in October 2026 using a leaked AWS access key scenario and updated the plan afterwards.

**Status:** Yes · **Evidence available:** Incident Response Plan; tabletop exercise report · **SOC 2:** CC7.3, CC7.4 · **NIST CSF 2.0:** RS.MA-01, ID.IM-02

### 44. How and when will you notify us of a security incident?

We notify affected customers without undue delay, and no later than 72 hours after confirming a security incident that affects their data, by email to the account's admin contacts. This commitment is in our data processing agreement.

**Status:** Yes · **Evidence available:** Data processing agreement; Incident Response Plan · **SOC 2:** CC7.4, CC2.3 · **NIST CSF 2.0:** RS.CO-02

### 45. Have you had a security incident or data breach in the past three years?

No. We have had no security incidents affecting customer data since the company was founded in 2024.

**Status:** Info · **Evidence available:** Written confirmation from the CEO and CTO · **SOC 2:** CC7.3 · **NIST CSF 2.0:** None

## Business continuity

### 46. How is customer data backed up?

The database uses automated backups with point-in-time recovery, kept for 35 days. S3 versioning is on. An encrypted copy of the daily backups is kept in a second AWS region (us-west-2).

**Status:** Yes · **Evidence available:** Backup configuration screenshots · **SOC 2:** A1.2 · **NIST CSF 2.0:** PR.DS-11

### 47. Do you have a business continuity and disaster recovery plan, and is it tested?

Partly. The written plan sets a recovery time objective (RTO) of 8 hours and a recovery point objective (RPO) of 1 hour. In August 2026 we restored the production database from backup to a new instance in 47 minutes. A full failover to the second region has not been tested yet; that test is planned for Q2 2027.

**Status:** Partial · **Evidence available:** Business Continuity Plan; restore test record · **SOC 2:** A1.3, CC9.1 · **NIST CSF 2.0:** ID.IM-04, PR.DS-11

### 48. How do you maintain availability?

The database runs in multiple availability zones and the application runs across two. We publish a status page and target 99.9% monthly uptime. That is a target, not a contractual service level, unless it is written into your agreement.

**Status:** Yes · **Evidence available:** Architecture diagram; status page history · **SOC 2:** A1.1, A1.2 · **NIST CSF 2.0:** PR.IR-03

## Privacy and legal

### 49. Will you sign a data processing agreement (DPA)?

Yes. We have a standard DPA and will review a customer's own DPA. We host data only in the United States. If your data includes personal data from the EU or UK, tell us before you upload it so that transfer terms can be agreed first.

**Status:** Yes · **Evidence available:** Standard DPA · **SOC 2:** CC2.3 · **NIST CSF 2.0:** GV.OC-03

### 50. Do you carry cyber insurance?

Yes. We carry cyber liability insurance, and a certificate of insurance is available on request.

**Status:** Yes · **Evidence available:** Certificate of insurance · **SOC 2:** CC9.1 · **NIST CSF 2.0:** None

## Reviewer notes

Answers that changed during review. On real work, these go to the client with the draft so nothing is overstated.

- **Q4:** The founder's draft answer called the company "SOC 2 compliant". There is no SOC 2 report yet, so the answer was changed to state the readiness status and the planned examination date.
- **Q13:** The intake form said that suspending the Google account removes all access. GitHub and 1Password use separate accounts, so the answer now lists them as separate offboarding steps.
- **Q28:** The provider's retention period was confirmed against the signed agreement, not the provider's marketing page.
- **Q35:** The intake form said "antivirus on all laptops". The founder confirmed there is no separate antivirus or EDR tool, only built-in protection, so the status was changed from Yes to Partial, with a date for EDR.
- **Q45:** The no-incidents answer was confirmed in writing by the CEO and CTO before it was included.
- **Q47:** The first draft said disaster recovery was tested. Only a database restore was tested, so the answer now says exactly that and gives a date for the region failover test.

## Sources

- **SOC 2 references:** AICPA, TSP Section 100, 2017 Trust Services Criteria for Security, Availability, Processing Integrity, Confidentiality, and Privacy (edition including March 2020 updates). The AICPA's 2022 revision updated the points of focus but did not change the criteria.
- **NIST CSF references:** NIST CSWP 29, The NIST Cybersecurity Framework (CSF) 2.0, February 26, 2024.

## Want one like this for your company?

[See questionnaire pricing](questionnaires.md){ .md-button .md-button--primary } [Book a 15-minute call](https://cal.com/lloyd-johnson){ .md-button }

<small>Documentation and preparation services only. Not legal advice, an audit, or a SOC 2 report.</small>
