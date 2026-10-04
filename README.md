# Johnson Technical Systems | Security Documentation, Technical Writing & Homelab

> **Work in progress: every document in this repository is a Draft.** Nothing has been verified against primary sources or retested in the lab yet. Do not rely on any document as authoritative until its status reads Reviewed.

Security documentation, technical writing, and the lab work behind them, by Lloyd Johnson, Johnson Technical Systems LLC.

Site: [johnsontechnicalsystems.com](https://johnsontechnicalsystems.com)

I build it, document it, and map it to controls. The procedures here come from systems I configured, faults I diagnosed, and study scenarios written while preparing for CompTIA Network+ and Security+. Each one follows the same [SOP template](docs/templates/sop-template.md) and is mapped to NIST SP 800-53, ISO/IEC 27001:2022, and SOC 2 where a control applies.

## Three tracks, one body of work

| Track | For | Landing page |
| --- | --- | --- |
| Security & Compliance Documentation | Policies, SOPs, and control mappings for audit readiness and customer security reviews | [docs/security-compliance.md](docs/security-compliance.md) |
| Technical Writing | Runbooks, procedures, knowledge base articles, and documentation cleanup | [docs/technical-writing.md](docs/technical-writing.md) |
| Homelab | The working configurations and evidence behind the documents | [docs/homelab.md](docs/homelab.md) |

The tracks share documents rather than competing for them. One lab produces a configuration and evidence (homelab), a procedure (technical writing), and control mappings (compliance).

## Index

| Document | Milestone | Status | Version | Sources |
| --- | --- | --- | --- | --- |
| [SOP-001: Secure Remote Access to Windows Workstations](docs/sops/sop-001-secure-remote-access.md) | Security+ Frameworks | Draft | 0.2 | Microsoft Remote Desktop documentation, NIST SP 800-53, ISO/IEC 27001:2022, CIS Controls v8, AICPA SOC 2 |
| [SOP-002: Local LLM Inference Stack: Operation & Troubleshooting](docs/sops/sop-002-local-llm-inference-stack.md) | Network Operations & Troubleshooting | Draft | 0.2 | Ollama, Open WebUI, and Tailscale documentation, NIST SP 800-53, ISO/IEC 27001:2022 |
| [SOP-003: Network Troubleshooting Runbook](docs/sops/sop-003-network-troubleshooting-runbook.md) | Network Operations & Troubleshooting | Draft | 0.2 | CompTIA Network+ N10-009 objectives, NIST SP 800-53, ISO/IEC 27001:2022 |
| [SOP-004: Cat6 Cable Termination and Testing (T568B)](docs/sops/sop-004-cat6-termination-and-testing.md) | Network+ Fundamentals | Draft | 0.1 | ANSI/TIA-568, ANSI/TIA-606, NIST SP 800-53 |
| [SOP-005: VLAN Creation and Segmentation on a Managed Switch](docs/sops/sop-005-vlan-creation-and-segmentation.md) | Subnetting & VLANs | Draft | 0.2 | Cisco IOS documentation, NIST SP 800-53, AICPA SOC 2 |
| [SOP-006: Endpoint Isolation During a Suspected Compromise](docs/sops/sop-006-endpoint-isolation.md) | Security+ Frameworks | Draft | 0.2 | NIST SP 800-61 Rev. 3, NIST SP 800-53, AICPA SOC 2 |

## Milestones

- **Network+ Fundamentals**: core network layers, physical topology, cabling standards
- **Subnetting & VLANs**: logical network segmentation, multi-VLAN design
- **Security+ Frameworks**: incident response, endpoint isolation, NIST/SOC 2 alignment
- **Network Operations & Troubleshooting**: running, maintaining, and diagnosing live systems (Network+ N10-009 domains 3.0 and 5.0)

## Review process

- **Draft**: written and internally consistent, but not yet checked against primary sources. Every document is currently a Draft.
- **Reviewed**: every command, step, and control reference checked by the author against primary sources (NIST SP 800-53, AICPA SOC 2 Trust Services Criteria, ISO/IEC 27001:2022, vendor documentation).
- **Published**: reviewed, given version 1.0 or later, and featured on the landing pages.

A document moves up a status through a pull request that records what was checked. First drafts are produced with AI assistance (a local model via Ollama and Open WebUI, and Claude Code), and nothing leaves Draft until the author has verified it. Details are in [docs/about/review-process.md](docs/about/review-process.md).

SOP-001 to SOP-003 document systems the author built and faults the author diagnosed, with identifying details omitted. SOP-004 to SOP-006 are written for a generic small office. None contain client data, and none are client deliverables.

These documents are portfolio samples, not legal advice, an audit opinion, or a certification.

## Repository layout

```text
docs/                 Site content (built with Zensical from mkdocs.yml)
  index.md            Home page and document list
  security-compliance.md, technical-writing.md, homelab.md   Track landing pages
  sops/               SOP-001 to SOP-006
  templates/          SOP template
  about/              Review process, AI use, and limits
.github/workflows/    Lint and build checks; deploys the site from main
CHANGELOG.md          What changed and when
```

## License

Documentation is licensed under [Creative Commons Attribution-NonCommercial-NoDerivatives 4.0](LICENSE) (CC BY-NC-ND 4.0). You may share it with attribution, but not sell it or publish modified versions.
