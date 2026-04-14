#!/usr/bin/env python3
"""Fetch public PRs and issues from a GitHub account and update the profile README."""

from __future__ import annotations

import json
import os
import re
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

WORK_USERNAME = "jacobokeeffe-ow"
ITEMS_PER_SECTION = 5
README_PATH = Path(__file__).resolve().parent.parent / "README.md"

START_MARKER = "<!-- ACTIVITY:START -->"
END_MARKER = "<!-- ACTIVITY:END -->"


def github_search(query: str, token: str | None = None) -> list[dict]:
    """Run a GitHub Search API query and return the items."""
    url = f"https://api.github.com/search/issues?q={urllib.parse.quote(query)}&sort=updated&per_page={ITEMS_PER_SECTION}"
    req = urllib.request.Request(url)
    req.add_header("Accept", "application/vnd.github+json")
    req.add_header("User-Agent", "okeefj22-profile-readme")
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    with urllib.request.urlopen(req) as resp:
        data = json.loads(resp.read().decode())
    return data.get("items", [])


def format_date(iso_date: str) -> str:
    """Format an ISO date string to 'Mon DD, YYYY'."""
    dt = datetime.fromisoformat(iso_date.replace("Z", "+00:00"))
    return dt.strftime("%b %-d, %Y")


def repo_from_url(html_url: str) -> str:
    """Extract 'owner/repo' from a GitHub HTML URL."""
    parts = html_url.split("/")
    # https://github.com/owner/repo/...
    return f"{parts[3]}/{parts[4]}"


def format_item(item: dict) -> str:
    """Format a single issue or PR as a markdown list entry."""
    title = item["title"]
    url = item["html_url"]
    repo = repo_from_url(url)
    date = format_date(item["created_at"])
    return f"- [{title}]({url}) — *{repo}* ({date})"


def build_activity_section(prs: list[dict], issues: list[dict]) -> str:
    """Build the markdown content for the activity section."""
    lines = []

    if prs:
        lines.append("")
        lines.append("### Pull Requests")
        lines.append("")
        for pr in prs:
            lines.append(format_item(pr))

    if issues:
        lines.append("")
        lines.append("### Issues")
        lines.append("")
        for issue in issues:
            lines.append(format_item(issue))

    now = datetime.now(timezone.utc).strftime("%b %-d, %Y")
    lines.append("")
    lines.append(f"*Last updated: {now}*")
    lines.append("")

    return "\n".join(lines)


def update_readme(activity_md: str) -> bool:
    """Replace content between markers in the README. Returns True if changed."""
    readme = README_PATH.read_text()

    pattern = re.compile(
        rf"({re.escape(START_MARKER)}).*?({re.escape(END_MARKER)})",
        re.DOTALL,
    )
    replacement = rf"\1\n{activity_md}\2"
    new_readme = pattern.sub(replacement, readme)

    if new_readme == readme:
        return False

    README_PATH.write_text(new_readme)
    return True


def main() -> None:
    token = os.environ.get("GITHUB_TOKEN")

    print(f"Fetching public PRs for {WORK_USERNAME}...")
    prs = github_search(f"author:{WORK_USERNAME} is:public type:pr", token)
    print(f"  Found {len(prs)} PRs")

    print(f"Fetching public issues for {WORK_USERNAME}...")
    issues = github_search(f"author:{WORK_USERNAME} is:public type:issue", token)
    print(f"  Found {len(issues)} issues")

    activity_md = build_activity_section(prs, issues)
    changed = update_readme(activity_md)

    if changed:
        print("README.md updated.")
    else:
        print("No changes to README.md.")


if __name__ == "__main__":
    main()
