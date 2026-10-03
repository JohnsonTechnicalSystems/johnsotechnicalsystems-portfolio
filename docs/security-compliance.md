# Security & Compliance Documentation

> **Work in progress: every document is a Draft.** Nothing on this site has been verified yet. Commands, steps, and control references have not been checked against primary sources or retested in the lab. Do not rely on any document as authoritative until its status reads Reviewed. See [Review Process](about/review-process.md).

Policies, SOPs, and control mappings that an auditor, assessor, or customer security reviewer can trace from requirement to procedure to evidence.

## What I write

- Standard operating procedures with verification steps and evidence lists
- Security policies for small and mid-sized organizations
- Control mappings to NIST SP 800-53 Rev 5, ISO/IEC 27001:2022 Annex A, AICPA SOC 2 Trust Services Criteria, and CIS Controls v8
- Incident response procedures and playbooks

## Start with these

All samples below are Drafts.

| Document | Why it is a good sample |
| --- | --- |
| [SOP-001: Secure Remote Access](sops/sop-001-secure-remote-access.md) | Full control mapping across four frameworks, a recorded risk acceptance with compensating controls, and a verification test (V-3) that proves the control instead of assuming it |
| [SOP-006: Endpoint Isolation](sops/sop-006-endpoint-isolation.md) | Incident containment aligned to NIST SP 800-61 Rev. 3, with evidence preservation and SOC 2 CC7 mapping |
| [SOP-005: VLAN Segmentation](sops/sop-005-vlan-creation-and-segmentation.md) | A change-controlled network procedure with management-plane restrictions and CM-3 / CC8.1 change evidence |

## In progress

- A starter policy set for a fictional company: information security, access control, acceptable use, change management, and incident response
- A control matrix that links each control to its policy, its SOP, and the lab evidence that shows it working
- A risk register and a ransomware tabletop exercise built on SOP-006

## Scope of this work

These documents support readiness for an audit or assessment. They are not an audit opinion or a certification. A SOC 2 report can only be issued by a licensed CPA firm, and an ISO/IEC 27001 certificate only by an accredited certification body. Control mappings record the author's intent and are not an assessor's determination. See [Review Process](about/review-process.md).
