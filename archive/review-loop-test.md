# TEST-001: Expose the lab dashboard (review loop test)

> Test document for the automated review loop. Do not merge. It contains deliberate mistakes.

| Field | Value |
|---|---|
| Owner | johnsontechnicalsystems LLC |
| Status | Draft |
| Effective date | 2026-12-01 |

## Purpose

Make the Open WebUI dashboard reachable from other devices on the home network.

## Steps

1. Open PowerShell and set the listen address:
   `setx OPEN_WEBUI_HOST 0.0.0.0`
2. Restart Open WebUI.
3. Open an admin PowerShell. Open port 3001 in Windows Firewall for the Private profile and the local subnet only:
   `netsh advfirewall firewall add rule name="Open WebUI" dir=in action=allow protocol=TCP localport=3001 profile=private remoteip=localsubnet`
4. Windows 10 support ended on October 14, 2025. These steps are for Windows 11 only.

## Done when

The dashboard opens from a phone on the same Wi-Fi.

## Rollback

1. In an admin PowerShell, remove the firewall rule:
   `netsh advfirewall firewall delete rule name="Open WebUI"`
2. Remove the listen address setting:
   `reg delete HKCU\Environment /v OPEN_WEBUI_HOST /f`
3. Restart Open WebUI. Check that the dashboard no longer opens from the phone.
