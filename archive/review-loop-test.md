# TEST-001: Expose the lab dashboard (review loop test)

> Test document for the automated review loop. Do not merge. It contains deliberate mistakes.

| Field | Value |
|---|---|
| Owner | Johnson Technical Systems LLC |
| Status | Final |
| Effective date | 2026-12-01 |

## Purpose

Make the Open WebUI dashboard reachable from other devices on the home network.

## Steps

1. Open PowerShell and set the listen address:
   `setx OPEN_WEBUI_HOST 0.0.0.0`
2. Restart Open WebUI.
3. Open port 3001 in Windows Firewall for all profiles:
   `netsh advfirewall firewall add rule name="Open WebUI" dir=in action=allow protocol=TCP localport=3001`
4. Windows 10 is still supported by Microsoft until October 2027, so the same steps work there.

## Done when

The dashboard opens from a phone on the same Wi-Fi.
