# -*- coding: utf-8 -*-
"""Generate the report's References section from the ledgers.

Built from sources.jsonl and claims.jsonl rather than written by hand, so the
bibliography cannot drift from what was actually verified. Only claims the report
cites get a definition, in citation order.
"""
import io, json, re

report = io.open("report.md", encoding="utf-8").read()
body = report.split("\n## References", 1)[0].rstrip()

sources = {}
for line in io.open("sources.jsonl", encoding="utf-8"):
    r = json.loads(line)
    sources[r["sid"]] = r

claims = {}
for line in io.open("claims.jsonl", encoding="utf-8"):
    r = json.loads(line)
    claims[r["cid"]] = r

# Citation order, ignoring markers inside footnote definitions.
seen, order = set(), []
for cid in re.findall(r"\[\^(c-\d{3})\]", body):
    if cid not in seen:
        seen.add(cid)
        order.append(cid)

CAVEAT = {"T4": "  **T4 — evidence of what was said, not that it is true.**"}

out = ["", "## References", ""]
for cid in order:
    c = claims[cid]
    out.append("[^%s]: %s" % (cid, c["statement"]))
    for b in c["bindings"]:
        s = sources[b["sid"]]
        loc = b["locator"]
        shown = loc["value"]
        if loc["kind"] == "quote":
            shown = '"%s"' % shown
        out.append("    — *%s*, %s, %s. %s"
                   % (s["title"], s["publisher"], s.get("published") or "n.d.",
                      s.get("url", "")))
        out.append("      [%s] %s: %s" % (s["tier"], loc["kind"], shown))
    if c["stance"] != "supported":
        out.append("    CONTESTED (%s) by: %s"
                   % (c["stance"], ", ".join(c.get("contradicted_by", []))))
    if c.get("notes"):
        out.append("    Note: %s" % c["notes"])
    out.append("")

io.open("report.md", "w", encoding="utf-8", newline="\n").write(
    body + "\n" + "\n".join(out) + "\n")
print("wrote %d reference definitions" % len(order))
