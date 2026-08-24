# -*- coding: utf-8 -*-
"""Assemble book.html.in in the book-forge sheet-oxblood shape.

Drafting source is book/01-sections/*.md. Each becomes a
<section class="sheet chapter">. Citations are authored inline in the markdown
as <sup>c-0NN</sup>; this normalises them to the theme's class and refuses to
build if any points at a claim that is absent from research/claims.jsonl or
marked failed -- which is what keeps the prose and the ledger in step.
"""
import io
import json
import os
import re
import subprocess
import sys

SECDIR = "book/01-sections"
STYLE_BASE = "assets/_base-style.txt"
OUT = "book.html.in"

STANDFIRST = {
    1: "An AI-generated analysis of a payments foundation model, and a "
       "specification cited four times that no first-party material contains.",
    2: "What the company put on the record, what it left out, and the "
       "disclosure bar its own peers already clear.",
    3: "Service boundaries were not fashion. They were an answer to a question "
       "about what happens when one part of a system is wrong.",
    4: "A payments platform at comparable scale attempted the consolidation, "
       "published what broke, and intends to try again.",
    5: "Every published benchmark in this literature stops five orders of "
       "magnitude short of where these systems run.",
    6: "A representation layer feeding specialists, and the five conditions "
       "that should gate anything moving into the path.",
    7: "The evidence that would change this position, named in advance.",
}


def ledger_cids():
    ok, bad = set(), set()
    with io.open("research/claims.jsonl", encoding="utf-8") as fh:
        for line in fh:
            r = json.loads(line)
            (ok if r.get("verified") == "pass" else bad).add(r["cid"])
    return ok, bad


def convert(md_path, n):
    html = subprocess.check_output(
        ["pandoc", md_path, "-f", "markdown", "-t", "html5", "--wrap=preserve"],
        stderr=subprocess.STDOUT).decode("utf-8")

    # inline citations -> the theme's class
    html = re.sub(r'<sup>(c-\d{3})</sup>', r'<sup class="cite">\1</sup>', html)

    m = re.search(r"<h1[^>]*>Section (\d+)\.\s*(.*?)</h1>", html, flags=re.S)
    if not m:
        raise SystemExit("no section heading in %s" % md_path)
    title = m.group(2).strip()

    # section headings become the mono beat rules, before the title is emitted
    # as an h2 -- otherwise the same regex converts the title too
    tail = html[m.end():]
    tail = re.sub(r"<h2[^>]*>(.*?)</h2>",
                  lambda x: '<p class="beat">%s</p>' % x.group(1).strip(),
                  tail, flags=re.S)
    head = ('<p class="chapter-num">%02d</p>\n  <h2>%s</h2>\n'
            '  <p class="standfirst">%s</p>' % (n, title, STANDFIRST[n]))
    html = html[:m.start()] + head + tail

    html = re.sub(r'(<p class="standfirst">.*?</p>\s*)<p>', r'\1<p class="dropcap">',
                  html, count=1, flags=re.S)
    body = "\n  ".join(html.strip().split("\n"))
    return ('<!-- ===== SECTION %02d ===== -->\n'
            '<section class="sheet chapter">\n  %s\n</section>' % (n, body))


def main():
    ok, bad = ledger_cids()
    files = sorted(f for f in os.listdir(SECDIR) if f.endswith(".md"))
    parts, used = [], set()
    for f in files:
        n = int(re.match(r"(\d+)", f).group(1))
        part = convert(os.path.join(SECDIR, f), n)
        used |= set(re.findall(r'<sup class="cite">(c-\d{3})</sup>', part))
        parts.append(part)
        sys.stderr.write("  s%02d %s\n" % (n, f))

    missing = sorted(used - ok)
    if missing:
        raise SystemExit("citations point at claims that are absent or failed: %s"
                         % ", ".join("%s%s" % (c, " (FAILED)" if c in bad else "")
                                     for c in missing))

    style = io.open(STYLE_BASE, encoding="utf-8").read().rstrip()
    style = style.replace("Onboarding Slop — designed edition",
                          "A Monolith Wearing a Transformer — designed edition")
    if not style.endswith("</style>"):
        style += "\n</style>"

    doc = HEAD % style + "\n\n" + "\n\n".join(parts) + "\n\n" + TAIL
    io.open(OUT, "w", encoding="utf-8", newline="\n").write(doc)
    print("wrote %s (%d sections, %d distinct citations)" % (OUT, len(parts), len(used)))


HEAD = """<meta charset="utf-8">
<title>A Monolith Wearing a Transformer</title>
<meta name="author" content="Anuj Sadani">
<meta name="description" content="Whether domain foundation models belong in the critical path of payment infrastructure. 19 captured sources, 31 claims bound to exact quotations.">

<style>
%s

<!-- ============================ COVER ============================ -->
<section class="sheet cover">
  <img src="{{COVER_PAGE_URI}}" alt="Cover: the title A Monolith Wearing a Transformer, subtitled what we un-learned about decoupling, by Anuj Sadani.">
</section>

<!-- ============================ TITLE PAGE ============================ -->
<section class="sheet titlepage">
  <p class="kicker">A verified inquiry &middot; 2026</p>
  <h1>A Monolith<br>Wearing a<br>Transformer</h1>
  <div class="rule"></div>
  <p class="sub">What we un-learned about decoupling.</p>
  <p class="desc">A payments company announced a transformer trained on four
    billion transactions, and proposed that routing, fraud, risk and checkout
    all be served from it. The proposal arrived in a document containing a
    latency specification that does not exist.</p>
  <p class="desc">This paper takes the architecture seriously anyway. It asks
    what service boundaries were for, what a shared backbone in the payment path
    costs when it is wrong, and what the published evidence actually settles &mdash;
    which is less than either side of the argument assumes.</p>
  <p class="desc">The conclusion is not that the model is bad. It is that a
    domain foundation model is a strong supporting system and a poor primary
    one, and that the burden of proof runs the other way in infrastructure where
    failure is expensive.</p>
  <p class="byline">Anuj Sadani
    <small>Every claim bound to a captured source</small>
  </p>
  <p class="entry-links">
    <a class="entry-summary" href="summary/">Short on time? Read the argument in brief &mdash; 5 min</a>
  </p>
  <a class="cover-dl" href="https://ko-fi.com/s/93e24c2638" target="_blank" rel="noopener"><span class="ar">&nearr;</span>&nbsp; Get the typeset PDF on Ko-fi</a>
</section>

<!-- BOOK-FORGE:AFTER-COVER -->"""

TAIL = """<!-- BOOK-FORGE:BEFORE-END -->"""


if __name__ == "__main__":
    main()
