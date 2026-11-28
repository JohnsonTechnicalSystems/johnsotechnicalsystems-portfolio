# Instructions for Claude Code

## Commits

- Author commits as `JohnsonTechnicalSystems <johnson.technical.systems@gmail.com>`.
- Write each commit message as a short summary line, then a blank line, then one line on why the change was made.
- End the message with the `Co-Authored-By` trailer. Do not add a `Claude-Session` line.
- Do not rewrite or amend commits that are already pushed.

Example:

```
Add SOP-007 for firewall rule review

Gives small offices a repeatable quarterly review of firewall rules.

Co-Authored-By: Claude <noreply@anthropic.com>
```

## SOP status lists

- Each SOP's Document Control table is the source of truth for its Version and Status.
- After changing an SOP's Version or Status, or adding an SOP, run `python scripts/sync_status.py` and commit the result. It updates the README index, the Status column in `docs/samples.md`, and the status line in `docs/about/review-process.md`. CI fails if they are out of step.

## Pull requests

- Make every change on a new branch. Open it as a pull request against `main` with the label `needs-review`.
- Never push directly to `main`, turn on auto-merge, or merge a pull request yourself.
- If the `needs-review` label cannot be added, stop and report the error. Do not leave the pull request unlabeled.
- The review loop on Lloyd's PC then reviews it and swaps the label to `ai-reviewed`. Lloyd merges.
- Do not change labels after you open the pull request. If you push more commits, tell Lloyd, who re-applies `needs-review` for another pass.
- Do not add a "Generated with Claude Code" line or Claude session links to pull request descriptions or comments.
