# Changelog

All documents remain Drafts until their status field says otherwise.

## 2026-11-26: Add five samples; remove the SOP template and lab work pages

- New samples, each for a fictional business and each with a PDF download: an AI use policy with an AI tool inventory, a public security page with a claim check, and a cyber insurance renewal pack (30 application answers, evidence summary, gap list and one-page incident response plan). The inventory and the renewal pack also come as spreadsheets.
- Two samples first written for Upwork are now on the site: an access control policy and a written information security plan (WISP) for a tax practice. In the WISP, the incident steps now follow the IRS data theft page (contact the local FBI office; the Secret Service if directed), and the IRS Publication 4557 revision is corrected to Rev. 6-2024.
- NIST CSF 2.0 and NIST AI RMF 1.0 identifiers in the new samples were checked against NIST CSWP 29 and NIST AI 100-1; the Safeguards Rule citations in the WISP were rechecked against 16 CFR Part 314.
- The samples index now lists the security and compliance documents first, with the service each one relates to. The AI use policy, WISP, insurance pack, partner and home pages link to the new samples.
- Removed the SOP template and lab work pages from the site (moved to archive/). They read as study material, not client-facing samples. The evidence-handling note from the lab work page is now on the review process page.

## 2026-11-26: Broaden the sharing image and description to small firms

- The social share image now reads "For small firms" in place of "For early-stage software and AI companies". The headline, colors, font and 1200x630 size are unchanged.
- The site description and homepage title, which feed the Open Graph and Twitter card text, now describe written security documentation for small firms.
- The homepage opening sentence and the README now name small firms and the buyers served (startups, small finance firms, MSPs and vCISO partners), and the homepage sentence lists AI use policies and WISPs alongside questionnaires.
- The security questionnaires page now addresses software, AI and other small firms with a deal waiting on a security review, in place of seed to Series A software and AI companies only.

## 2026-11-23: Rebuild the site around paid services

- New homepage that leads with the offer: security questionnaires, starter policy packs and public security pages for early-stage software and AI companies, with prices, a three-step process and contact details.
- Service pages for cold outreach to link to: questionnaires, partners, AI use policy, documentation and automation.
- Added a Security page on how client documents are handled, plus Terms and Privacy pages and a footer disclaimer.
- Removed the "nothing verified" banner from the homepage. SOPs now sit under Samples as illustrative examples, each still showing its Draft status.
- Added WISP pack (FTC Safeguards Rule) and cyber insurance renewal pack pages; WISP references checked against 16 CFR Part 314 and IRS IR-2026-92.
- Archived the standalone documentation page to archive/.
- Stage-1 starting prices; partner first job at 25% off; veteran-owned noted.
- Replaced the Security & Compliance and Technical Writing track pages with the new service pages; renamed Homelab to Lab work.

## 2026-10-03: Restructure for three tracks

### Positioning

- Repositioned from a single SOC 2 and GRC focus to three tracks drawn from the same documents: Security & Compliance Documentation, Technical Writing, and Homelab.
- Added a landing page for each track and a home page that routes readers to the right one.
- Added a Draft banner to the README and every landing page, and stated on the Review Process page that no document has been Reviewed yet.

### Document fixes (all still Draft, changes not yet tested)

- **SOP-001:** recorded the mesh VPN key-expiry exemption as an accepted risk with five compensating controls; moved the ISP outage failure mode to SOP-003; renumbered from 1.0 to 0.2 to match Draft status.
- **SOP-002:** bound Open WebUI to loopback and published it with Tailscale Serve, so it is no longer reachable from the local network; pinned the container image to a release tag instead of `:main`; stop the container before copying the database; added a rollback procedure and two verification checks.
- **SOP-003:** remapped controls from incident response (IR-4, IR-5, ISO 5.25 to 5.27) to documented operating procedures and maintenance records (ISO 5.37, NIST MA-2), since the cases are operational faults.
- **SOP-005:** separated the native VLAN (998) from the parking VLAN (999); added a VLAN 99 management interface with an SSH-only access list; added BPDU guard on access ports; aligned verification with the layer 2 scope; remapped trunk controls from SOC 2 CC6.6 to CC6.1.
- **SOP-006:** cited NIST SP 800-61 Rev. 3 by name and tied the procedures to CSF 2.0 Respond and Recover.
- **All SOPs and the template:** owner field now reads "Lloyd Johnson, Johnson Technical Systems LLC". Code blocks inside numbered steps are indented so the steps render in order.
- **Template:** placeholders changed from `<Name>` to `[Name]` so they display on the site instead of being read as HTML.

### Structure and tooling

- Moved `sops/` and `templates/` into `docs/` for the site build.
- Added `mkdocs.yml` for a Zensical site build with light and dark themes.
- Added a GitHub Actions workflow that lints Markdown, builds the site in strict mode (failing on broken internal links), and deploys to GitHub Pages from `main`.
- Added a CC BY-NC-ND 4.0 license for the documentation.
- Set the site URL to johnsontechnicalsystems.com. The custom domain itself is configured in the repository's Pages settings and in Cloudflare DNS.
