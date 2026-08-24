# -*- coding: utf-8 -*-
"""Claims from the three sources added after the first report: Plaid, Thoughtworks,
and an independent practitioner survey of the category.

These reach the architecture question the first pass could not support. Two of
them arrive at one remove -- a practitioner summarising Adyen's and Stripe's
published work -- and that provenance is recorded on every row, because the
distinction between reading a paper and reading someone's account of it is the
whole point of this ledger.
"""
import io, json

import build_claims as bc

rows = []


def claim(cid, statement, bindings, stance="supported", confidence="moderate",
          verified="pass", contradicted_by=None, notes=None):
    r = {"cid": cid, "statement": statement, "bindings": bindings,
         "stance": stance, "confidence": confidence, "verified": verified}
    if contradicted_by:
        r["contradicted_by"] = contradicted_by
    if notes:
        r["notes"] = notes
    rows.append(r)


q, qe = bc.q, bc.qe

# --------------------------------------------------- disclosure by comparators
claim("c-019",
      "Plaid reports its sequential model preventing 26.5% more dollar value in returns at a fixed 1% action rate, and reducing default risk by 13.6% at a 70% approval rate.",
      [qe("s-012", ("prevented 26.5% more dollar value in returns", "at a fixed 1% action rate"),
          ("reduced the default risk by 13.6% at a 70% approval rate", "approval rate"))],
      confidence="moderate",
      notes="THE DISCLOSURE CONTRAST. Vendor-published like Razorpay's, but both figures name an operating point -- a fixed action rate and a fixed approval rate. Without one, a detection improvement is unreadable, because it can always be bought with false positives. This is precisely what Razorpay's multipliers omit.")

claim("c-020",
      "A consultancy analysis of the category reports conversion uplift of up to 6%, cost reductions of up to 5%, and an 86% reduction in manual risk rules across 60 enterprise pilots.",
      [q("s-013", "conversion uplift of up to 6%", "across 60 enterprise pilots")],
      confidence="low",
      notes="States a sample (60 pilots), which is more than Razorpay offers, but 'up to' reports a ceiling rather than a typical result and the pilots are not identified. Thoughtworks sells delivery consulting into this category.")

# ------------------------------------------- the architecture evidence, at one remove
claim("c-021",
      "Stripe positions its payments foundation model as an addition to its existing specialist models rather than a replacement for them.",
      [q("s-014", "Stripe describes it as an addition, not a replacement",
         "not a replacement")],
      confidence="low",
      notes="SUPERSEDED BY c-029. The phrase is the practitioner's paraphrase, not Stripe's -- 'replace' appears in neither Stripe primary. Kept for the record. Originally filed as: directly supports the supporting-system position, and it comes from the category's most credible builder. AT ONE REMOVE: this is a practitioner's characterisation of Stripe's published work, not Stripe's own words. Obtain Stripe's write-up before this carries weight in print.")

claim("c-022",
      "Adyen attempted to replace its many models with a single global model and reported that it tried, failed, and would keep trying.",
      [q("s-014", "it tried replacing its many models with one global model",
         "tried, failed, and will keep trying")],
      confidence="low",
      notes="SUPERSEDED BY c-025 and c-026. The primary says the failure was latency and uptime in a critical flow, and that Adyen expects to move its whole pipeline to deep learning -- both lost in this rendering. Kept for the record. Originally filed as: the strongest available evidence against the monolith, and it is an admission from a company that attempted it with hundreds of petabytes and its own hardware. AT ONE REMOVE: reported by a practitioner summarising Adyen's published Uplift work. The primary must be obtained before this becomes load-bearing -- it is exactly the kind of secondhand attribution this project exists to catch.")

claim("c-023",
      "Companies in this category have published methods and failures on the public record, which establishes a disclosure norm rather than an industry-wide opacity.",
      [q("s-014", "these companies are putting their methods, and even their failures",
         "on the public record")],
      confidence="low",
      notes="Reframes the critique fairly: the problem is not that transactional foundation models are inherently unverifiable, but that one vendor's disclosure falls below a standard its peers already meet.")

# --------------------------------------------------------------- the conclusion
claim("c-024",
      "Razorpay's disclosure is the outlier in its category rather than the norm: peers state operating points, sample sizes, and in one case a failed attempt, while Razorpay states bare multipliers with no baseline.",
      [qe("s-012", ("prevented 26.5% more dollar value in returns", "at a fixed 1% action rate"),
          ("reduced the default risk by 13.6% at a 70% approval rate", "approval rate")),
       q("s-006", "enterprises still lack baselines, testing methodology",
         "independent validation needed for assessment")],
      confidence="moderate",
      notes="REVISES THE FIRST REPORT. That report treated unverifiability as a property of the category. These three sources show it is not: the comparators disclose operating points and sample sizes. The finding is narrower and harder -- Razorpay is below a bar its peers clear.")

with io.open("claims.jsonl", "a", encoding="utf-8", newline="\n") as fh:
    for r in rows:
        fh.write(json.dumps(r, ensure_ascii=False) + "\n")
print("appended %d claims" % len(rows))
