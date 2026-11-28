# Johnson Technical Systems | Security Documentation, Technical Writing & Homelab

> **Check each document's status before relying on it.** Approved documents have been checked against primary sources and confirmed by the owner. Drafts have not, so do not rely on a Draft as authoritative. The index below lists the current status of each SOP.

Security documentation, technical writing, and the lab work behind them, by Lloyd Johnson, Johnson Technical Systems LLC.

Site: [johnsontechnicalsystems.com](https://johnsontechnicalsystems.com)

I build it, document it, and map it to controls. The procedures here come from systems I configured, faults I diagnosed, and study scenarios written while preparing for CompTIA Network+ and Security+. Each one follows the same [SOP template](docs/templates/sop-template.md) and is mapped to NIST SP 800-53, ISO/IEC 27001:2022, and SOC 2 where a control applies.

## What the site offers

The site at [johnsontechnicalsystems.com](https://johnsontechnicalsystems.com) leads with written security documentation for small firms (startups, small finance firms, MSPs and vCISO partners): security questionnaires, starter policy packs and public security pages, with pages for partner overflow work, FTC Safeguards Rule WISP packs, cyber insurance renewal packs, AI use policies and automation. The SOPs below are published there under Samples as illustrative examples.

## Index

The status and version of each SOP come from the SOP's own Document Control table. `scripts/sync_status.py` copies them here, and the CI check fails if this list falls out of step.

<!-- sop-index:start -->

| Document | Status | Version | Sources |
| --- | --- | --- | --- |
| [SOP-001: Secure Remote Access to Windows Workstations](docs/sops/sop-001-secure-remote-access.md) | Approved | 1.0 | Microsoft Remote Desktop documentation, NIST SP 800-53, ISO/IEC 27001:2022, CIS Controls v8, AICPA SOC 2 |
| [SOP-002: Local LLM Inference Stack: Operation & Troubleshooting](docs/sops/sop-002-local-llm-inference-stack.md) | Draft | 0.2 | Ollama, Open WebUI, and Tailscale documentation, NIST SP 800-53, ISO/IEC 27001:2022 |
| [SOP-003: Network Troubleshooting Runbook](docs/sops/sop-003-network-troubleshooting-runbook.md) | Draft | 0.2 | CompTIA Network+ N10-009 objectives, NIST SP 800-53, ISO/IEC 27001:2022 |
| [SOP-004: Cat6 Cable Termination and Testing (T568B)](docs/sops/sop-004-cat6-termination-and-testing.md) | Draft | 0.1 | ANSI/TIA-568, ANSI/TIA-606, NIST SP 800-53 |
| [SOP-005: VLAN Creation and Segmentation on a Managed Switch](docs/sops/sop-005-vlan-creation-and-segmentation.md) | Draft | 0.2 | Cisco IOS documentation, NIST SP 800-53, AICPA SOC 2 |
| [SOP-006: Endpoint Isolation During a Suspected Compromise](docs/sops/sop-006-endpoint-isolation.md) | Approved | 1.0 | NIST SP 800-61 Rev. 3, NIST SP 800-53, AICPA SOC 2 |

<!-- sop-index:end -->

## Review process

- **Draft**: written and internally consistent, but not yet checked against primary sources.
- **Reviewed**: every command, step, and control reference checked by the author against primary sources (NIST SP 800-53, AICPA SOC 2 Trust Services Criteria, ISO/IEC 27001:2022, vendor documentation).
- **Approved**: reviewed, the environment it describes confirmed by the owner, and issued as version 1.0 or later with an effective date and next review date.

A document moves up a status through a pull request that records what was checked. First drafts are produced with AI assistance (a local model via Ollama and Open WebUI, and Claude Code), and nothing leaves Draft until the author has verified it. Details are in [docs/about/review-process.md](docs/about/review-process.md).

SOP-001 to SOP-003 document systems the author built and faults the author diagnosed, with identifying details omitted. SOP-004 to SOP-006 are written for a generic small office. None contain client data, and none are client deliverables.

These documents are portfolio samples, not legal advice, an audit opinion, or a certification.

## Repository layout

```text
docs/                 Site content (built with Zensical from mkdocs.yml)
  index.md            Home page and document list
  questionnaires.md, partners.md, wisp.md, insurance-pack.md, ai-policy.md, automation.md   Service pages
  samples.md, lab-work.md   Samples overview and lab work
  security.md, legal/   Data handling, Terms and Privacy
  sops/               SOP-001 to SOP-006
  templates/          SOP template
  about/              Review process, AI use, and limits
.github/workflows/    Lint, build and status-sync checks; deploys the site from main
scripts/              sync_status.py keeps SOP status lists in step with the SOPs
archive/              Retired pages, not built into the site
CHANGELOG.md          What changed and when
```

## License

Documentation is licensed under [Creative Commons Attribution-NonCommercial-NoDerivatives 4.0](LICENSE) (CC BY-NC-ND 4.0). You may share it with attribution, but not sell it or publish modified versions.
