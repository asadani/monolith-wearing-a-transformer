# A Monolith Wearing a Transformer

**What we un-learned about decoupling.**

A payments company announced a transformer trained on four billion transactions,
and a research document proposed that routing, fraud, risk and checkout all be
served from it. That document contained a latency specification that does not
exist.

This paper takes the architecture seriously anyway.

Read it online: **[tech.anujsadani.in/monolith-wearing-a-transformer](https://tech.anujsadani.in/monolith-wearing-a-transformer/)**  
Typeset PDF: **[ko-fi.com/s/93e24c2638](https://ko-fi.com/s/93e24c2638)**

---

## The argument

**A domain foundation model is a strong supporting system and a poor primary
one.** The distinction is not about model quality. It is about where in the path
the artifact sits, and what still works when it is wrong.

Three steps, in order of how well the evidence supports them.

1. **Service boundaries were blast-radius machinery, not fashion.** A shared
   backbone serving routing, fraud, risk and checkout removes the compartment
   boundary the bulkhead pattern exists to create — which makes its failure a
   single point of failure *by construction rather than by misconfiguration*.
   You cannot configure the compartment back. This step is **deduction, not
   measurement**, and it is marked low confidence in the ledger for that reason.

2. **The one company that published an attempt reports it failing on latency and
   uptime, in a critical flow — not on accuracy.** It also says it intends to try
   again. Both halves are in the paper, because quoting the first alone would be
   the same selective reading the paper opens by criticizing.

3. **Nobody has benchmarked the thing being argued about.** No published
   comparison of a consolidated backbone against task-specific models on
   production payment traffic exists, on either side. The academic literature
   reached for instead measures a data regime roughly five orders of magnitude
   smaller than the systems it is used to justify, so it neither supports nor
   refutes them.

The paper ends by naming, in advance, the five findings that would change its
conclusion — and the one kind of result that would not.

---

## What is in here

| Path | What it is |
|---|---|
| `book/01-sections/` | The manuscript, seven sections, markdown |
| `research/` | The evidence: 19 snapshotted sources, 31 claims, the gate's verdict |
| `research/snapshots/` | A saved copy of every source cited, as captured |
| `source-documents/` | The AI-generated documents under audit, and the audit |
| `scripts/port-to-bookforge.py` | Manuscript → `book.html.in`; **refuses to build on a citation to a missing or failed claim** |
| `assets/` | Cover art and the base stylesheet |
| `index.html` | The built edition |

The typeset PDF is not in this repository. It is distributed from
[Ko-fi](https://ko-fi.com/s/93e24c2638). The reading edition above is free and
complete; the PDF is the designed 29-page edition.

---

## How the claims are checked

Every factual sentence carries a marker like <sup>c-025</sup> that resolves to a
row in `research/claims.jsonl`. Each row binds the statement to an exact quotation
in a file under `research/snapshots/`, captured with its SHA-256. A gate refuses
the report when a binding is missing, when a snapshot's hash has changed, or when
a contested finding is presented as settled.

```
python <research-anything>/scripts/verify_claims.py --workspace research
```

Current verdict: **PASS** — 19 sources, 31 claims, 27 cited, 0 hard failures.

**One claim failed verification** (`c-014`) and is therefore cited nowhere in the
paper. That is the system working rather than a defect in it.

### Limitations, stated here rather than buried

- **The architectural evidence is almost entirely T4.** Adyen and Stripe are
  vendors writing about their own systems; the bulkhead pattern is cited from an
  encyclopedia because Michael Nygard's *Release It!* (2007) was **not obtained**.
  Section 3 says so in the text.
- **Two claims changed on contact with their primaries.** An earlier draft carried
  Adyen and Stripe at one remove, through a practitioner's summary. Both were
  replaced, and the summary had improved on both. Notably, "an addition, not a
  replacement" is **not** Stripe's phrase — the word *replace* appears in neither
  Stripe source. Section 6 corrects this in the body rather than quietly.
- **The central architectural claim is reasoning, not evidence.** If someone runs
  the study Section 5 specifies and it goes the other way, this was a well-sourced
  argument for the wrong conclusion.

---

## Building it

Built with [book-forge](https://github.com/asadani/book-forge) — HTML through
headless Chrome, folios stamped with PyMuPDF.

```
python scripts/port-to-bookforge.py    # manuscript -> book.html.in
bf inject                              # front/back matter
bf build                               # -> index.html + PDF, verified
```

---

Copyright © 2026 Anuj Sadani. All rights reserved. See `LICENSE`.

Snapshots under `research/snapshots/` remain the property of the publishers who
wrote them and are kept only as evidence.
