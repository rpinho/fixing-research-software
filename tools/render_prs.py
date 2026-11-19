"""Render the pull-request tables from tools/prs.tsv and the GitHub API.

Run: python3 tools/render_prs.py [--bio-readme PATH] [--physics-readme PATH]
(set GITHUB_TOKEN: about 3 API calls per PR exceed the unauthenticated limit).

prs.tsv columns: repo, PR number, field, type (bug fix | speedup | tests/CI | tool), one-line description.
Writes the full table, grouped by field, between <!-- auto:prs --> and <!-- /auto --> in README.md.
With --bio-readme it also rewrites the <!-- auto:bio-prs --> block of ai-biology with the biology rows and a
link back here; with --physics-readme it rewrites <!-- auto:physics-prs --> in ai-physics with a link and counts.
Each PR's status is fetched once per run. A failed API call is retried, then the run stops without writing.
"""
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HOME = "https://github.com/rpinho/fixing-research-software"
BOTS = re.compile(r"bot|copilot|reviewer|github-actions|gemini|coderabbit|sourcery|codecov|codspeed|^claude$|^rpinho$", re.I)
TYPES = ("bug fix", "speedup", "tests/CI", "tool")
FIELDS = ("biology", "physics and astronomy", "materials and chemistry", "mathematics", "general tools")


def api(path: str):
    for attempt in range(4):
        req = urllib.request.Request(f"https://api.github.com/{path}")
        req.add_header("Accept", "application/vnd.github+json")
        if os.environ.get("GITHUB_TOKEN"):
            req.add_header("Authorization", f"Bearer {os.environ['GITHUB_TOKEN']}")
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                return json.load(resp)
        except urllib.error.HTTPError as e:
            if e.code < 500 or attempt == 3:
                raise
        except urllib.error.URLError:
            if attempt == 3:
                raise
        time.sleep(5 * (attempt + 1))


def pr_status(repo: str, number: str) -> str:
    pr = api(f"repos/{repo}/pulls/{number}")
    if pr.get("merged_at"):
        return f"merged {pr['merged_at'][:10]}"
    if pr["state"] == "closed":
        return "closed"
    people = [c["user"]["login"] for c in api(f"repos/{repo}/issues/{number}/comments?per_page=100")]
    people += [r["user"]["login"] for r in api(f"repos/{repo}/pulls/{number}/reviews?per_page=100") if r.get("user")]
    replies = sum(1 for login in people if not BOTS.search(login))
    return f"open, {replies} repl{'y' if replies == 1 else 'ies'}" if replies else "open"


def load():
    rows = []
    for line in (ROOT / "tools/prs.tsv").read_text().splitlines():
        if not line.strip() or line.startswith("#"):
            continue
        repo, number, field, kind, desc = line.split("\t")
        if kind not in TYPES or field not in FIELDS:
            raise SystemExit(f"prs.tsv: bad type {kind!r} or field {field!r} for {repo}#{number}")
        rows.append(dict(repo=repo, number=number, field=field, kind=kind, desc=desc))
    for r in rows:
        r["status"] = pr_status(r["repo"], r["number"])
    return rows


def counts(rows) -> str:
    s = [r["status"].split()[0].rstrip(",") for r in rows]
    repos = len({r["repo"] for r in rows})
    return (f"{len(rows)} PR{'s' if len(rows) != 1 else ''} to {repos} repositor{'ies' if repos != 1 else 'y'}: "
            f"{s.count('merged')} merged, {s.count('open')} open, {s.count('closed')} closed.")


def table(rows) -> list:
    out = ["| Repo | PR | Type | What it does | Status |", "| --- | --- | --- | --- | --- |"]
    for r in rows:
        url = f"https://github.com/{r['repo']}/pull/{r['number']}"
        out.append(f"| [{r['repo']}](https://github.com/{r['repo']}) | [#{r['number']}]({url}) | {r['kind']} | {r['desc']} | {r['status']} |")
    return out


def slug(field: str) -> str:
    return re.sub(r"[^a-z0-9 -]", "", field.lower()).replace(" ", "-")


def replace(path: Path, marker: str, body: str) -> None:
    start, end = f"<!-- auto:{marker} -->", "<!-- /auto -->"
    text = path.read_text()
    if start not in text:
        raise SystemExit(f"{path}: missing {start}")
    path.write_text(re.sub(re.escape(start) + r".*?" + re.escape(end), lambda _: f"{start}\n{body}\n{end}", text, flags=re.S))


def main() -> None:
    args = sys.argv[1:]
    rows = load()
    parts = [counts(rows), ""]
    for f in FIELDS:
        sub = [r for r in rows if r["field"] == f]
        if sub:
            parts += [f"### {f[0].upper() + f[1:]}", "", counts(sub), "", *table(sub), ""]
    replace(ROOT / "README.md", "prs", "\n".join(parts).rstrip())
    if "--bio-readme" in args:
        bio = [r for r in rows if r["field"] == "biology"]
        body = [counts(bio), f"All fields, including physics, materials and general tools: [{HOME}]({HOME}#pull-requests).", "", *table(bio)]
        replace(Path(args[args.index("--bio-readme") + 1]), "bio-prs", "\n".join(body))
    if "--physics-readme" in args:
        phys = [r for r in rows if r["field"] == "physics and astronomy"]
        link = f"{HOME}#{slug('physics and astronomy')}"
        replace(Path(args[args.index("--physics-readme") + 1]), "physics-prs",
                f"{counts(phys)} The table is in [fixing-research-software]({link}).")


if __name__ == "__main__":
    main()
