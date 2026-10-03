# SOP-004: Cat6 Cable Termination and Testing (T568B)

Sep 29, 2026 · @Lloyd

## 1. Document Control

| Field | Value |
| --- | --- |
| Document ID | SOP-004 |
| Version | 0.1 (Draft) |
| Owner | Lloyd Johnson, Johnson Technical Systems LLC |
| Milestone | Network+ Fundamentals |
| Review cycle | Every 12 months, or when the cabling standard is revised |
| Classification | Internal / Portfolio sample |
| Related | SOP-005 VLAN Creation and Segmentation; SOP-003 Network Troubleshooting Runbook |

## 2. Purpose and Scope

This SOP standardizes how copper Category 6 UTP cable is terminated, labeled, and tested. The goal is that every horizontal run is consistent, traceable, and verified before it goes into service.

**In scope:** new or re-terminated Cat6 UTP horizontal cabling, both patch panel to wall outlet and field-made patch cords, installed by internal staff or contractors at a generic small office.

**Out of scope:** fiber, shielded cable (F/UTP, S/FTP), and cabling installed under a separate certified-installer contract.

## 3. Reference: T568B Pin Assignment

| Pin | Color |
| --- | --- |
| 1 | White/Orange |
| 2 | Orange |
| 3 | White/Green |
| 4 | Blue |
| 5 | White/Blue |
| 6 | Green |
| 7 | White/Brown |
| 8 | Brown |

| Limit | Value |
| --- | --- |
| Permanent link (panel to outlet) | 90 m maximum |
| Channel (including patch cords) | 100 m maximum |
| Pair untwist at termination | 0.5 in (13 mm) maximum |
| Bend radius (UTP) | At least 4x cable outside diameter |

## 4. Procedure A: Termination

1. Assign an identifier using the site's TIA-606 labeling scheme, for example `TR1-PP02-14` for telecom room 1, patch panel 2, port 14. Record it in the cable inventory before pulling.
2. Confirm the planned run fits within the limits in Section 3.
3. Pull the cable without exceeding the manufacturer's maximum pulling tension. Keep it away from fluorescent fixtures, motors, and power lines.
4. Strip only as much jacket as the jack or connector needs. Do not nick the conductor insulation. Remove the spline if present.
5. Arrange the pairs in T568B order (Section 3). Keep each pair twisted to within 0.5 in of the termination point.
6. Punch down to the keystone jack or patch panel with a 110 tool, or crimp an RJ45 plug rated for Cat6. Confirm the jacket sits inside the strain relief.
7. Use T568B at both ends. Do not mix T568A and T568B on one run unless a crossover is required and documented.

## 5. Procedure B: Testing and Labeling

1. Run at least a wiremap test (opens, shorts, reversed, crossed, and split pairs) and a length test.
2. Where a certification tester is available, certify to Cat6 permanent link limits and save the result.
3. Apply the identifier at both ends, within 12 in of the termination.
4. Update the cable inventory with the test result, date, and technician.
5. Re-terminate and retest any run that fails. Do not put a failed run into service.

## 6. Verification

- [ ] Wiremap passes on every pair with no split pairs
- [ ] Measured length is within the limits in Section 3
- [ ] Both ends are labeled with the same identifier
- [ ] The cable inventory entry includes the test result, date, and technician

## 7. Responsible Parties

| Role | Responsibility |
| --- | --- |
| Network Technician | Terminates, tests, labels, and records each run |
| IT Manager | Owns the labeling scheme and inventory; spot-checks test records |
| Contractor (if used) | Follows this SOP and delivers test results before sign-off |

## 8. Control Mapping

Verify each reference against the published text before changing status to Reviewed.

| Procedure step | Standard or control | Why it applies |
| --- | --- | --- |
| Pin assignment, length and untwist limits (Sections 3 and 4) | ANSI/TIA-568 (verify current revision, 568.2-D or later) | Source of the T568B scheme and Cat6 performance requirements |
| Labeling and records (Procedure B) | ANSI/TIA-606 (verify current revision) | Source of the labeling and record-keeping requirements |
| Cable inventory (Procedure B) | NIST SP 800-53 Rev 5 CM-8 System Component Inventory | Network infrastructure components are tracked and documented |
| Documented, labeled runs | NIST SP 800-53 Rev 5 PE-4 Access Control for Transmission | Known cabling makes unauthorized taps or changes easier to detect |

## 9. Revision History

| Version | Date | Change |
| --- | --- | --- |
| 0.1 | 2026-09-29 | Initial AI-assisted draft; not yet fact-checked |
