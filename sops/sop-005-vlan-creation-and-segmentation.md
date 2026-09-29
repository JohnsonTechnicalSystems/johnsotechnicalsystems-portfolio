# SOP-005: VLAN Creation and Segmentation on a Managed Switch

Sep 29, 2026 · @Lloyd

## 1. Document Control

| Field | Value |
| --- | --- |
| Document ID | SOP-005 |
| Version | 0.1 (Draft) |
| Owner | Lloyd Johnson, johnsontechnicalsystems LLC |
| Milestone | Subnetting & VLANs |
| Review cycle | Every 6 months, or after any switch platform or IOS upgrade |
| Classification | Internal / Portfolio sample |
| Related | SOP-004 Cat6 Cable Termination; SOP-003 Network Troubleshooting Runbook |

## 2. Purpose and Scope

This SOP defines a repeatable, change-controlled process for creating VLANs and assigning switch ports. It separates user, server, voice, and management traffic into distinct broadcast domains and limits lateral movement between them.

**In scope:** Cisco IOS / IOS-XE managed access switches at a generic small office. Other vendors follow the same steps with their own syntax.

**Out of scope:** inter-VLAN routing and firewall rules.

## 3. VLAN Plan

| VLAN | Name | Subnet | Purpose |
| --- | --- | --- | --- |
| 10 | USERS | 10.10.10.0/24 | Staff workstations |
| 20 | SERVERS | 10.10.20.0/24 | Internal servers |
| 30 | VOICE | 10.10.30.0/24 | IP phones |
| 99 | MGMT | 10.10.99.0/24 | Switch and AP management |
| 999 | BLACKHOLE | none | Unused ports and native VLAN |

## 4. Procedure A: Change Preparation

1. Open a change request listing the VLAN IDs, names, subnets, affected ports, rollback plan, and maintenance window. Get approval before making changes.
2. Back up the current configuration with `copy running-config tftp:`, or save the `show running-config` output to the change ticket.

## 5. Procedure B: Configuration

1. Create and name the VLANs:

```
configure terminal
vlan 10
 name USERS
vlan 20
 name SERVERS
vlan 30
 name VOICE
vlan 99
 name MGMT
vlan 999
 name BLACKHOLE
exit
```

2. Assign access ports:

```
interface range gigabitEthernet1/0/1 - 20
 switchport mode access
 switchport access vlan 10
 switchport voice vlan 30
 spanning-tree portfast
exit
```

3. Configure the uplink trunk with an explicit allowed list and an unused native VLAN. On platforms that also support ISL, add `switchport trunk encapsulation dot1q` before `switchport mode trunk`.

```
interface gigabitEthernet1/0/48
 switchport mode trunk
 switchport trunk native vlan 999
 switchport trunk allowed vlan 10,20,30,99
 switchport nonegotiate
exit
```

4. Park and shut down unused ports:

```
interface range gigabitEthernet1/0/21 - 47
 switchport mode access
 switchport access vlan 999
 shutdown
exit
```

5. Save the configuration: `copy running-config startup-config`.

## 6. Verification

- [ ] `show vlan brief` lists every VLAN with the expected ports
- [ ] `show interfaces trunk` shows only VLANs 10, 20, 30, and 99 allowed, with native VLAN 999
- [ ] `show interfaces status` shows unused ports disabled
- [ ] A host in each VLAN gets the expected address and reaches its gateway
- [ ] Before and after configs and verification output are attached to the change ticket
- [ ] The network diagram and VLAN/IP plan are updated

## 7. Responsible Parties

| Role | Responsibility |
| --- | --- |
| Network Administrator | Plans the VLANs, makes the change, and verifies results |
| IT Manager / Change Advisory Board | Approves the change and reviews post-change evidence |
| Security Lead | Confirms segmentation matches data-flow and access requirements |

## 8. Control Mapping

Verify each reference against the published text before changing status to Reviewed. Verify each command against the Cisco configuration guide for the specific switch model and IOS version.

| Procedure step | NIST SP 800-53 Rev 5 | AICPA SOC 2 (TSC 2017) |
| --- | --- | --- |
| Separate VLANs by trust level (Section 3) | SC-7 Boundary Protection | CC6.1 Logical access security |
| Trunk allowed list, parked unused ports (Procedure B) | AC-4 Information Flow Enforcement | CC6.6 Protection against threats from outside system boundaries |
| Approved change with backup and rollback (Procedure A) | CM-3 Configuration Change Control | CC8.1 Change management |
| Updated diagram and VLAN plan (Section 6) | CM-2 Baseline Configuration | CC8.1 Change management |

## 9. Revision History

| Version | Date | Change |
| --- | --- | --- |
| 0.1 | 2026-09-29 | Initial AI-assisted draft; not yet fact-checked |
