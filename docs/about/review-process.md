# Review Process

## Document status

As of November 2026, SOP-001 and SOP-006 are Approved. SOP-002 to SOP-005 are Drafts.

| Status | Meaning |
| --- | --- |
| Draft | Written and internally consistent, but not every command, step, and control reference has been checked against primary sources yet |
| Reviewed | Every factual claim, command, and control reference checked by the author against primary sources: NIST SP 800-53 Rev 5, ISO/IEC 27001:2022, AICPA Trust Services Criteria, vendor documentation, and the relevant standard |
| Approved | Reviewed, the environment it describes confirmed by the owner, and issued as version 1.0 or later with an effective date and next review date |

A document moves up a status through a commit that records what was checked and against which source. The commit history is the audit trail for each review.

## Use of AI

First drafts are produced with AI assistance, using a local model and Claude Code. AI output is treated as a draft from a junior writer: every command is checked against vendor documentation or run in the lab, every control reference is checked against the framework text, and anything that cannot be verified is removed or marked for verification. The status field shows how far that checking has gone.

## Real and illustrative content

SOP-001, SOP-002, and SOP-003 document systems the author built and faults the author diagnosed. Identifying details are omitted. SOP-004, SOP-005, and SOP-006 are written for a generic small office and do not describe any client environment.

None of these documents contain client data, and none are client deliverables.

## Evidence handling

Published evidence is redacted before it is committed. Public IP addresses are replaced with documentation ranges (192.0.2.0/24, 198.51.100.0/24, 203.0.113.0/24), and serial numbers, wireless keys, account names, and hostnames that identify a real location are removed.

## Limits

These documents are portfolio samples. They are not legal advice, an audit opinion, or a certification. Control mappings record the author's intent and should be confirmed by a qualified assessor for any real environment.
