# -*- coding: utf-8 -*-
"""Claims from the primaries fetched to replace two secondhand attributions.

Both leads resolved, and both changed. The practitioner's rendering of Adyen was
directionally right and imprecise about the failure mode; the Stripe phrase
attributed to Stripe turned out not to be Stripe's. Superseded rows stay in the
ledger with a note, because a record of what a claim used to say is worth having.
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

# --------------------------------------------------------------- Adyen primary
claim("c-025",
      "Adyen reports trying bigger artifacts and complex deep learning models that combine multiple decisions, and finding they would often compromise the engineering requirements - latency and uptime - of online deployments in a critical flow.",
      [qe("s-016", ("bigger artifacts and complex deep learning models", "deep learning models"),
          ("compromise the engineering requirements (latency, uptime)", "in a critical flow."))],
      confidence="moderate",
      notes="SUPERSEDES c-022, which reached this at one remove as 'tried, failed, and will keep trying'. The primary is more specific and more useful: what failed was not accuracy but latency and uptime IN A CRITICAL FLOW, which is precisely the architectural objection. First-party vendor writing, so still T4.")

claim("c-026",
      "Adyen states it continues to investigate that approach and expects to move its whole pipeline to deep learning architectures in the short future.",
      [qe("s-016", ("We do however keep on investigating this line of thinking",
              "line of thinking"),
          ("expecting to move the whole pipeline to deep learning architectures",
           "in the short future"))],
      confidence="moderate",
      notes="THE HONEST OTHER HALF, and it must be carried alongside c-025. Adyen is not a witness against consolidation. It is a witness that consolidation is operationally hard in a critical flow today, while intending to get there. Quoting the first half alone would be the same selective use this paper criticises.")

claim("c-027",
      "Adyen's current architecture is a collection of machine learning models of various natures that share awareness and knowledge, optimized globally toward a shared objective rather than merged into one model.",
      [q("s-016", "consists of a collection of machine learning models of various natures",
         "share awareness and knowledge")],
      confidence="moderate",
      notes="The alternative architecture, evidenced: coordinated specialists with a shared objective, not one backbone. This is the concrete shape of the 'supporting system' position.")

# -------------------------------------------------------------- Stripe primary
claim("c-028",
      "Stripe reports that after deploying its Payments Foundation Model, its detection rate for card-testing attacks on large users increased from 59% to 97% overnight.",
      [q("s-018", "our detection rate for attacks on large users significantly increased",
         "from 59% to 97%")],
      confidence="moderate",
      notes="SUPERSEDES the trade-press version in c-011. First-party, and it states both a baseline and an attack class -- the disclosure Razorpay omits. Vendor-published, so T4.")

claim("c-029",
      "Stripe describes its foundation model as compressing payments into atomic embeddings that it then leverages across multiple use cases, including training classifiers on sequences of those embeddings.",
      [q("s-017", "It also compresses payments into atomic embeddings",
         "training classifiers on sequences of embeddings")],
      confidence="moderate",
      notes="REPLACES c-021, whose 'an addition, not a replacement' was a practitioner's paraphrase and is NOT Stripe's wording -- the word 'replace' does not appear in either Stripe primary. What the primaries do support is architecturally stronger and more precise: the foundation model is a representation layer feeding downstream classifiers, not a decision-maker standing in for them.")

# ----------------------------------------------------------- decoupling rationale
claim("c-030",
      "The bulkhead pattern isolates parts of an application into pools or compartments so that the failure of one component will not cascade to others, named for the watertight sections of a ship's hull.",
      [q("s-019", "for isolating parts of an application into pools or compartments",
         "will not cascade to other components")],
      confidence="low",
      notes="THE SOURCE SECTION 3 NEEDED, and its provenance must be stated in the text. Nygard's Release It! (2007) was NOT obtained; this is an encyclopedia's account of the pattern it introduced. A paper that opens on an invented citation cannot cite a book it has not opened.")

claim("c-031",
      "A shared backbone serving routing, fraud, risk and checkout from one model removes the compartment boundary that the bulkhead pattern exists to create, making its failure a single point of failure by construction rather than by misconfiguration.",
      [q("s-019", "for isolating parts of an application into pools or compartments",
         "will not cascade to other components"),
       qe("s-016", ("compromise the engineering requirements (latency, uptime)",
                    "in a critical flow."))],
      confidence="low",
      notes="THE PAPER'S CENTRAL ARCHITECTURAL CLAIM. It is deduction from a definition plus one practitioner report, not a measurement, and the text must present it that way. Nobody has benchmarked a consolidated payments backbone against a decomposed one in production; if they had, this paper would cite it instead of reasoning.")

with io.open("claims.jsonl", "a", encoding="utf-8", newline="\n") as fh:
    for r in rows:
        fh.write(json.dumps(r, ensure_ascii=False) + "\n")
print("appended %d claims from primaries" % len(rows))
