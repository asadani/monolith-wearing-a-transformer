# -*- coding: utf-8 -*-
"""Build claims.jsonl by lifting quote locators straight out of the snapshots.

Quotes are never retyped: each spec names a start and an end anchor and the span
between them is taken verbatim from the snapshot, so a claim cannot drift from
its source. Anchors are matched against an ASCII-flattened copy so they need not
reproduce curly quotes and dashes.
"""
import io, json, re

SNAP = "snapshots/%s.txt"
_PUNCT = {u"‘": "'", u"’": "'", u"“": '"', u"”": '"',
          u"–": "-", u"—": "-", u"−": "-", u" ": " "}


def span(sid, start, end):
    text = io.open(SNAP % sid, encoding="utf-8").read()
    flat = re.sub(r"\s+", " ", text)
    for a, b in _PUNCT.items():
        flat = flat.replace(a, b)
    i = flat.find(start)
    if i < 0:
        raise SystemExit("MISSING START in %s: %r" % (sid, start))
    j = flat.find(end, i)
    if j < 0:
        raise SystemExit("MISSING END in %s: %r" % (sid, end))
    q = flat[i:j + len(end)].strip()
    if len(q.split()) > 25:
        raise SystemExit("TOO LONG (%d words) %s: %r" % (len(q.split()), sid, q))
    return q


def q(sid, a, b):
    return {"sid": sid, "locator": {"kind": "quote", "value": span(sid, a, b)},
            "verified_by": "quote-match"}


def sec(sid, value, evidence):
    return {"sid": sid, "locator": {"kind": "section", "value": value},
            "verified_by": "claim-auditor", "evidence": evidence}


def qe(sid, *pairs):
    parts = [span(sid, a, b) for a, b in pairs]
    v = " ... ".join(parts)
    if len(v.split()) > 25:
        raise SystemExit("TOO LONG elided (%d) %s" % (len(v.split()), sid))
    return {"sid": sid, "locator": {"kind": "quote", "value": v},
            "verified_by": "quote-match"}


C = []


def claim(cid, statement, bindings, stance="supported", confidence="moderate",
          verified="pass", contradicted_by=None, notes=None):
    r = {"cid": cid, "statement": statement, "bindings": bindings,
         "stance": stance, "confidence": confidence, "verified": verified}
    if contradicted_by:
        r["contradicted_by"] = contradicted_by
    if notes:
        r["notes"] = notes
    C.append(r)


# ---------------------------------------------- what Razorpay itself claims
claim("c-001",
      "Razorpay's own product page states three headline gains for Vulcan: an 8-10% improvement in success rates, 5x more disputed transactions identified, and 8x more international card fraud detected.",
      [qe("s-001", ("8-10% improvement in success rates", "success rates"),
          ("5X more disputed transactions identified", "identified"),
          ("8X more international card fraud detected", "detected"))],
      confidence="high",
      notes="First-party marketing. Under the technical lens this is T4: a claim about a system nobody outside Razorpay can run.")

claim("c-002",
      "Razorpay describes Vulcan as India's first transformer-based AI foundation model for payments.",
      [q("s-001", "India's first transformer-based AI Foundation Model", "for Payments")],
      confidence="high",
      notes="Recorded as a claim about priority, which the brief puts out of scope for adjudication.")

claim("c-003",
      "Razorpay's chief executive states that Vulcan was trained on 3 trillion data points collected across 4 billion digital payments.",
      [q("s-002", "Training the model on 3 trillion data points", "4 billion digital payments")],
      confidence="moderate",
      notes="Attributed to Harshil Mathur in a named publication, which is better provenance than an anonymous release, but still the vendor describing its own system.")

claim("c-004",
      "The training and inference hardware is reported as NVIDIA H100 GPUs, with AWS supplying the cloud infrastructure.",
      [q("s-002", "this mostly includes the top-end H100 GPUs", "architectural g")],
      confidence="moderate",
      notes="NVIDIA and AWS are named commercial partners in the launch, so this is not third-party corroboration of anything beyond the hardware itself.")

# ------------------------------------------- the method that is not there
claim("c-005",
      "Independent trade analysis finds that the Vulcan figures come without the baselines, testing methodology, confidence intervals or independent validation an enterprise would need to assess them.",
      [q("s-006", "enterprises still lack baselines, testing methodology",
         "independent validation needed for assessment")],
      confidence="moderate",
      notes="THE CENTRAL FINDING, and it is reached independently rather than only by me. T3 trade press, but specific and named.")

claim("c-006",
      "The baseline for the 8-10% success-rate improvement has not been released, leaving open what the improvement was measured against.",
      [q("s-006", "according to Razorpay, but the baseline has not been released",
         "What was this 8-10% improvement measured against?")],
      confidence="moderate")

claim("c-007",
      "Razorpay names Blinkit, redBus and Bachatt as merchants in the early deployment.",
      [q("s-004", "Blinkit", "Bachatt")],
      confidence="moderate",
      notes="The merchant names check out against the launch release; what is absent is any per-merchant measurement.")

# ------------------------------------------------ the fabricated precision
claim("c-008",
      "Razorpay's first-party Vulcan materials - the product page, the engineering blog and the launch press release - describe decision speed only qualitatively: 'Decisions made in milliseconds' on the product page, and 'real time' or 'instantly' elsewhere. None states a numeric latency figure of any kind, and no 29-millisecond inference budget appears in any of them.",
      [sec("s-001", "the three first-party artifacts captured: s-001, s-003, s-004",
           "No numeric latency figure in any of four snapshots; s-001 says 'Decisions made in milliseconds', s-003/s-004 say 'real time'/'instantly'; '29' absent entirely.")],
      confidence="moderate",
      notes="FIRST WORDING FAILED THE AUDITOR. It said Razorpay describes speed 'only as milliseconds', which is false: that word appears in s-001 alone, while s-003 and s-004 use 'real time' and 'instantly'. It also scoped the absence to 'Razorpay's public materials' and 'no first-party source', which three snapshots cannot discharge. This is the auditor's narrower wording, bound explicitly to the three captured artifacts. Caution recorded by the auditor: s-003's phrase 'at that exact millisecond' describes how fast a routing path degrades, NOT inference latency, and must not be repurposed as a speed claim.")

# ---------------------------------------------- the tabular literature
claim("c-009",
      "The benchmark most often cited for tree-based models beating deep learning scopes its finding to medium-sized data of around ten thousand samples.",
      [q("s-007", "tree-based models remain state-of-the-art on medium-sized data",
         "10K samples)")],
      confidence="high",
      notes="Decisive for scope: this is five orders of magnitude below the 4 billion transactions Vulcan claims, so it neither supports nor refutes the Vulcan architecture. The source documents cite the GBDT-versus-transformer debate as though it settles their case.")

claim("c-010",
      "The leading tabular foundation model's strong results have been established largely in closed evaluation settings, and its robustness in open environments was still an open question as of that evaluation.",
      [qe("s-008", ("the majority of this research remains confined to closed environments",
              "closed environments"),
          ("Can TabPFN v2 maintain good performance in open environments?",
           "in open environments?"))],
      confidence="moderate",
      notes="Disconfirming for the documents' premise that tabular transformers are an established win.")

# ------------------------------------------------------ the comparator
claim("c-011",
      "Stripe's comparable payments foundation model was reported to improve card-testing detection on large businesses by 64% quickly, against a two-year effort to reach an 80% rate.",
      [qe("s-009", ("a 64% improvement in the rate of detecting card-testing",
              "card-testing"),
          ("compared to a two-year slog to achieve an 80%", "an 80%"))],
      confidence="low",
      notes="Comparator case. Still a vendor-sourced figure, reported by trade press. Its value here is that Stripe states a baseline and an attack class, which Razorpay does not.")

claim("c-012",
      "An adviser quoted in independent coverage of Stripe's model warns that where regional payment behaviour is under-represented its predictions may skew, producing both false positives and negatives.",
      [q("s-009", "its predictions may be skewed, potentially leading to both false positives",
         "false positives and negatives")],
      confidence="low",
      notes="Named outside expert, not a measurement. Relevant to Vulcan because an India-only training corpus is the same structural risk in reverse.")

# ------------------------------------------------- the architecture claim
claim("c-013",
      "In network configuration repair, agentic architectures outperformed base models on repair efficacy by 12% and on safety by 17% on average.",
      [q("s-011", "agentic architectures outperform base LLMs in repair efficacy",
         "safety (by 17% on average)")],
      confidence="moderate",
      notes="Runs against the documents' framing that modular agentic designs are the compromise option. Different domain, and the cost comparison reported elsewhere is in the paper body which was not read.")

claim("c-014",
      "The claim that monolithic agentic AI 'hits a ceiling', with rising costs and declining accuracy on niche tasks, could not be traced to any retrievable study.",
      [q("s-010", "Beyond Microservices", "Enterprise Architecture")],
      verified="fail", confidence="low",
      notes="FAILED. The source documents attribute this to 'a recent study'. The vendor article they cite renders its body in JavaScript and only navigation was captured; a targeted search for the phrasing returned adjacent cost research but nothing matching. Unsupported as written -- either find the study or drop the sentence.")

# Guarded: build_conclusions and build_additions import this module for its
# quote helpers. Without the guard that import re-runs the write and silently
# truncates claims.jsonl back to the base set, dropping everything appended.
if __name__ == "__main__":
    with io.open("claims.jsonl", "w", encoding="utf-8", newline="\n") as fh:
        for r in C:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")
    print("wrote %d claims" % len(C))
