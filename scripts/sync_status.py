"""Keep every list of SOP statuses in step with the SOPs themselves.

Each SOP in docs/sops/ is the source of truth for its own Version and Status
(its Document Control table). This script copies those values into:

  - README.md: the SOP index between the sop-index markers
  - docs/samples.md: the Status column of the sample tables
  - docs/about/review-process.md: the status summary line between the
    sop-status markers

Usage:
  python scripts/sync_status.py           update the files
  python scripts/sync_status.py --check   change nothing; exit 1 if any list
                                          is out of date (used in CI)

Standard library only.
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOPS = ROOT / "docs" / "sops"
README = ROOT / "README.md"
SAMPLES = ROOT / "docs" / "samples.md"
PROCESS = ROOT / "docs" / "about" / "review-process.md"
STATUSES = ("Draft", "Reviewed", "Approved")


def field(text, name):
    # [ \t] rather than \s at line ends: \s would also match the newline.
    m = re.search(rf"^\|[ \t]*{re.escape(name)}[ \t]*\|[ \t]*(.+?)[ \t]*\|[ \t]*$", text, re.M)
    return m.group(1).strip() if m else ""


def read_sops():
    sops = []
    for path in sorted(SOPS.glob("sop-*.md")):
        text = path.read_text(encoding="utf-8")
        title = re.search(r"^# (.+)$", text, re.M).group(1).strip()
        version_cell = field(text, "Version")
        version = re.match(r"[\d.]+", version_cell)
        status = field(text, "Status")
        if not status:
            status = next((s for s in STATUSES if s.lower() in version_cell.lower()), "")
        if not version or status not in STATUSES:
            sys.exit(f"{path.name}: could not read Version/Status "
                     f"(Version='{version_cell}', Status='{status}')")
        sops.append({"id": field(text, "Document ID") or title.split(":")[0],
                     "title": title, "file": path.name,
                     "version": version.group(0), "status": status})
    return sops


def between(text, name, new_body, where):
    start, end = f"<!-- {name}:start -->", f"<!-- {name}:end -->"
    pattern = re.compile(re.escape(start) + r"\n.*?\n" + re.escape(end), re.S)
    if not pattern.search(text):
        sys.exit(f"{where}: markers '{start}' and '{end}' not found")
    # Blank lines keep Markdown lint happy (tables need blank lines around them).
    return pattern.sub(lambda _: f"{start}\n\n{new_body}\n\n{end}", text)


def readme_index(text, sops):
    # Keep each row's Sources cell; the SOP header does not hold it.
    sources = {}
    for line in text.splitlines():
        m = re.match(r"^\| \[(SOP-\d+):.*\|\s*([^|]*?)\s*\|\s*$", line)
        if m:
            sources[m.group(1)] = m.group(2)
    rows = ["| Document | Status | Version | Sources |", "| --- | --- | --- | --- |"]
    for s in sops:
        rows.append(f"| [{s['title']}](docs/sops/{s['file']}) | {s['status']} | "
                    f"{s['version']} | {sources.get(s['id'], 'See the document')} |")
    return between(text, "sop-index", "\n".join(rows), "README.md")


def samples_status(text, sops):
    by_file = {s["file"]: s["status"] for s in sops}

    def fix(m):
        line, file = m.group(0), m.group(1)
        if file not in by_file:
            return line
        return re.sub(r"\|[ \t]*[^|]*?[ \t]*\|[ \t]*$", f"| {by_file[file]} |", line)

    return re.sub(r"^\| \[[^\]]+\]\(sops/([^)]+)\)[^\n]*\|[ \t]*$", fix, text, flags=re.M)


def summary_line(sops):
    groups = {}
    for s in sops:
        groups.setdefault(s["status"], []).append(s["id"])
    parts = []
    for status in ("Approved", "Reviewed", "Draft"):
        ids = groups.get(status)
        if not ids:
            continue
        names = ids[0] if len(ids) == 1 else ", ".join(ids[:-1]) + " and " + ids[-1]
        verb = "is" if len(ids) == 1 else "are"
        label = status if status != "Draft" else ("a Draft" if len(ids) == 1 else "Drafts")
        parts.append(f"{names} {verb} {label}.")
    return "Current status: " + " ".join(parts)


def main():
    check = "--check" in sys.argv
    sops = read_sops()
    changes = {
        README: readme_index,
        SAMPLES: samples_status,
        PROCESS: lambda t, s: between(t, "sop-status", summary_line(s), "review-process.md"),
    }
    stale = []
    for path, update in changes.items():
        old = path.read_text(encoding="utf-8")
        new = update(old, sops)
        if new != old:
            stale.append(path.relative_to(ROOT).as_posix())
            if not check:
                path.write_text(new, encoding="utf-8", newline="\n")
    if check and stale:
        print("SOP status lists are out of date: " + ", ".join(stale))
        print("Run: python scripts/sync_status.py  and commit the result.")
        sys.exit(1)
    print(("Updated: " + ", ".join(stale)) if stale else "SOP status lists are up to date.")


if __name__ == "__main__":
    main()
