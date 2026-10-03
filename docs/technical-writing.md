# Technical Writing

> **Work in progress: every document is a Draft.** Nothing on this site has been verified yet. Commands, steps, and control references have not been checked against primary sources or retested in the lab. Do not rely on any document as authoritative until its status reads Reviewed. See [Review Process](about/review-process.md).

Procedures and runbooks that someone else can follow without calling the author.

## What I write

- Runbooks and troubleshooting guides
- Standard operating procedures and configuration guides
- Knowledge base articles and end-user how-to guides
- Cleanup and restructuring of existing IT documentation

## Start with these

All samples below are Drafts.

| Document | What it shows |
| --- | --- |
| [SOP-003: Network Troubleshooting Runbook](sops/sop-003-network-troubleshooting-runbook.md) | Real incidents written up in a repeatable seven-step case format, including a case where the first fix did not clear the fault |
| [SOP-002: Local LLM Inference Stack](sops/sop-002-local-llm-inference-stack.md) | An operations guide with health checks, a backup and rollback procedure, and a failure-mode table built from observed faults |
| [SOP-004: Cat6 Cable Termination and Testing](sops/sop-004-cat6-termination-and-testing.md) | A short field procedure that turns a cabling standard into numbered steps and a checklist |

## How I write

- **Task first.** Each procedure starts with what it achieves and what it does not cover, then gives numbered steps in the order they are performed.
- **Verification is part of the procedure.** A procedure ends with checks that prove it worked, not with the last configuration step.
- **Failure modes come from real faults.** Symptom, cause, and resolution tables record what actually went wrong, including when an error message pointed at the wrong component.
- **Consistent structure.** Every SOP uses the same [template](templates/sop-template.md), so a reader who has seen one knows where to find everything in the next.
- **Docs as code.** Markdown in Git, changes reviewed through pull requests, and automated checks before publishing.

## In progress

- A before-and-after rewrite of a public vendor knowledge base article, with notes on each editing decision
- A knowledge base article: "Can't connect to a Windows PC with Remote Desktop"
- An end-user guide to setting up multi-factor authentication
