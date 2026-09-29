# SOP-001: Secure Remote Access to Windows Workstations

| Field | Value |
| --- | --- |
| Document ID | SOP-001 |
| Version | 1.0 |
| Status | Draft |
| Owner | Johnson Technical Systems |
| Milestone | Security+ Frameworks |
| Effective date | 2026-09-18 |
| Next scheduled review | 2027-03-18 |
| Review cycle | Semiannual, or upon material change to the access path |
| Classification | Internal |

## 1. Purpose

This procedure defines the required configuration for remote graphical access to Windows workstations operated by Johnson Technical Systems.

Remote access is the highest-risk access path into any workstation. It authenticates a user who is not physically present, it is reachable by anyone who can route to the host, and it grants a full interactive desktop rather than a scoped set of commands. Remote Desktop Protocol (RDP) in particular is among the most frequently targeted services on the public internet, and unprotected RDP endpoints are routinely discovered by automated scanning within hours of exposure.

This procedure exists to ensure that remote access to a workstation is:

1. Unreachable from the public internet by design, rather than by obscurity.
2. Authenticated before a session is established, not after.
3. Granted through a dedicated, least-privileged account.
4. Rate-limited against credential guessing.
5. Recoverable if the remote path fails while the operator is away from the device.

## 2. Scope

**In scope.** Windows 10 Pro and Windows 11 Pro workstations owned and operated by Johnson Technical Systems, accessed remotely by the system owner from outside the premises where the host resides. Covers host configuration, account provisioning, network transport, client configuration, and verification.

**Out of scope.** Windows Home editions, which cannot host an RDP session. Domain-joined or Active Directory environments, where these settings are enforced by Group Policy rather than locally. Client-owned or client-managed systems. Third-party remote control software. Physical security of the host, which is addressed separately.

**Assumed environment.** A single-operator business with one workstation, a consumer-grade internet connection, and no on-site IT support. This assumption matters because it removes the option of asking someone to intervene at the keyboard, and several requirements below exist only for that reason.

## 3. Roles and Responsibilities

| Role | Responsibility |
| --- | --- |
| System Owner | Approves this procedure, authorizes who may hold remote access, performs the semiannual review |
| System Administrator | Executes the configuration in Sections 6 through 9, maintains the host, holds console-level recovery access |
| Remote User | Connects under the dedicated remote account, reports failures, does not alter host configuration |
| Reviewer | Confirms verification tests in Section 10 were performed and recorded |

In a single-operator business one person holds every role. The separation is retained deliberately. It documents which hat is being worn during each action, and it means the procedure does not need rewriting when a second person is added.

## 4. Definitions

| Term | Definition |
| --- | --- |
| RDP | Remote Desktop Protocol. Microsoft's protocol for interactive remote sessions, listening on TCP and UDP 3389 by default |
| NLA | Network Level Authentication. Requires the connecting user to authenticate before a session is created on the host, rather than presenting a logon screen first |
| Account lockout threshold | The number of consecutive failed logon attempts after which an account is disabled for a set duration |
| CGNAT | Carrier-Grade Network Address Translation. An ISP practice of placing subscribers behind a shared public address, meaning the subscriber's router holds no publicly routable address |
| Mesh VPN | An overlay network in which each enrolled device establishes an authenticated, encrypted connection to every other device in the same tenant, using outbound connections only |
| Overlay address | The stable address assigned to a device by the mesh VPN, independent of its underlying network |
| DHCP reservation | A router configuration binding a specific hardware (MAC) address to a fixed local IP address |
| Self-signed certificate | A certificate the host generates for itself, trusted by no external authority. Windows uses one for RDP by default |

## 5. Prerequisites

Confirm all of the following before beginning Section 6. Each is a hard prerequisite, not a recommendation.

1. The host runs Windows 10 Pro, Windows 11 Pro, or an Enterprise edition. Home editions cannot accept incoming RDP sessions.
2. The administrator performing this procedure has local administrator rights on the host and physical or console access to it.
3. The host is mains-powered and will remain powered on.
4. An identity provider account exists for the mesh VPN tenant, protected by multi-factor authentication. This account becomes the outer gate to the host, so it is protected at least as strongly as the host itself.
5. Each client device that will hold a saved connection has full-disk encryption enabled and a screen lock configured.
6. A recovery path exists for the host that does not depend on remote access, such as a second person with physical access, or acceptance of an outage until the operator returns.

## 6. Procedure, Part A: Host Configuration

**A.1 Enable Remote Desktop.** On the host, open Settings, then System, then Remote Desktop. Set the toggle to on.

**A.2 Require Network Level Authentication.** In the advanced settings under the same page, confirm that NLA is required. Do not disable it. With NLA off, the host builds a session for an unauthenticated connection, which both consumes resources and widens the pre-authentication attack surface.

**A.3 Set the network profile to Private.** Open Settings, then Network and internet, then the active adapter, and set the network profile to Private. The default Windows Firewall rule for RDP is scoped to private networks. A host on a Public profile will accept the connection at the network layer and then silently drop it during session negotiation, which presents as an indefinite hang rather than a clear error.

**A.4 Confirm the firewall scope.** Verify that the inbound Remote Desktop rule remains enabled for the Private profile and disabled for Public. Do not widen it.

**A.5 Disable sleep and hibernation.** Open Settings, then System, then Power, and set sleep to Never while plugged in. A host that sleeps is unreachable, and it cannot be woken from outside the local network.

**A.6 Record the host identity.** Record the computer name and confirm the account name Windows uses internally by running `whoami` in a command prompt. The output is the exact `hostname\username` string the client will require. Do not infer the username from the display name, the profile folder, or the associated email address, as these frequently differ.

## 7. Procedure, Part B: Account Provisioning

**B.1 Create a dedicated remote account.** In an elevated PowerShell or Command Prompt session, create a standard user account used only for remote access:

```
net user <remoteaccount> "<strong unique password>" /add
net localgroup "Remote Desktop Users" <remoteaccount> /add
```

Elevation is required. A non-elevated shell returns `System error 5` on any write operation.

**B.2 Do not grant administrative rights.** Do not add the remote account to the Administrators group. Installation and configuration tasks inside the session will prompt for administrator credentials, which is the intended behaviour and preserves a meaningful privilege boundary.

**B.3 Retain a separate console account.** The primary account used at the physical keyboard remains distinct from the remote account. This is the single most important control in this section for a remote operator. Failed remote logons consume the lockout budget of whichever account they target, and a lockout cannot be cleared remotely. Isolating remote attempts to a dedicated account preserves console access as a recovery path.

**B.4 Set a unique password.** The remote account password is unique to that account and stored in a password manager. It is not reused from any other service.

**B.5 Record the lockout policy.** Run `net accounts` and record the lockout threshold, lockout duration, and observation window. Retain the output as evidence.

**B.6 Confirm account state.** Run `net user <remoteaccount>` and confirm that `Account active` reads `Yes`. If an account has been locked by failed attempts, this field reads `Locked` and every subsequent logon is rejected regardless of whether the password is correct. Clear a lockout from the console with `net user <account> /active:yes` in an elevated session.

## 8. Procedure, Part C: Network Transport

**C.1 Do not forward TCP 3389.** Port forwarding RDP to the public internet is prohibited under this procedure. It is not permitted with a strong password, a non-standard external port, or a source IP restriction. Exposed RDP endpoints are indexed by automated scanning continuously, and a 10-attempt lockout threshold still permits well over a thousand guesses per day against a known account name.

**C.2 Confirm no existing exposure.** On the edge router, review the port forwarding, DMZ, and UPnP configuration and confirm that no rule forwards 3389 or places the host in a DMZ. Record the result.

**C.3 Assign a stable local address.** Note the host's IPv4 address and the MAC address of the adapter carrying it. Create a DHCP reservation on the router binding that MAC to that address. Verify the MAC against the correct adapter, as virtualization and container platforms create additional adapters with similar addresses.

**C.4 Install the mesh VPN on the host.** Install the client, sign in to the organization's tenant, and confirm the host appears in the tenant device list. Record the overlay address assigned to the host.

**C.5 Disable key expiry on the host.** Devices in a mesh VPN tenant are typically issued keys that expire on a fixed schedule. When a key expires, the device leaves the network and requires interactive re-authentication at the console. For an always-on host accessed remotely, disable key expiry. Leaving it enabled creates a scheduled, unattended loss of access.

**C.6 Confirm outbound-only operation.** No inbound firewall rule or router configuration is required for the mesh VPN. Both endpoints establish outbound connections to a coordination service, which is why this design functions where the ISP places the subscriber behind CGNAT and no publicly routable address exists.

## 9. Procedure, Part D: Client Configuration

**D.1 Enroll the client.** Install the mesh VPN client on the connecting device and sign in to the same tenant. Confirm the device appears in the tenant device list.

**D.2 Configure the connection.** In the RDP client, set the destination to the host's overlay address rather than its local IP or hostname. The overlay address is stable across networks; the local address is not, and hostname resolution is unreliable across platforms.

**D.3 Authenticate with the fully qualified account name.** Enter the username in `hostname\username` form as confirmed in step A.6.

**D.4 Validate the host certificate on first connection.** Windows presents a warning that the host certificate is not from a trusted certifying authority. This is expected, as the host uses a self-signed certificate. Before accepting, confirm that the certificate name matches the expected hostname. A mismatch indicates the connection is terminating somewhere other than the intended host and must not be accepted.

**D.5 Enable redirection only as needed.** Drive and clipboard redirection are configured before connecting, under Local Resources in the client. Enable only the drives required. Redirection is suitable for documents and configuration files and unsuitable for bulk transfer over a remote link.

**D.6 Save the connection profile.** Save the configured connection so that redirection settings and the destination address persist.

**D.7 Secure the client.** Confirm the client device has full-disk encryption enabled and locks on sleep. A saved connection profile on an unencrypted, unlocked device is a standing route into the host.

## 10. Verification

All five tests are performed at initial implementation and repeated at each semiannual review. Results are recorded with the date and the name of the tester.

| ID | Test | Expected result |
| --- | --- | --- |
| V-1 | Connect from a client on the same local network, using the host's local IP address | Session established |
| V-2 | Connect using the overlay address while both devices are on the local network | Session established |
| V-3 | Connect using the overlay address with the client on a separate connection, such as cellular data or a tethered hotspot | Session established |
| V-4 | From outside the network, attempt to reach TCP 3389 at the site's public address | No response. Any response is a finding requiring immediate remediation |
| V-5 | Confirm `net accounts` reports a non-zero lockout threshold | Threshold is configured and recorded |

V-3 is the test that proves the control works. V-1 and V-2 succeed whenever the client shares a network with the host, so neither distinguishes a working remote path from a working local one.

**Evidence to retain.** Output of `net accounts` and `net user <remoteaccount>`, a screenshot of the router configuration showing no forwarding rule for 3389, the tenant device list showing enrolled devices with key expiry disabled, and a dated record of the five test results.

## 11. Known Failure Modes

Observed during implementation and retained for diagnostic use. The ordering matters: several of these present identically, and the table distinguishes them by what changes rather than by symptom alone.

| Symptom | Cause | Resolution |
| --- | --- | --- |
| Correct credentials rejected, having worked previously | Account locked after reaching the failed-attempt threshold. `net user <account>` reports `Account active: Locked` | Clear from the console with `net user <account> /active:yes` in an elevated session. Cannot be cleared remotely |
| Connection hangs indefinitely at "Securing connection" | Host network profile set to Public, so the firewall drops the traffic mid-negotiation | Set the network profile to Private |
| Hang persists after the profile change | RDP negotiating over UDP where that path is partially blocked | Force TCP-only transport by setting `SelectTransport` to 1 under the Terminal Services policy key, then reboot or restart the `TermService` service |
| `System error 5. Access is denied` on a `net user` command | Shell is not elevated. Read operations succeed while writes fail, which masks the cause | Run the shell as administrator. Confirm the title bar reads Administrator and the prompt opens in `system32` |
| Restarting `TermService` fails with the same error | Same cause as above | Elevate the shell |
| Warning that the certificate is not from a trusted certifying authority | Host uses a self-signed RDP certificate | Expected. Confirm the certificate name matches the host, then accept |
| New remote account shows an empty desktop with no applications | Windows created a separate user profile for the new account | Expected behaviour, not data loss. The original profile is intact under its own account |
| Host unreachable after a router restart, overlay address still working | Local DHCP lease reassigned | Confirm the DHCP reservation is present and bound to the correct MAC address |
| All devices join Wi-Fi but no traffic passes; router shows PON green, INTERNET red, WAN status unconnected | Upstream session not reissued after a power interruption. Not a local configuration fault | Power cycle the router for a full five minutes. If unresolved, escalate to the ISP, citing PON online with no WAN address |

## 12. Control Mapping

This section connects the procedure to recognized control frameworks. It is what separates a technical runbook from a compliance artifact, and it is the section a client or assessor reads first.

| Framework | Control | Satisfied by |
| --- | --- | --- |
| NIST SP 800-53 Rev 5 | AC-17 Remote Access | Sections 8 and 9. Remote access is established only over an authenticated encrypted overlay, with no public listener |
| NIST SP 800-53 Rev 5 | AC-7 Unsuccessful Logon Attempts | Step B.5. Lockout threshold configured, recorded, and verified at V-5 |
| NIST SP 800-53 Rev 5 | AC-6 Least Privilege | Steps B.1 and B.2. Remote account is a standard user, not an administrator |
| NIST SP 800-53 Rev 5 | IA-2(1) Multi-factor Authentication | Prerequisite 4. The identity provider fronting the overlay network enforces MFA |
| NIST SP 800-53 Rev 5 | SC-8 Transmission Confidentiality and Integrity | Step A.2 and Section 8. NLA plus an encrypted overlay transport |
| NIST SP 800-53 Rev 5 | CM-7 Least Functionality | Steps C.1 and C.2. No inbound listener published to the public internet |
| ISO/IEC 27001:2022 Annex A | A.5.15 Access control | Section 7 |
| ISO/IEC 27001:2022 Annex A | A.6.7 Remote working | Sections 8 and 9 |
| ISO/IEC 27001:2022 Annex A | A.8.5 Secure authentication | Steps A.2, B.4, and Prerequisite 4 |
| ISO/IEC 27001:2022 Annex A | A.8.1 User endpoint devices | Prerequisite 5 and step D.7 |
| CIS Controls v8 | 5.4 Restrict administrator privileges to dedicated accounts | Steps B.2 and B.3 |
| CIS Controls v8 | 6.4 Require MFA for remote network access | Prerequisite 4 |
| CIS Controls v8 | 12.7 Ensure remote devices use a VPN and connect through managed infrastructure | Sections 8 and 9 |
| SOC 2 (TSC 2017) | CC6.1 Logical access security | Sections 7 through 9 |
| SOC 2 (TSC 2017) | CC6.6 Protection against threats from outside the system boundary | Steps C.1, C.2, and test V-4 |

Mappings are the implementer's assertion of intent. They are not a substitute for an assessor's independent determination, and control identifiers should be re-verified against the current revision of each framework at review.

## 13. Review and Revision History

This procedure is reviewed semiannually, and additionally whenever the host operating system changes major version, the mesh VPN provider changes, the internet service or edge router is replaced, or an access failure occurs that this document does not explain.

| Version | Date | Author | Change |
| --- | --- | --- | --- |
| 1.0 | 2026-09-18 | Johnson Technical Systems | Initial issue. Derived from a documented implementation and its observed failure modes |
