# -*- coding: utf-8 -*-
"""Append synthesised conclusions to claims.jsonl.

A conclusion is a claim: it binds to source passages like any other row, and its
confidence is the weakest link in its chain rather than the average.
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

claim("c-015",
      "Every performance figure attributed to Vulcan originates with Razorpay, and no independent party has measured the system; the gap is not that the numbers are contradicted but that nothing outside the vendor exists to check them against.",
      [qe("s-001", ("8-10% improvement in success rates", "success rates"),
          ("8X more international card fraud detected", "detected")),
       q("s-006", "enterprises still lack baselines, testing methodology",
         "independent validation needed for assessment")],
      confidence="moderate",
      notes="THE ANSWER TO SUB-QUESTION 1 AND 2. Under the technical lens a vendor benchmark is strong evidence of what the vendor claims and weak evidence of what a buyer will see. There is no T1 or T2 source in this corpus for any Vulcan performance figure, and there cannot be while the model is unrunnable outside Razorpay.")

claim("c-016",
      "The tabular-model literature cited to justify a transformer backbone measures a data regime roughly five orders of magnitude smaller than the system it is used to justify, so it neither supports nor refutes the payments architecture.",
      [q("s-007", "tree-based models remain state-of-the-art on medium-sized data",
         "10K samples)"),
       qe("s-008", ("the majority of this research remains confined to closed environments",
                    "closed environments"),
          ("Can TabPFN v2 maintain good performance in open environments?",
           "in open environments?"))],
      confidence="moderate",
      notes="THE ANSWER TO SUB-QUESTION 3, and it cuts both ways: the GBDT benchmark cannot be used to dismiss Vulcan either. The source documents present the debate as settled in the transformer's favour; the honest position is that nobody has benchmarked this regime in public.")

claim("c-017",
      "The comparator vendor discloses more method than Razorpay does, naming a baseline detection rate and a specific attack class, which is the minimum an outside reader needs to weigh a claim.",
      [qe("s-009", ("a 64% improvement in the rate of detecting card-testing", "card-testing"),
          ("compared to a two-year slog to achieve an 80%", "an 80%")),
       q("s-006", "according to Razorpay, but the baseline has not been released",
         "What was this 8-10% improvement measured against?")],
      confidence="low",
      notes="Both figures are vendor-sourced, so this is a contrast in disclosure rather than in verified performance. Confidence is low because the Stripe figure reaches me through trade press, not from Stripe's own publication.")

claim("c-018",
      "The documents' architectural conclusion rests on an untraceable claim and on evidence from a different class of system, while the one measured comparison in the corpus found modular agentic designs outperforming a monolithic baseline on efficacy and safety.",
      [q("s-011", "agentic architectures outperform base LLMs in repair efficacy",
         "safety (by 17% on average)")],
      stance="mixed", confidence="low", contradicted_by=["s-010"],
      notes="THE ANSWER TO SUB-QUESTION 4. c-014 failed outright, and the evidence that does exist is from network configuration repair, not payments. Marked mixed because the retrieved evidence points against the documents' framing while the vendor commentary they cite points for it, and neither is about a transactional foundation model.")

with io.open("claims.jsonl", "a", encoding="utf-8", newline="\n") as fh:
    for r in rows:
        fh.write(json.dumps(r, ensure_ascii=False) + "\n")
print("appended %d conclusions" % len(rows))
