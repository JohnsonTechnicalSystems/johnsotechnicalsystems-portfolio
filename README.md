# Johnson Technical Systems | GRC & Technical Documentation Portfolio

Compliance documentation, SOPs, and control mappings for small and mid-sized organizations.

Practical SOPs, configuration guides, and compliance documentation produced while studying for CompTIA Network+ and Security+, written to demonstrate real-world technical translation and GRC (Governance, Risk, and Compliance) consulting skills.

Every document maps to a specific study milestone and follows a consistent template (see `/templates`). Drafts are produced with AI assistance (a local LLM via Ollama/Open WebUI, and Claude Code), then reviewed, fact-checked, and corrected by the author before publishing. The status field on each document reflects its actual review state.

**Documents are illustrative examples written for generic or fictional organizations. They are not client deliverables and contain no client data.**

## Index

| Document | Milestone | Status | Date | Sources |
|----------|-----------|--------|------|---------|
| [SOP-001: Secure Remote Access to Windows Workstations](sops/sop-001-secure-remote-access.md) | Security+ Frameworks | Draft | 2026-09-18 | Microsoft Remote Desktop documentation, NIST SP 800-53, ISO/IEC 27001:2022, CIS Controls v8, AICPA SOC 2 |
| [SOP-002: Local LLM Inference Stack: Operation & Troubleshooting](sops/sop-002-local-llm-inference-stack.md) | Network Operations & Troubleshooting | Draft | 2026-09-29 | Ollama & Open WebUI documentation, NIST SP 800-53, ISO/IEC 27001:2022 |
| [SOP-003: Network Troubleshooting Runbook](sops/sop-003-network-troubleshooting-runbook.md) | Network Operations & Troubleshooting | Draft | 2026-09-29 | CompTIA Network+ N10-009 objectives, NIST SP 800-53, ISO/IEC 27001:2022 |
| [SOP-004: Cat6 Cable Termination and Testing (T568B)](sops/sop-004-cat6-termination-and-testing.md) | Network+ Fundamentals | Draft | 2026-09-29 | ANSI/TIA-568, ANSI/TIA-606, NIST SP 800-53 |
| [SOP-005: VLAN Creation and Segmentation on a Managed Switch](sops/sop-005-vlan-creation-and-segmentation.md) | Subnetting & VLANs | Draft | 2026-09-29 | Cisco IOS documentation, NIST SP 800-53, AICPA SOC 2 |
| [SOP-006: Endpoint Isolation During a Suspected Compromise](sops/sop-006-endpoint-isolation.md) | Security+ Frameworks | Draft | 2026-09-29 | NIST SP 800-61, NIST SP 800-53, AICPA SOC 2 |

## Milestones

- **Network+ Fundamentals**: core network layers, physical topology, cabling standards
- **Subnetting & VLANs**: logical network segmentation, multi-VLAN design
- **Security+ Frameworks**: incident response, endpoint isolation, NIST/SOC 2 alignment
- **Network Operations & Troubleshooting**: running, maintaining, and diagnosing live systems (Network+ N10-009 domains 3.0 and 5.0)

## About the review process

- **Draft**: AI-assisted first pass; not yet verified. Do not treat as authoritative.
- **Reviewed**: every factual and control reference checked by the author against primary sources (NIST SP 800-53, AICPA SOC 2 Trust Services Criteria, vendor documentation).
- **Published**: reviewed, finalized, and linked from the index.
