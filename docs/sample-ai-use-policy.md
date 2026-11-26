---
title: Sample AI use policy and AI tool inventory for a fictional software company
description: "An AI use policy and AI tool inventory for a fictional seed-stage software company, stating what is in place, partial and planned."
---

# Sample AI use policy and AI tool inventory for Quorrel, Inc. (fictional)

> **A fictional company, a real method.** An AI use policy and AI tool inventory for Quorrel, Inc., the fictional seed-stage software company used in the sample security questionnaire. The policy states which rules are in place today, which are partial and which are planned, and the inventory records what each AI tool may be used for and on what terms.

[Download the policy (PDF)](downloads/JTS-Sample-AI-Use-Policy.pdf){ .md-button .md-button--primary } [Download the inventory (.xlsx)](downloads/JTS-Sample-AI-Tool-Inventory.xlsx){ .md-button }

## About this sample

- Quorrel, Inc. is a fictional company. Its facts, dates and figures were invented for this sample, and they match the sample security questionnaire (questions 26 to 29) and the sample Access Control Policy, so the three documents agree with one another.
- The policy and inventory were written from scratch by Johnson Technical Systems. They are not copied from any template, standard or vendor document.
- Vendor products are described generically (for example, "AI coding assistant, business plan"). Real vendors change their terms, so a client's inventory names each product and plan and records the date its terms were checked.
- The NIST references show where each topic sits in each framework, to help a reviewer find the related text. They are not an assessment, and they do not claim conformity with either framework. ISO/IEC 42001 is not mapped in this sample.
- Every NIST AI RMF and NIST CSF identifier was checked against the source documents listed below in November 2026.

## Document control

| Field | Value |
| --- | --- |
| Policy owner | Chief Technology Officer (CTO) |
| Approved by | Chief Executive Officer (CEO) |
| Version | 1.1 |
| Effective date | November 2026 |
| Classification | Internal |
| Next review | May 2027, or sooner when an AI tool or model provider is added or changes its terms |

## 1. Purpose

This policy sets out how Quorrel uses artificial intelligence (AI) tools in its work and in its product. Its aim is that customer data reaches an AI tool only where this policy allows it, that every AI tool in use is known and approved, and that a person remains responsible for anything an AI tool produces.

## 2. Scope

This policy applies to every Quorrel employee and to any future contractor ("workforce members"). It covers:

- **AI tools used for work:** chat assistants, coding assistants and any other tool that generates or summarises content
- **AI features inside tools Quorrel already uses,** such as summaries in the team chat tool
- **AI in the product:** the third-party LLM API that Quorrel Intake uses to extract contract terms

How Quorrel's customers use AI in their own businesses is outside the scope of this policy.

## 3. Definitions

| Term | Meaning in this policy |
| --- | --- |
| AI tool | Software that generates text, code, images or summaries from a prompt, whether it is a separate product or a feature inside another tool. |
| Approved tool | An AI tool listed in the AI tool inventory (Annex A) with the status Approved, used through a company account. |
| Data classes | Public, Internal and Confidential, as defined in the Data Classification Policy. All customer data is Confidential. |

## 4. Roles and responsibilities

| Role | Responsibility under this policy |
| --- | --- |
| CEO | Approves this policy and any exception to it. Approves, with the CTO, any new model provider or any new use of customer data with AI. |
| CTO | Owns this policy and the AI tool inventory. Reviews and decides each request for a new AI tool. Reviews every inventory entry every six months. |
| Operations lead | Keeps the approval records and seat lists. Includes this policy in onboarding. |
| Managers | Request tools for their teams and make sure their teams follow section 5. |
| All workforce members | Use only approved tools, follow the data rules in section 5.2, check what AI produces before relying on it, and report problems under section 8. |

## 5. Rules for using AI tools at work

### 5.1 Approved tools and company accounts

- Only tools with the status Approved in the inventory may be used for work.
- Approved tools are used through a company account, with Google sign-in where the tool supports it. Personal AI accounts are not used for work.
- A tool that is not in the inventory is requested under section 7 before anyone uses it.

### 5.2 What data may go into an AI tool

| Data | Rule |
| --- | --- |
| Public | May be used in any approved tool. |
| Internal (for example source code, plans and internal documents) | May be used only in tools whose inventory entry allows Internal data. |
| Confidential (all customer data, including uploaded contracts and extracted terms) | May be processed only by a tool whose inventory entry allows Confidential data. Today that is one tool: the product's LLM API, reached only through the application. Customer data is never pasted into a chat assistant, a coding assistant or any other tool. |
| Passwords, keys and other secrets | Never entered into any AI tool. |
| Personal details of employees or job candidates | Not entered into an AI tool without the CTO's approval. |

### 5.3 Checking what AI produces

- The person who uses an AI tool's output is responsible for it, as if they had written it themselves.
- AI-assisted code follows the same path as all other code: a pull request, an approving review from someone other than the author, and passing automated tests and static analysis.
- Facts, figures and references produced by an AI tool are checked before they go into anything sent to a customer.
- AI tools are not used to make decisions about hiring, pay, performance or dismissal.

### 5.4 Customer communications

An AI tool may help draft a reply to a customer, provided no customer document or extracted term is entered into it and the sender reads and corrects the draft before sending.

### 5.5 Recording and transcribing meetings

AI note-takers and transcription tools are not approved. They are not added to any call with a customer or a prospect.

### 5.6 AI features inside existing tools

When a vendor adds an AI feature to a tool Quorrel already uses, the feature is treated as a new AI tool. Where the administrator settings allow, it stays switched off until it has been reviewed under section 7.

## 6. AI in the product

- Quorrel Intake sends the text of an uploaded contract to one third-party LLM API, under a commercial agreement. The provider is named on the public subprocessor list.
- Quorrel does not train or fine-tune models on customer data. The agreement prohibits the provider from using API inputs and outputs to train its models. Any future change would require each customer's opt-in.
- Under the agreement, the provider may keep API inputs and outputs for up to 30 days for abuse monitoring, after which they are deleted.
- Each request contains one customer's document and only the text needed for the extraction. Document text is treated as untrusted data, never as instructions. The model has no tools and no access to other data.
- Outputs are checked against a fixed schema. In the product, every extracted term is labelled as AI-generated and links to its source text, so that the user can review it.
- Before any change of model or prompt goes live, extraction accuracy is tested against a fixed test set, and the change follows the normal change process.
- A new model provider, or any new use of customer data with AI, needs the approval of the CTO and the CEO and an entry in the risk register. Customers who subscribe to subprocessor notices are told 30 days before a new provider is added.

## 7. Approving a new AI tool

A request is made through a Linear ticket that names the tool, the plan, what it will be used for and the data it would need. Before deciding, the CTO checks and records:

1. Whether the vendor uses inputs or outputs to train its models, on the specific plan Quorrel would buy
2. How long the vendor keeps inputs and outputs, and whether they can be deleted
3. Where the data is processed
4. Whether the tool supports Google sign-in and multi-factor authentication
5. What administrator controls and audit logs the plan provides
6. Which other companies the vendor passes data to
7. The highest data class the tool would be allowed to handle

The decision is recorded in the inventory as Approved, with the highest data class allowed, or Not approved, with the reason. Every entry is reviewed every six months, and sooner when a vendor changes its terms.

## 8. Reporting a problem

A workforce member reports to the CTO at once if Confidential data has been entered into a tool that is not approved for it, if an AI tool has exposed data it should not have, or if AI output has caused an error that reached a customer. The report is handled under the Incident Response Plan. Reporting early is never held against the person who reports.

## 9. Training and acknowledgement

Every workforce member acknowledges this policy when hired and once a year after that. From Q1 2027 the annual security training will include a section on this policy; until then, the policy has been presented at an all-hands meeting (see section 11).

## 10. Exceptions

An exception to this policy needs a written request that gives the reason and the risk, and the CEO's approval. An exception lasts at most 90 days and is recorded in the risk register.

## 11. Where this policy stands today

This table states plainly which parts of the policy are in place, partial, planned or not in place as of November 2026.

| Requirement | Status | What is and is not in place |
| --- | --- | --- |
| Inventory of AI tools (Annex A) | In place | First completed in November 2026 from a staff survey and the existing SaaS inventory. It lists 8 entries: 5 approved, 1 switched off pending review and 2 not approved. |
| Controls on AI in the product (section 6) | In place | In place since launch, and described the same way in the security questionnaire. |
| Company accounts for every AI tool (5.1) | Partial | The survey found two engineers using a personal plan of a coding assistant. Both moved to the company business plan in November 2026. Personal chat assistant accounts are prohibited by this policy but are not technically prevented. |
| AI features inside existing tools reviewed (5.6) | Partial | The team chat tool and the issue tracker have been reviewed and approved. The monitoring tool's AI features are switched off until their review in January 2027. |
| Technical blocking of unapproved AI tools | Not in place | There is no technical block. The company relies on this policy, the inventory, and a quarterly review of the third-party apps that staff have connected to their Google accounts. Browser and device controls will be evaluated in Q2 2027. |
| AI training for all staff (section 9) | Planned | The policy was presented at the November 2026 all-hands meeting. An AI section will be added to the annual security training in Q1 2027. |

## 12. Evidence this policy produces

Each requirement leaves a record. These are the records a customer's reviewer or an auditor can ask to see.

| Requirement | Evidence | How often |
| --- | --- | --- |
| 5.1, 7 Approved tools and approvals | AI tool inventory; Linear approval tickets; record of the terms checked and the date | Each request; inventory reviewed every six months |
| 5.1 Company accounts | Seat lists for each approved tool; quarterly review of connected third-party apps in Google Workspace | Quarterly |
| 5.3 Review of AI-assisted code | Pull request history showing review and passing checks | Each change |
| 6 AI in the product | Provider agreement clauses on training and retention; subprocessor list; evaluation results for each model or prompt change | Each change; agreement checked every six months |
| 8 Reporting | Incident records and their follow-up actions | Each report |
| 9 Training and acknowledgement | Acknowledgement records; training completion report once the AI section is added | At hire and annually |
| 10 Exceptions | Approved exception requests; risk register entries | Each exception |

## 13. Framework references

| Reference | What it covers | Sections |
| --- | --- | --- |
| AI RMF GOVERN 1.4 | The risk management process and its outcomes are set out in transparent policies, procedures and other controls | Whole policy |
| AI RMF GOVERN 1.6 | Mechanisms are in place to inventory AI systems | 7, Annex A |
| AI RMF GOVERN 2.1 | Roles, responsibilities and lines of communication for AI risk are documented and clear | 4 |
| AI RMF GOVERN 2.2 | Personnel receive AI risk management training | 9 |
| AI RMF GOVERN 3.2 | Policies define roles and responsibilities for human-AI configurations and oversight of AI systems | 5.3, 6 |
| AI RMF GOVERN 6.1 | Policies and procedures address AI risks associated with third-party entities | 6, 7 |
| AI RMF MEASURE 2.3 | AI system performance is measured for conditions similar to deployment, and the measures are documented | 6 |
| AI RMF MANAGE 3.1 | AI risks and benefits from third-party resources are regularly monitored, with controls applied and documented | 7, Annex A |
| AI RMF MANAGE 4.3 | Incidents and errors are communicated to relevant AI actors, and response processes are followed and documented | 8 |
| CSF GV.PO-01 | Policy for managing cybersecurity risks is established, communicated and enforced | Whole policy |
| CSF GV.SC-05 | Requirements to address supply chain cybersecurity risks are integrated into contracts and agreements | 6, 7 |
| CSF GV.SC-06 | Planning and due diligence are performed before entering supplier relationships | 7 |
| CSF GV.SC-07 | Risks posed by suppliers are understood, recorded and monitored over the course of the relationship | 7, Annex A |
| CSF ID.AM-02 | Inventories of software, services and systems are maintained | Annex A |
| CSF PR.AT-01 | Personnel are given awareness and training | 9 |

The descriptions above are summaries; see the source documents for the exact wording.

## 14. Enforcement and review

Breaking this policy can lead to loss of access and to disciplinary action. The CTO reviews this policy every six months and whenever an AI tool or model provider is added or changes its terms. The CEO approves each new version.

| Version | Date | Change | Approved by |
| --- | --- | --- | --- |
| 1.0 | August 2026 | First version, covering AI in the product and a short rule on workforce use | CEO |
| 1.1 | November 2026 | Added the AI tool inventory as Annex A, the rule on AI features inside existing tools, the rule on personal accounts and the status table in section 11 | CEO |

## Annex A: AI tool inventory

One row for each AI tool in use, requested or refused. The spreadsheet download holds the same inventory with each field in its own column.

| # | Tool | Used for and by | Highest data class | Vendor terms: training and retention | Sign-in | Status | Decision and next review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Third-party large language model (LLM) API, commercial agreement | Extracting contract terms inside Quorrel Intake. Used by: the application only; no person uses it directly | Confidential | Training: No. The agreement prohibits it. Retention: up to 30 days for abuse monitoring, then deleted | API key held in AWS Secrets Manager | Approved | CTO and CEO, August 2026. Next review: May 2027 |
| 2 | AI coding assistant, business plan | Code suggestions and chat in the editor. Used by: 7 engineers | Internal | Training: No, under the business plan terms (checked November 2026). Retention: not kept after the response is returned, under the plan terms | Company GitHub accounts, two-factor authentication enforced | Approved | CTO, November 2026. Next review: May 2027 |
| 3 | General-purpose AI chat assistant, team plan | Drafting, summarising and research. Used by: all 11 employees | Internal | Training: No. Training is switched off for the whole workspace (checked November 2026). Retention: deleted 30 days after a user deletes a conversation | Google sign-in with 2-Step Verification | Approved | CTO, November 2026. Next review: May 2027 |
| 4 | AI features in the team chat tool | Channel summaries and search. Used by: all 11 employees | Internal | Training: No, under the vendor's terms (checked November 2026). Retention: follows the workspace retention setting | Google sign-in | Approved | CTO, November 2026. Next review: May 2027 |
| 5 | AI features in the issue tracker | Drafting and summarising tickets. Used by: engineering and customer success | Internal | Training: No, under the vendor's terms (checked November 2026). Retention: follows the workspace retention setting | Google sign-in | Approved | CTO, November 2026. Next review: May 2027 |
| 6 | AI features in the monitoring tool | Log summaries and suggested queries. Used by: no one; the feature is switched off | None until reviewed | Training: Not yet checked. Retention: not yet checked | Google sign-in | Off pending review | CTO; review due January 2027, because logs can contain customer identifiers. Next review: January 2027 |
| 7 | AI meeting note-taker | Recording and summarising calls (requested by customer success). Used by: no one | None | Training: The vendor's standard terms allowed recordings to be used to improve its service. Retention: not applicable | Not applicable | Not approved | CTO, November 2026. It would record customer calls, which are Confidential. Next review: On request |
| 8 | Personal AI accounts of any kind | Any work use. Used by: no one | None | Training: Depends on the account; cannot be checked or controlled by Quorrel. Retention: cannot be checked | Personal sign-in outside company control | Not approved | CTO, November 2026. Replaced by tools 2 and 3. Next review: Not applicable |

## Reviewer notes

What changed during review. On real work, these notes go to the client with the draft so that nothing is overstated.

| Where | What changed in review |
| --- | --- |
| Sections 5.2 and 6 | The founder's draft said "we never send customer data to AI tools". The product sends the text of each uploaded contract to the LLM API, so the sentence was untrue. The policy now names the one tool that receives customer data and the terms it does so under. |
| Annex A | The intake form listed two AI tools. A short staff survey found five in use, including two personal accounts for a coding assistant. All were added to the inventory, and the personal accounts were recorded as a gap and closed. |
| Section 11 | The draft said "all AI tools are blocked unless approved". No technical block exists. The policy now says so, and lists blocking as not in place with a date for evaluating it. |
| Annex A, tool 3 | The statement that the chat assistant does not train on Quorrel's data came from the vendor's marketing page. It was confirmed against the team plan terms and the workspace setting, and the date of the check was recorded. |
| Section 9 | The draft said AI training was complete. Only an all-hands briefing had taken place, so training is shown as Planned with a date. |
| Section 6 | The provider's retention period was matched to question 28 of the security questionnaire, so the policy and the questionnaire give the same figure. |

## Sources

- **NIST AI RMF references:** NIST AI 100-1, Artificial Intelligence Risk Management Framework (AI RMF 1.0), January 2023.
- **NIST CSF references:** NIST CSWP 29, The NIST Cybersecurity Framework (CSF) 2.0, February 26, 2024.

## Want one like this for your company?

[See AI use policy pricing](ai-policy.md){ .md-button .md-button--primary } [Book a 15-minute call](https://cal.com/lloyd-johnson){ .md-button }

<small>Documentation and preparation services only. Not legal advice, an audit, or a certification.</small>
