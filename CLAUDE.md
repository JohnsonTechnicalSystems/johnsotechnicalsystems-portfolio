# Instructions for Claude Code

## Commits

- Author commits as `JohnsonTechnicalSystems <johnson.technical.systems@gmail.com>`.
- Write each commit message as a short summary line, then a blank line, then one line on why the change was made.
- End the message with the `Co-Authored-By` trailer. Do not add a `Claude-Session` line.
- Do not rewrite or amend commits that are already pushed.

Example:

```
Add SOP-007 for firewall rule review

Covers the quarterly rule review required by the Security+ Frameworks milestone.

Co-Authored-By: Claude <noreply@anthropic.com>
```

## Pull requests

- Make every change on a new branch. Open it as a pull request against `main` with the label `needs-review`.
- Never push directly to `main`, turn on auto-merge, or merge a pull request yourself.
- If the `needs-review` label cannot be added, stop and report the error. Do not leave the pull request unlabeled.
- The review loop on Lloyd's PC then reviews it and swaps the label to `ai-reviewed`. Lloyd merges.
- Do not change labels after you open the pull request. If you push more commits, tell Lloyd. He re-applies `needs-review` for another pass.
