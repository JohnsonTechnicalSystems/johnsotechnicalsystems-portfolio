# Johnson Technical Systems

> **Work in progress: every document is a Draft.** Nothing on this site has been verified yet. Commands, steps, and control references have not been checked against primary sources or retested in the lab. Do not rely on any document as authoritative until its status reads Reviewed. See [Review Process](about/review-process.md).

Security documentation, technical writing, and the lab work behind them.

I build it, document it, and map it to controls. The procedures here come from systems I configured, faults I diagnosed, and study scenarios for a generic small office, written to a consistent template and mapped to NIST SP 800-53, ISO/IEC 27001:2022, and SOC 2 where a control applies.

## Pick your path

| If you need | Start here |
| --- | --- |
| Security policies, SOPs, and control mappings for an audit or a customer questionnaire | [Security & Compliance Documentation](security-compliance.md) |
| Runbooks, procedures, knowledge base articles, or a documentation cleanup | [Technical Writing](technical-writing.md) |
| Evidence that the documentation reflects real, working configurations | [Homelab](homelab.md) |

## How the work is produced

- **Docs as code.** Every document is Markdown in Git, reviewed through pull requests, and checked by CI before it is published.
- **One template.** Each SOP has the same sections: document control, scope, procedure, verification, failure modes, control mapping, and revision history.
- **Honest status.** Each document is marked Draft, Reviewed, or Published, and the label reflects its actual review state. See [Review Process](about/review-process.md).
- **AI-assisted, verified before release.** First drafts are produced with AI assistance. Every command, step, and control reference must be checked by the author before a document leaves Draft. No document has completed that check yet.

## Documents

| Document | Track | Status |
| --- | --- | --- |
| [SOP-001: Secure Remote Access to Windows Workstations](sops/sop-001-secure-remote-access.md) | Compliance, Homelab | Draft |
| [SOP-002: Local LLM Inference Stack](sops/sop-002-local-llm-inference-stack.md) | Homelab, Writing | Draft |
| [SOP-003: Network Troubleshooting Runbook](sops/sop-003-network-troubleshooting-runbook.md) | Writing, Homelab | Draft |
| [SOP-004: Cat6 Cable Termination and Testing](sops/sop-004-cat6-termination-and-testing.md) | Writing | Draft |
| [SOP-005: VLAN Creation and Segmentation](sops/sop-005-vlan-creation-and-segmentation.md) | Compliance, Writing | Draft |
| [SOP-006: Endpoint Isolation During a Suspected Compromise](sops/sop-006-endpoint-isolation.md) | Compliance | Draft |
| [SOP Template](templates/sop-template.md) | All | Template |
