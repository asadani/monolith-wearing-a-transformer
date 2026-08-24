# Synthesis

18 claims, 17 passing, 1 failed. 11 sources: **no T1, three T2, four T3, four T4.**
That distribution is itself the headline finding and is explained below.

---

## SQ1–2 — The Vulcan numbers, and whether anyone else has checked

**Converged, and the convergence is on absence.** The three headline gains are
real as *claims*: 8–10% success-rate improvement, 5x disputes identified, 8x
international card fraud detected, stated on Razorpay's own page [c-001]. The
training scale — 3 trillion data points over 4 billion payments — is attributed
to Razorpay's chief executive in a named publication [c-003], with H100s and AWS
as the stated infrastructure [c-004]. The named merchants check out [c-007].

What does not exist is any method. Not a baseline, not a window, not a control,
not a confidence interval, in any first-party artifact. The Razorpay engineering
blog — the closest thing to a technical write-up — contains no benchmark, holdout,
test set, precision or recall figure at all.

This is not only my reading. Independent trade analysis reaches it directly:
enterprises "still lack baselines, testing methodology, confidence intervals and
independent validation needed for assessment" [c-005], and the baseline for the
8–10% figure has not been released [c-006].

**Single-source dependency, structurally.** Every performance figure traces to one
origin [c-015]. Twelve URLs circulating after launch are one source. NVIDIA and
AWS are commercial partners in the announcement, not validators.

Confidence: **moderate** on what is claimed, and there is nothing to be confident
*about* on what is delivered.

---

## SQ5 — The 29-millisecond figure

**This is the sharpest finding, and it is about the source documents rather than
about Razorpay.**

The architectural analysis states a 29ms inference budget four times, including
in a comparison table against a "200–800 ms" conventional baseline, each carrying
a superscript citation marker.

No such figure exists in the record. Razorpay's first-party materials describe
decision speed only qualitatively — "Decisions made in milliseconds" on the
product page, "real time" and "instantly" in the blog and release — and **none
states a numeric latency figure of any kind** [c-008]. Two targeted searches
returned nothing either.

An independent auditor working from a fresh context confirmed the absence and
rejected my first wording of it, which had claimed Razorpay describes speed "only
as milliseconds". That was false: the word appears in one artifact of three. The
claim now carries the narrower wording and is bound explicitly to the three
captured artifacts, because an absence claim scoped to "all public materials"
cannot be discharged by three files.

One trap recorded for whoever writes from this: the blog's phrase "at that exact
millisecond" describes how quickly a routing path degrades. It is not a latency
figure and must not be repurposed as one.

**Checked and absent**, with the scope stated.

---

## SQ3 — The tabular premise

**Contested, and both sides are arguing about a different machine.**

The documents present the transformer-over-GBDT shift as settled. The most-cited
benchmark on the other side scopes its finding explicitly to medium-sized data of
around ten thousand samples [c-009]. Vulcan claims four billion transactions.
That is roughly five orders of magnitude.

Meanwhile the leading tabular foundation model's results were established largely
in closed evaluation settings, with open-environment robustness an open question
[c-010].

So the literature neither supports the documents' premise nor refutes it [c-016].
This matters in both directions: it would be just as wrong to wave Grinsztajn at
Vulcan and call the architecture disproven. **Nobody has benchmarked this regime
in public.**

Confidence: **moderate**, and the finding is a scope mismatch rather than a verdict.

---

## SQ4 — The architecture argument

**Weakest part of the documents.** The claim that monolithic agentic AI "hits a
ceiling" with rising costs and declining accuracy on niche tasks is attributed to
"a recent study" and could not be traced to anything retrievable [c-014 — failed].
The vendor article it points at renders its body in JavaScript; only navigation
was captured, and a targeted search surfaced adjacent cost research but nothing
matching.

The one measured comparison in the corpus points the other way: in network
configuration repair, agentic architectures outperformed base models on repair
efficacy by 12% and safety by 17% [c-013]. Different domain, and the cost
comparison that secondary summaries report sits in a paper body I did not read —
so it transfers as a caution, not a refutation [c-018, contested].

The deeper problem is category. The monolith-versus-microservices argument is
borrowed from commentary about LLM agents. A structured-data transformer serving
payment decisions is a different class of system, and the transfer is the
documents' inference, not their source's claim.

---

## The overall answer

**The architecture may well be sound. Nothing in the public record establishes
that it is, and the documents present vendor claims and invented precision as
though it does.**

Three separate problems, in descending order of severity:

1. **Invented precision.** 29ms, stated four times with citation markers, exists
   nowhere. So does its "200–800 ms" counterpart.
2. **Unsupported attribution.** The architectural conclusion's load-bearing claim
   traces to nothing [c-014].
3. **Vendor claims presented as findings.** Real, correctly quoted, and entirely
   unverifiable [c-015].

What can be said with a straight face: Razorpay claims these gains; the training
scale and infrastructure are on the record from a named executive; the comparator
vendor discloses more method than Razorpay does [c-017]; and the tabular
literature is silent on this scale [c-016].

---

## Gaps

**Checked and absent**
- Any numeric latency figure in Razorpay's first-party materials [c-008].
- Any baseline, control or measurement window for the three headline gains.
- Any independent measurement of a payments foundation model in production.
- A retrievable source for the "hits a ceiling" claim [c-014].

**Not checked**
- The body of the network-repair paper, whose cost comparison I saw only in a
  search summary and deliberately did not cite.
- The ACM Computing Surveys tabular survey, which would be the best single
  synthesis of SQ3 but was not retrieved.
- Stripe's own publication of its foundation-model results; the figure here comes
  through trade press.
- Indian payments regulation, LLM agent frameworks, other domains — excluded by
  the brief.

**Unknowable from public sources**
- Vulcan's parameter count, architecture, serving topology and true latency.
- Whether the 8x fraud figure holds false-positive rates constant.
- What the 8–10% was measured against.

## What would change the conclusion

A merchant publishing its own before-and-after; a regulator's audit; or Razorpay
releasing a baseline and an evaluation protocol. Any one of those would move the
performance claims from unverifiable to contestable, which is a large upgrade.

**Which single source, if withdrawn, changes the answer:** s-006. It is the only
independent voice asking the baseline question, and without it the critique rests
on my own reading of an absence.
