# Changelog

All documents remain Drafts until their status field says otherwise.

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
