# The documents under audit

These are **not sources**. They are the inputs this paper examines, and they are
published here so that Section 1's central claim is checkable by anyone who wants
to check it.

| File | What it is |
|---|---|
| `Domain Foundation Models Architectural Analysis.md` | AI-generated architectural analysis. Contains the 29-millisecond inference figure, cited four times, that has no source. |
| `deep-research-report.md` | AI-generated research report on the same subject. |
| `AUDIT.md` | The verification pass over both documents, written before the paper was. |

## Why they are here

Section 1 of the paper asserts that a specific number in these documents — an
"ultra-low latency budget of 29 milliseconds", appearing four times, once in a
comparison table against a 200-to-800ms baseline, each instance carrying a
superscript citation marker — does not appear in any of Razorpay's first-party
materials.

That is a claim about a document. A reader cannot evaluate it without the
document. So the document is here.

The whole verification procedure:

```
grep -noiE "29[[:space:]]*(ms|milliseconds)" "Domain Foundation Models Architectural Analysis.md"
```

Four hits — line 10 in the prose, carrying a superscript citation marker; line 17
in the comparison table, against a `200 – 800 ms` baseline; lines 77 and 102
reasoning about the GPU hardware such a budget would demand. Only one of the four
spells the unit out, which is why a plain `grep -c "29 milliseconds"` finds one
and understates it.

Then search Razorpay's captured first-party materials — `research/snapshots/s-001.txt`,
`s-003.txt`, `s-004.txt` — for any numeric latency figure at all.

## What they are not

They are not evidence for anything the paper argues. Nothing in
`research/claims.jsonl` binds to them. They are the subject, in the way a
retracted paper is the subject of a note about its retraction.

Neither document is presented as the work of any named person or organisation.
Both were machine-generated, and the paper's argument is precisely that this is
no longer visible from the inside of the text.
