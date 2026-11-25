# SOP-001: Secure Remote Access to Windows Workstations

| Field | Value |
| --- | --- |
| Document ID | SOP-001 |
| Version | 1.0 |
| Status | Approved |
| Owner | Lloyd Johnson, johnsontechnicalsystems LLC |
| Effective date | 2026-11-26 |
| Next scheduled review | 2027-05-26 |
| Review cycle | Semiannual, or upon material change to the access path |
| Classification | Internal |
| Related | SOP-002 Local LLM Inference Stack; SOP-003 Network Troubleshooting Runbook |

## 1. Purpose

This procedure defines the required configuration for remote graphical access to Windows workstations operated by Johnson Technical Systems.

Remote access is the highest-risk access path into any workstation. It authenticates a user who is not physically present, it is reachable by anyone who can route to the host, and it grants a full interactive desktop rather than a scoped set of commands. Microsoft advises against exposing Remote Desktop Protocol (RDP) directly to the internet, and internet-facing RDP is a common target for automated scanning and password guessing.

This procedure exists to ensure that remote access to a workstation is:

1. Unreachable from the public internet by design, rather than by obscurity.
2. Authenticated before a session is established, not after.
3. Granted only to a named account, with any administrative rights it holds recorded as an accepted risk.
4. Rate-limited against credential guessing.
5. Recoverable if the remote path fails while the operator is away from the device.

## 2. Scope

**In scope.** Windows 11 Pro, Enterprise, and Education workstations owned and operated by Johnson Technical Systems, accessed remotely by the system owner from outside the premises where the host resides. Covers host configuration, account provisioning, network transport, client configuration, and verification. The mesh VPN in this implementation is Tailscale; the requirements are written so that another mesh VPN with equivalent controls could be substituted.

**Out of scope.** Windows Home editions, which cannot host an RDP session. Domain-joined or Active Directory environments, where these settings are enforced by Group Policy rather than locally. Client-owned or client-managed systems. Third-party remote control software. Physical security of the host, which is addressed separately.

**Assumed environment.** A single-operator business with one workstation, a consumer-grade internet connection, and no on-site IT support. This assumption matters because it removes the option of asking someone to intervene at the keyboard, and several requirements below exist only for that reason.

## 3. Roles and Responsibilities

| Role | Responsibility |
| --- | --- |
| System Owner | Approves this procedure, authorizes who may hold remote access, accepts the residual risks recorded in steps B.2 and C.5, performs the semiannual review |
| System Administrator | Executes the configuration in Sections 6 through 9, maintains the host, holds console-level recovery access |
| Remote User | Connects under the authorized remote account, reports failures, changes host configuration only in the System Administrator role |
| Reviewer | Confirms verification tests in Section 10 were performed and recorded |

In a single-operator business one person holds every role. The separation is retained deliberately. It documents which hat is being worn during each action, and it means the procedure does not need rewriting when a second person is added.

## 4. Definitions

| Term | Definition |
| --- | --- |
| RDP | Remote Desktop Protocol. Microsoft's protocol for interactive remote sessions, listening on TCP and UDP 3389 by default |
| NLA | Network Level Authentication. Requires the connecting user to authenticate before a session is created on the host, rather than presenting a logon screen first |
| Account lockout threshold | The number of failed logon attempts within the observation window after which the account is locked for the lockout duration |
| CGNAT | Carrier-Grade Network Address Translation. An ISP practice of placing subscribers behind a shared public address, meaning the subscriber's router holds no publicly routable IPv4 address |
| Mesh VPN | An overlay network in which enrolled devices authenticate to a coordination service and then exchange encrypted traffic directly with any other device the access rules permit, using outbound connections only |
| Tailnet | Tailscale's name for one organization's private mesh network and its device list, access rules, and settings |
| Overlay address | The stable address assigned to a device by the mesh VPN, independent of its underlying network. Tailscale assigns IPv4 addresses from 100.64.0.0/10 and IPv6 addresses from fd7a:115c:a1e0::/48 |
| DHCP reservation | A router configuration binding a specific hardware (MAC) address to a fixed local IP address |
| Self-signed certificate | A certificate the host generates for itself, trusted by no external authority. Windows uses one for RDP by default |

## 5. Prerequisites

Confirm all of the following before beginning Section 6. Each is a hard prerequisite, not a recommendation.

1. The host runs a supported Pro, Enterprise, or Education edition of Windows 11. Home editions cannot accept incoming RDP sessions.
2. The administrator performing this procedure has local administrator rights on the host and physical or console access to it.
3. The host is mains-powered and will remain powered on.
4. The identity provider account used to sign in to the tailnet, which is also the tailnet administrator account, is protected by multi-factor authentication. This account becomes the outer gate to the host, so it is protected at least as strongly as the host itself.
5. Each client device that will hold a saved connection has full-disk encryption enabled and a screen lock configured.
6. A recovery path exists for the host that does not depend on remote access, such as a second person with physical access, or acceptance of an outage until the operator returns.

## 6. Procedure, Part A: Host Configuration

**A.1 Enable Remote Desktop.** On the host, open Settings, then System, then Remote Desktop. Set the toggle to on.

**A.2 Require Network Level Authentication.** On the same page, expand Remote Desktop and confirm that "Require devices to use Network Level Authentication to connect" is on. Do not disable it. With NLA off, the host builds a session for an unauthenticated connection, which both consumes resources and widens the pre-authentication attack surface.

**A.3 Restrict the RDP firewall rules to the tailnet.** Enabling Remote Desktop turns on the built-in inbound rules in the "Remote Desktop" firewall group. As enabled, they can accept connections from any address on any network profile, including over IPv6. Restrict them so that only overlay addresses can connect. In an elevated PowerShell session:

```
Set-NetFirewallRule -DisplayGroup "Remote Desktop" -RemoteAddress 100.64.0.0/10, fd7a:115c:a1e0::/48
```

With this scope, the network profile of the physical adapter (Public or Private) no longer decides whether RDP is reachable, and a host that receives a global IPv6 address from the ISP does not offer RDP to it.

**A.4 Confirm the firewall scope.** Run the following and confirm that every rule in the group shows the two overlay ranges as its remote address and no wider scope:

```
Get-NetFirewallRule -DisplayGroup "Remote Desktop" | Get-NetFirewallAddressFilter | Format-Table RemoteAddress
```

Re-run this check after any Windows feature update or after toggling Remote Desktop off and on, either of which can reset the rules.

**A.5 Disable sleep and hibernation.** Open Settings, then System, then Power, and set sleep to Never while plugged in. A host that sleeps is unreachable, and waking it remotely requires additional infrastructure on the local network that this procedure does not provide.

**A.6 Record the host name and remote username.** Run `hostname` and record the computer name. Record the exact username the client enters for the remote account designated in step B.1. Do not infer account names from the display name, the profile folder, or an associated email address, as these frequently differ. Running `whoami` while signed in as an account shows the exact `hostname\username` string for that account.

## 7. Procedure, Part B: Account Provisioning

**B.1 Designate the remote account.** Remote access is granted to one named account, the remote account. In this implementation it is the System Owner's daily account. Any other account that could sign in over RDP but is not authorized for remote access is disabled, from an elevated shell:

```
net user <account> /active:no
```

The preferred configuration, used wherever practical, is a remote account that is a standard user. Create it with `net user <remoteaccount> * /add` and add it to the Remote Desktop Users group with `net localgroup "Remote Desktop Users" <remoteaccount> /add`. The `*` makes Windows prompt for the password, so it is not written to the screen or to shell history. Elevation is required for these commands; a non-elevated shell returns `System error 5`.

**B.2 Administrative rights of the remote account, as an accepted risk.** In this implementation the remote account is a member of the Administrators group, and the Administrators group keeps its default right to sign in through Remote Desktop Services. The System Owner accepts this deviation from the preferred configuration so that remote sessions open the owner's own desktop, files, and applications. It is recorded as an accepted risk with these compensating controls:

1. RDP accepts connections only from overlay addresses (step A.3), verified by tests V-1 and V-4.
2. Only approved tailnet devices can reach the host, and the tailnet sign-in requires MFA (Prerequisite 4 and step C.5).
3. NLA authenticates the user before a session is created (step A.2), and account lockout limits password guessing (step B.5).
4. User Account Control remains on. An administrator's applications run with standard user rights until an administrative action is approved at a consent prompt.
5. A separate recovery administrator is kept for console use only (step B.3).

Residual risk: a person who holds both an approved tailnet device and the remote account's password gains full administrative control of the host, with UAC presenting a consent prompt rather than a second password. The System Owner reviews this acceptance at each semiannual review, and whenever a second person is given remote access.

**B.3 Keep a recovery administrator, and keep it off RDP.** A second local administrator account exists for recovery at the console, for example if the remote account is locked out or its sign-in fails. It is never used for remote sessions:

1. Create it in an elevated shell with `net user <recoveryadmin> * /add` and `net localgroup Administrators <recoveryadmin> /add`.
2. Stop its password from expiring with `Set-LocalUser -Name <recoveryadmin> -PasswordNeverExpires $true`. A rarely used account whose password expires under the local password policy would fail when it is needed.
3. Sign in with it once at the console to confirm the password, then sign out.
4. Deny it remote sign-in. In Local Security Policy (`secpol.msc`), go to Local Policies, then User Rights Assignment, open "Deny log on through Remote Desktop Services", and add the account. This setting takes precedence over "Allow log on through Remote Desktop Services".
5. Record a screenshot of both user rights as evidence.

**B.4 Set unique passwords.** The remote account and recovery administrator passwords are each unique and stored in a password manager. Neither is reused from any other service.

**B.5 Record the lockout policy.** Run `net accounts` and record the lockout threshold, lockout duration, and observation window. The threshold must be non-zero. New installations of Windows 11 default to a threshold of 10 attempts, a 10-minute duration, and a 10-minute observation window. Systems upgraded from earlier versions may have no lockout policy at all (a threshold of 0, meaning never), so check the value rather than assuming it. If it is 0, set it in Local Security Policy under Account Policies, then Account Lockout Policy. Retain the output as evidence.

**B.6 Confirm account state.** Run `net user <remoteaccount>` and confirm that `Account active` reads `Yes`. A locked account reads `Locked` in this field, and every logon is rejected while the lockout lasts, even with the correct password. The account unlocks automatically when the lockout duration passes. To unlock it sooner, sign in at the console as an administrator, open Local Users and Groups (`lusrmgr.msc`), open the account's properties, and clear "Account is locked out".

## 8. Procedure, Part C: Network Transport

**C.1 Do not forward TCP 3389.** Forwarding RDP to the public internet is prohibited under this procedure. It is not permitted with a strong password, a non-standard external port, or a source IP restriction. Exposed RDP endpoints are found by automated scanning, and at the Windows default policy an attacker can stay just under the lockout threshold indefinitely: nine guesses every ten minutes is about 1,300 guesses per day against a known account name, without ever triggering a lockout.

**C.2 Confirm no existing exposure.** On the edge router, confirm each of the following and record the result:

1. No port forwarding rule forwards TCP or UDP 3389, or any port, to the host.
2. The host is not in a DMZ.
3. UPnP is disabled, or its active mappings list shows nothing for the host.
4. If the ISP provides IPv6, the router's IPv6 firewall blocks unsolicited inbound connections. IPv6 does not use NAT, so a host with a global IPv6 address is directly addressable unless this firewall blocks it. Step A.3 is the host-side control for the same risk.

**C.3 Assign a stable local address (recommended).** The remote path in this procedure uses only the overlay address, so a stable local address is not required for remote access. It is recommended for local administration and diagnostics. Note the host's IPv4 address and the MAC address of the adapter carrying it, and create a DHCP reservation on the router binding that MAC to that address. Verify the MAC against the correct adapter, as virtualization and container platforms create additional adapters with similar addresses. On a Wi-Fi adapter, turn off random hardware addresses for this network, or the MAC address the router sees will not match the reservation.

**C.4 Install the mesh VPN on the host and run it unattended.** Install Tailscale, sign in to the tailnet, and confirm the host appears in the device list in the admin console. Record the host's overlay address and its MagicDNS name. Turn on unattended mode: right-click the Tailscale icon in the notification area, open Preferences, select Run unattended, and confirm. The equivalent command is `tailscale set --unattended=true`. Without it, Tailscale on Windows runs inside the signed-in user's session, so after a reboot or sign-out the host drops off the tailnet until someone signs in at the keyboard. The Windows account that turns on unattended mode owns the Tailscale configuration on the host.

**C.5 Disable key expiry on the host, as an accepted risk.** Tailscale node keys expire on a fixed schedule, 180 days by default (configurable from 1 to 180 days). When a key expires, connections to and from the device stop until a user re-authenticates on that device. Expiry is disabled per device from the Machines page of the admin console. For an always-on host accessed remotely, disable key expiry on the host only. Leaving it enabled creates a scheduled, unattended loss of access.

Disabling expiry removes a periodic re-authentication control, so the System Owner records it as an accepted risk with these compensating controls in place:

1. MFA on the identity provider account that signs in to and administers the tailnet (Prerequisite 4).
2. Device approval is enabled, so a new device cannot use the tailnet until an administrator approves it.
3. The tailnet access control policy allows only the remote user's enrolled client devices to reach the host, and only on TCP 3389 plus any other port a related procedure requires (SOP-002 uses TCP 443 for Tailscale Serve). The default allow-all policy is removed.
4. Key expiry stays enabled on every client device. Only the host is exempt.
5. The tailnet device list is reviewed at each semiannual review, and a lost or retired device is removed the same day.

**C.6 Confirm outbound-only operation.** No inbound firewall rule or router port forward is required for the mesh VPN. Each device makes outbound HTTPS connections to the coordination service, then connects to its peers directly using NAT traversal. When the NAT on both ends prevents a direct path, traffic is carried by Tailscale's relay servers, still end-to-end encrypted. This is why the design works where the ISP places the subscriber behind CGNAT and no publicly routable IPv4 address exists.

## 9. Procedure, Part D: Client Configuration

**D.1 Enroll the client.** Install Tailscale on the connecting device and sign in to the same tailnet. Approve the device in the admin console and confirm it appears in the device list with key expiry enabled.

**D.2 Configure the connection.** In the RDP client, set the destination to the host's overlay address or MagicDNS name, not its local IP address. The overlay address and MagicDNS name stay the same on every network; the local address does not, and step A.3 blocks it.

**D.3 Authenticate with the recorded username.** Enter the remote account's username exactly as recorded in step A.6.

**D.4 Validate the host certificate on first connection.** Windows warns that the host certificate is not from a trusted certifying authority. This is expected, as the host uses a self-signed certificate. A matching name alone does not prove identity, because anyone can create a self-signed certificate with any name. Before accepting, compare the certificate thumbprint shown by the client with the thumbprint recorded on the host, either in `certlm.msc` under Remote Desktop, then Certificates, or with:

```
Get-ChildItem "Cert:\LocalMachine\Remote Desktop" | Format-List Subject, Thumbprint, NotAfter
```

Accept only if the thumbprints match. Record the thumbprint, and expect the warning again when the certificate is renewed.

**D.5 Enable redirection only as needed.** Drive and clipboard redirection are configured before connecting, under Local Resources in the client. Enable only the drives required. Redirection is suitable for documents and configuration files and unsuitable for bulk transfer over a remote link.

**D.6 Save the connection profile.** Save the configured connection so that redirection settings and the destination address persist.

**D.7 Secure the client.** Confirm the client device has full-disk encryption enabled and locks on sleep. A saved connection profile on an unencrypted, unlocked device is a standing route into the host.

## 10. Verification

All tests are performed at initial implementation and repeated at each semiannual review. Results are recorded with the date and the name of the tester.

| ID | Test | Expected result |
| --- | --- | --- |
| V-1 | From another device on the local network, with Tailscale disconnected on that device, attempt an RDP connection to the host's local IP address | Connection fails. A session or a logon prompt is a finding: step A.3 is not in effect |
| V-2 | Connect using the overlay address while both devices are on the local network | Session established |
| V-3 | Connect using the overlay address with the client on a separate connection, such as cellular data or a tethered hotspot | Session established |
| V-4 | From outside the network, attempt to reach TCP 3389 at the site's public IPv4 address and, if the host has a global IPv6 address, at that address | No response on either. Any response is a finding requiring immediate remediation |
| V-5 | Confirm `net accounts` reports a non-zero lockout threshold | Threshold is configured and recorded |
| V-6 | In the Tailscale admin console, review the device list, device approval setting, and access control policy | Only known devices; key expiry disabled on the host only; device approval on; policy limits access to the host as in step C.5 |

V-3 is the test that proves the remote path works. V-2 succeeds whenever the client shares a network with the host, so it does not distinguish a working remote path from a working local one. V-1 and V-4 prove that the only way in is the overlay.

**Evidence to retain.** Output of `net accounts`, `net user <remoteaccount>`, `net localgroup Administrators`, `net localgroup "Remote Desktop Users"`, and the firewall scope check in step A.4; screenshots of the two Remote Desktop Services user rights (step B.3); a screenshot of the router configuration showing no forwarding rule, DMZ, or UPnP mapping for the host, and the IPv6 firewall setting; screenshots of the tailnet device list, device approval setting, and access control policy; the RDP certificate thumbprint; and a dated record of the six test results.

## 11. Known Failure Modes

Observed during implementation and retained for diagnostic use. The ordering matters: several of these present identically, and the table distinguishes them by what changes rather than by symptom alone.

| Symptom | Cause | Resolution |
| --- | --- | --- |
| Correct credentials rejected, having worked previously | Account locked after reaching the failed-attempt threshold. `net user <account>` reports `Account active: Locked` | Wait for the lockout duration to pass, or unlock at the console in `lusrmgr.msc` (step B.6) |
| Client cannot connect and times out, with Tailscale connected | No firewall rule admits TCP 3389 from the client's address. A blocked connection is dropped before any session starts | Run the check in step A.4 and reapply step A.3 |
| Connection hangs indefinitely at "Securing connection" | RDP negotiating over UDP where that path is partially blocked (SOP-003 Case 2) | On the host, set the policy "Select RDP transport protocols" to "Use only TCP" (Computer Configuration, Administrative Templates, Windows Components, Remote Desktop Services, Remote Desktop Session Host, Connections). This writes `SelectTransport` = 1 under `HKLM\SOFTWARE\Policies\Microsoft\Windows NT\Terminal Services`. Restart the host. TCP-only gives up UDP's performance benefits |
| `System error 5. Access is denied` on a `net user` command | Shell is not elevated. Read operations succeed while writes fail, which masks the cause | Run the shell as administrator. Confirm the title bar reads Administrator and the prompt opens in `system32` |
| Restarting `TermService` fails with the same error | Same cause as above | Elevate the shell |
| Warning that the certificate is not from a trusted certifying authority | Host uses a self-signed RDP certificate | Expected. Compare the thumbprint as in step D.4, then accept |
| New remote account shows an empty desktop with no applications | Windows created a separate user profile for the new account | Expected behaviour, not data loss. The original profile is intact under its own account |
| Host unreachable after a reboot, until someone signs in at the keyboard | Tailscale not in unattended mode | Turn on unattended mode (step C.4) |
| Host unreachable after a router restart by local IP, overlay address still working | Local DHCP lease reassigned | Confirm the DHCP reservation is present and bound to the correct MAC address (step C.3). Remote access is unaffected |

Faults upstream of the host, such as an ISP outage, are diagnosed with SOP-003 Network Troubleshooting Runbook. SOP-003 Case 1 records the ISP outage observed during this implementation.

## 12. Control Mapping

This section connects the procedure to recognized control frameworks. It is what separates a technical runbook from a compliance artifact, and it is the section a client or assessor reads first.

| Framework | Control | Satisfied by |
| --- | --- | --- |
| NIST SP 800-53 Rev. 5 | AC-17 Remote Access | Sections 8 and 9. Remote access is established only over an authenticated, encrypted overlay, with no public listener |
| NIST SP 800-53 Rev. 5 | AC-7 Unsuccessful Logon Attempts | Step B.5. Lockout threshold configured, recorded, and verified at V-5 |
| NIST SP 800-53 Rev. 5 | AC-6 Least Privilege | Partially met. The remote account holds administrative rights as an accepted risk (step B.2). User Account Control runs applications with standard rights until elevation is approved, and the recovery administrator cannot sign in remotely (step B.3) |
| NIST SP 800-53 Rev. 5 | IA-2(1) Multi-factor Authentication to Privileged Accounts | Prerequisite 4. The tailnet administrator account signs in through an identity provider that enforces MFA |
| NIST SP 800-53 Rev. 5 | SC-7 Boundary Protection | Steps A.3, C.1, and C.2. RDP accepts connections only from overlay addresses, and nothing is published at the network edge |
| NIST SP 800-53 Rev. 5 | SC-8 Transmission Confidentiality and Integrity | Section 8. RDP traffic is carried inside the encrypted overlay, and RDP itself uses TLS |
| NIST SP 800-53 Rev. 5 | CM-7 Least Functionality | Steps C.1 and C.2. No inbound port is published to the public internet |
| ISO/IEC 27001:2022 Annex A | A.5.15 Access control | Section 7 |
| ISO/IEC 27001:2022 Annex A | A.6.7 Remote working | Sections 8 and 9 |
| ISO/IEC 27001:2022 Annex A | A.8.2 Privileged access rights | Partially met. Steps B.2 and B.3 |
| ISO/IEC 27001:2022 Annex A | A.8.5 Secure authentication | Steps A.2, B.4, and Prerequisite 4 |
| ISO/IEC 27001:2022 Annex A | A.8.1 User endpoint devices | Prerequisite 5 and step D.7 |
| ISO/IEC 27001:2022 Annex A | A.8.20 Networks security | Steps A.3, C.2, and C.5 |
| CIS Controls v8 | 5.4 Restrict Administrator Privileges to Dedicated Administrator Accounts | Not met for the remote account, which is also the owner's daily account. Recorded as an accepted risk (step B.2) |
| CIS Controls v8 | 6.4 Require MFA for Remote Network Access | Partially met. MFA is required when a device joins the tailnet and when a client's key expires, not at each RDP session (Prerequisite 4, step C.5) |
| CIS Controls v8 | 12.7 Ensure Remote Devices Utilize a VPN and are Connecting to an Enterprise's AAA Infrastructure | Sections 8 and 9 |
| SOC 2 (2017 TSC) | CC6.1 Logical access security | Sections 7 through 9 |
| SOC 2 (2017 TSC) | CC6.6 Protection against threats from outside the system boundary | Steps A.3, C.1, C.2, and tests V-1 and V-4 |

The AICPA criteria have no official short titles; the SOC 2 labels above summarize the criterion text. Mappings are the implementer's assertion of intent. They are not a substitute for an assessor's independent determination, and control identifiers should be re-verified against the current revision of each framework at review.

## 13. Review and Revision History

This procedure is reviewed semiannually, and additionally whenever the host operating system changes major version, the mesh VPN provider changes, the internet service or edge router is replaced, or an access failure occurs that this document does not explain.

| Version | Date | Author | Change |
| --- | --- | --- | --- |
| 0.1 | 2026-09-18 | Johnson Technical Systems | Initial draft, derived from a documented implementation and its observed failure modes. Previously labelled 1.0 |
| 0.2 | 2026-10-03 | Johnson Technical Systems | Recorded key-expiry exemption as an accepted risk with compensating controls (C.5). Moved the ISP outage row to SOP-003. Version renumbered to match Draft status. Changes not yet tested |
| 0.3 | 2026-11-24 | Johnson Technical Systems | Verified against Microsoft and Tailscale documentation and the framework texts. Restricted the RDP firewall rules to overlay addresses (A.3, A.4), replacing the network-profile requirement, and corrected the "Securing connection" failure mode. Recorded remote sign-in with the owner's administrator account as an accepted risk with compensating controls (B.2), and added a recovery administrator denied RDP sign-in (B.3). Corrected lockout behaviour and defaults, and replaced the unlock command with the documented method (B.5, B.6). Added unattended mode (C.4), IPv6 and UPnP checks (C.2, V-4), password entry by prompt (B.1), and a thumbprint check for the host certificate (D.4). Narrowed scope to Windows 11. Corrected the IA-2(1) and CIS titles, added SC-7, A.8.2, and A.8.20, and marked CIS 6.4 as partially met. Removed the milestone row and gave the owner as the LLC's registered name |
| 1.0 | 2026-11-26 | Johnson Technical Systems | Approved by the System Owner. All Section 10 tests (V-1 to V-6) passed on 2026-11-26, and the compensating controls for the accepted risks in steps B.2 and C.5 were confirmed in place. Section 3 updated to cover both risk acceptances |
