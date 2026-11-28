# TEST-001: Expose the lab dashboard (review loop test)

> Test document for the automated review loop. Do not merge. It contains deliberate mistakes.

| Field | Value |
|---|---|
| Owner | johnsontechnicalsystems LLC |
| Status | Draft |
| Effective date | 2026-12-01 |

## Purpose

Make the Open WebUI dashboard reachable from other devices on the home network.

## Prerequisites

- Windows 11. Windows 10 support ended on October 14, 2025. These steps are for Windows 11 only.
- Run by: the lab owner, signed in with their normal account. That account must be able to open an admin PowerShell.
- The home Wi-Fi or Ethernet network uses the Private profile. Check in PowerShell:
  `Get-NetConnectionProfile | Select-Object InterfaceAlias, NetworkCategory`
  If it shows `Public`, change it in Settings > Network & internet before you start.
- Note the PC's LAN IPv4 address. You use it as `<LAN-IP>` below:
  `Get-NetIPAddress -AddressFamily IPv4 | Select-Object InterfaceAlias, IPAddress`
- Create a backup folder, for example `C:\Backups\TEST-001`.

## Steps

1. Back up first. In an admin PowerShell, export the firewall policy and check the file is not empty:
   `netsh advfirewall export "C:\Backups\TEST-001\firewall-before.wfw"`
   `Get-Item "C:\Backups\TEST-001\firewall-before.wfw" | Select-Object FullName, Length`
   `Length` must be greater than 0.
2. In a normal (not admin) PowerShell, record the current listen address setting. Write the value down, even if it is empty:
   `[Environment]::GetEnvironmentVariable("OPEN_WEBUI_HOST", "User")`
3. In the same normal PowerShell, set the listen address to the PC's LAN IP only. Do not use `0.0.0.0`:
   `setx OPEN_WEBUI_HOST <LAN-IP>`
4. Restart Open WebUI. Then check it listens on the LAN IP and port:
   `Get-NetTCPConnection -LocalPort 3001 -State Listen | Select-Object LocalAddress, LocalPort`
   `LocalAddress` must be `<LAN-IP>`, not `0.0.0.0`.
5. In an admin PowerShell, open port 3001 for the Private profile and the local subnet only. The check stops a duplicate rule:
   `if (-not (Get-NetFirewallRule -DisplayName "Open WebUI LAN (TEST-001)" -ErrorAction SilentlyContinue)) { New-NetFirewallRule -DisplayName "Open WebUI LAN (TEST-001)" -Direction Inbound -Action Allow -Protocol TCP -LocalPort 3001 -Profile Private -RemoteAddress LocalSubnet }`
   Check it exists and is enabled:
   `Get-NetFirewallRule -DisplayName "Open WebUI LAN (TEST-001)" | Select-Object DisplayName, Enabled, Profile`

## Done when

On a phone on the same Wi-Fi, `http://<LAN-IP>:3001` opens the Open WebUI sign-in page.

## Troubleshooting

- Phone cannot connect, and the PC shows the network as `Public`: the rule only applies to Private. Change the profile, then retry.
- Step 4 shows nothing listening: Open WebUI did not pick up the setting or uses another port. Check how Open WebUI is started and which port it uses.
- Step 4 still shows `0.0.0.0`: the setting was not read. `setx` only affects new shells and processes. Close all shells and restart Open WebUI.
- PC is reachable from itself but not from the phone: the router may have client (AP) isolation turned on. Turn it off for the home network, or use a network without it.
- Another program already uses port 3001: `Get-NetTCPConnection -LocalPort 3001` shows the owning process ID. Stop it, or pick another port and use it everywhere in this document.
- A third-party firewall or antivirus is installed: it may block the port even when Windows Firewall allows it. Add the same rule there.

## Rollback

1. In an admin PowerShell, remove the firewall rule and confirm it is gone:
   `Remove-NetFirewallRule -DisplayName "Open WebUI LAN (TEST-001)"`
   `Get-NetFirewallRule -DisplayName "Open WebUI LAN (TEST-001)" -ErrorAction SilentlyContinue`
   The second command must return nothing. If anything else broke, restore the full policy:
   `netsh advfirewall import "C:\Backups\TEST-001\firewall-before.wfw"`
2. In a normal (not admin) PowerShell, as the same user who ran Step 3, remove the listen address setting:
   `[Environment]::SetEnvironmentVariable("OPEN_WEBUI_HOST", $null, "User")`
   `Remove-Item Env:OPEN_WEBUI_HOST -ErrorAction SilentlyContinue`
   If Step 2 recorded an earlier value, set that value back instead.
3. Close all shells and restart Open WebUI. Check that it no longer listens on the LAN IP:
   `Get-NetTCPConnection -LocalPort 3001 -State Listen | Select-Object LocalAddress, LocalPort`
   Then check that the dashboard no longer opens from the phone.
