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
- The script does not add rows to `docs/samples.md`. When you add an SOP, add its row there by hand first; the script fails until that row exists.

## Pull requests

- Make every change on a new branch. Open it as a pull request against `main` with the label `needs-review`.
- Never push directly to `main`, turn on auto-merge, or merge a pull request yourself.
- If the `needs-review` label cannot be added, stop and report the error. Do not leave the pull request unlabeled.
- The review loop on Lloyd's PC then reviews it and swaps the label to `ai-reviewed`. Lloyd merges.
- Do not change labels after you open the pull request. If you push more commits, tell Lloyd, who re-applies `needs-review` for another pass.
- Do not add a "Generated with Claude Code" line or Claude session links to pull request descriptions or comments.

## Sample pages and their downloads

- Five sample pages are generated, each with its downloads in `docs/downloads/`: the AI use policy, the public security page, the insurance renewal pack, the access control policy and the WISP. The generator is outside this repo, in `Business - Johnson Technical Systems\site-samples\`. Its README says how to run it.
- After every change to one of these samples, re-sync everything that copies it, in the same pull request where possible: change the generator's data (for the WISP, change `upwork-samples/wisp-tax-practice.html`), run the build, and commit the page together with its regenerated downloads. Do not leave a page that differs from its PDF or spreadsheet.
- A build rewrites every sample. Stage and commit only the files for the sample you changed, then run `git restore .` to discard the other regenerated files, and check that `git status` is clean.
- After a WISP change, run the build with `--sync-upwork`. That copies the WISP source to the Upwork folder and exports that folder's PDF again. Because it overwrites the Upwork folder, use the flag only after the WISP pull request has been reviewed, from the branch that holds that reviewed WISP. Do not use it on a branch still waiting for review. Commit the generator's own changes in the `site-samples` repository.
- If you cannot run the build (for example in a cloud session, or when only the page was edited during review), say so in the pull request and tell Lloyd which downloads are now out of date.
- Copies already uploaded to an outside service, such as Upwork, cannot be re-synced from here. Tell Lloyd which ones need uploading again.
