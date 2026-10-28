"""Validate the AI for Hobbyists project.

Checks:
- HTML files parse with no unclosed or unexpected tags
- All internal links resolve to existing files
- LICENSE copyright line is exactly "Copyright (c) 2026 Asdale Dynamics, LLC"
- README credits Asdale Dynamics, LLC
- No secrets, API keys, or real personal data in tracked files

Exit code 0 on success, 1 on failure.
"""
import html.parser
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE_DIR = os.path.join(ROOT, "site")
DOCS_DIR = os.path.join(ROOT, "docs")

failures = []


def fail(msg):
    failures.append(msg)
    print("FAIL:", msg)


class HTMLChecker(html.parser.HTMLParser):
    VOID = {
        "area", "base", "br", "col", "embed", "hr", "img", "input",
        "link", "meta", "param", "source", "track", "wbr",
    }

    def __init__(self, name):
        super().__init__()
        self.name = name
        self.stack = []
        self.errors = []

    def handle_starttag(self, tag, attrs):
        if tag not in self.VOID:
            self.stack.append(tag)

    def handle_endtag(self, tag):
        if tag in self.VOID:
            return
        if self.stack and self.stack[-1] == tag:
            self.stack.pop()
        else:
            top = self.stack[-1] if self.stack else None
            self.errors.append(f"unexpected close </{tag}>, stack top {top}")


def check_html():
    print("== HTML structure ==")
    html_files = sorted(f for f in os.listdir(SITE_DIR) if f.endswith(".html"))
    html_files += sorted(
        os.path.join("apps", f)
        for f in os.listdir(os.path.join(SITE_DIR, "apps"))
        if f.endswith(".html")
    )
    # apps may contain nested html; gather recursively
    for dirpath, _, files in os.walk(SITE_DIR):
        for f in files:
            if f.endswith(".html"):
                full = os.path.join(dirpath, f)
                rel = os.path.relpath(full, SITE_DIR)
                if rel in html_files:
                    continue
                html_files.append(rel)

    for rel in sorted(html_files):
        path = os.path.join(SITE_DIR, rel)
        checker = HTMLChecker(rel)
        with open(path, encoding="utf-8") as fh:
            checker.feed(fh.read())
        if checker.stack:
            checker.errors.append(f"unclosed tags at EOF: {checker.stack}")
        if checker.errors:
            for err in checker.errors:
                fail(f"{rel}: {err}")
        else:
            print(f"  OK   {rel}")
    return html_files


def check_internal_links(html_files):
    print("== Internal links ==")
    href_re = re.compile(r'href="([^"]+)"')
    for rel in sorted(html_files):
        path = os.path.join(SITE_DIR, rel)
        base = os.path.dirname(path)
        with open(path, encoding="utf-8") as fh:
            content = fh.read()
        for m in href_re.finditer(content):
            href = m.group(1)
            if href.startswith("#") or href.startswith("http") or href.startswith("mailto:"):
                continue
            # strip fragment/query
            target = href.split("#")[0].split("?")[0]
            if target.startswith("../../LICENSE"):
                continue
            target_path = os.path.normpath(os.path.join(base, target))
            if not os.path.exists(target_path):
                fail(f"{rel}: link to missing file '{href}' -> {target_path}")


def check_license():
    print("== LICENSE ==")
    license_path = os.path.join(ROOT, "LICENSE")
    if not os.path.exists(license_path):
        fail("LICENSE file missing")
        return
    with open(license_path, encoding="utf-8") as fh:
        content = fh.read()
    expected = "Copyright (c) 2026 Asdale Dynamics, LLC"
    if expected not in content:
        fail(f"LICENSE missing exact line: {expected}")
    else:
        print("  OK   LICENSE copyright line present")


def check_readme():
    print("== README ==")
    readme_path = os.path.join(ROOT, "README.md")
    if not os.path.exists(readme_path):
        fail("README.md missing")
        return
    with open(readme_path, encoding="utf-8") as fh:
        content = fh.read()
    if "Asdale Dynamics, LLC" not in content:
        fail("README does not credit Asdale Dynamics, LLC")
    else:
        print("  OK   README credits Asdale Dynamics, LLC")


def scan_secrets():
    print("== Secrets / personal data scan ==")
    patterns = {
        "API key (sk-)": r"sk-[A-Za-z0-9]{20,}",
        "AWS key": r"AKIA[0-9A-Z]{16}",
        "GitHub token": r"ghp_[A-Za-z0-9]{20,}",
        "email address": r"[A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,}",
        "real street address": r"\d+\s+[A-Za-z]+\s+(Street|St|Avenue|Ave|Road|Rd|Drive|Dr|Lane|Ln)",
    }
    text_exts = (".html", ".md", ".js", ".py", ".css", ".txt", ".LICENSE", "")
    for dirpath, _, files in os.walk(ROOT):
        # skip .git
        if ".git" in dirpath.split(os.sep):
            continue
        for f in files:
            path = os.path.join(dirpath, f)
            _, ext = os.path.splitext(f)
            if ext not in text_exts and f != "LICENSE":
                continue
            try:
                with open(path, encoding="utf-8") as fh:
                    content = fh.read()
            except (UnicodeDecodeError, IsADirectoryError):
                continue
            rel = os.path.relpath(path, ROOT)
            for label, pattern in patterns.items():
                for m in re.finditer(pattern, content):
                    line = content[: m.start()].count("\n") + 1
                    # Allow the fictional example address used in privacy teaching
                    if label == "real street address" and "123 Main Street" in m.group(0):
                        continue
                    # Allow the credited author name / site
                    if label == "email address" and "dylanasdale@users.noreply.github.com" in m.group(0):
                        continue
                    fail(f"{rel}:{line} possible {label}: {m.group(0)[:60]}")


def main():
    print("Validating AI for Hobbyists project\n")
    html_files = check_html()
    check_internal_links(html_files)
    check_license()
    check_readme()
    scan_secrets()

    print()
    if failures:
        print(f"VALIDATION FAILED ({len(failures)} issue(s))")
        for f in failures:
            print("  -", f)
        return 1
    print("VALIDATION PASSED")
    return 0


if __name__ == "__main__":
    sys.exit(main())
