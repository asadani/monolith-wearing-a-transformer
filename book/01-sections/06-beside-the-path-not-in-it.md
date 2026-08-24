# Section 6. Beside the path, not in it

Everything so far has been an objection. Objections are cheap, and a paper that
stops at one is asking an engineering organization to do nothing, which is never the
right answer when a technology is this obviously useful.

So here is the position stated constructively.

A payments foundation model is a **strong supporting system and a poor primary
one**. The distinction is not about quality. It is about where in the path the
artifact sits, and what still works when it is wrong.

That sentence needs unpacking into something a team can act on, because "supporting
system" on its own is the kind of phrase everyone agrees with and nobody implements.

## Three places it belongs, and one it does not

**As a representation layer.** This is the highest-value position and the one with
the most evidence behind it. The model learns a compressed encoding of transaction
behavior; downstream task-specific models consume that encoding as features and make
the actual decisions.

Stripe describes exactly this shape. Its foundation model "compresses payments into
atomic embeddings, which we then leverage across multiple card testing use cases,
such as training classifiers on sequences of embeddings."<sup class="cite">c-029</sup>
The foundation model produces representations. Classifiers, plural, consume them and
decide.

I want to flag a correction here rather than bury it, because I made the error this
paper exists to catch. I had originally written that Stripe positions its model as
"an addition, not a replacement" &mdash; a clean, quotable phrase that fit the
argument perfectly. It is not Stripe's phrase. The word *replace* does not appear in
either of Stripe's primary write-ups; the phrasing came from a practitioner's
summary of them, and I repeated it as though it were the company's own. What the
primary sources support is narrower and, as it turns out, architecturally stronger:
not a positioning statement about what the model is *not*, but a description of what
it actually *is* &mdash; a representation layer feeding specialists.

The containment properties follow directly. Each classifier keeps its own owner,
threshold, deployment and rollback. If the embeddings drift, the classifiers can be
retrained or pinned to a previous embedding version independently. The compartment
survives, because the shared thing produces *inputs* rather than *verdicts*.

**As a coordinated peer.** The Adyen shape from Section 4: "a collection of machine
learning models of various natures that share awareness and
knowledge,"<sup class="cite">c-027</sup> optimized toward a global objective. Harder
to build, and it preserves the property that matters &mdash; separate artifacts,
separate deployment, shared purpose.

**Out of the synchronous path entirely.** A large amount of what these models are
genuinely best at does not need to answer in single-digit milliseconds: post-hoc
fraud review, chargeback prediction, merchant risk scoring, dispute triage,
reconciliation anomaly detection, batch retry strategy. In asynchronous positions
the latency and uptime constraints Adyen ran into<sup class="cite">c-025</sup> stop
binding, and a wrong answer is caught by a human or a later pass rather than by a
declined transaction.

**Where it does not belong** is the position the source document recommended: sole
authority over routing, fraud, risk and checkout in the synchronous path, with no
independent fallback for any of them.

## Promotion criteria

A supporting system can earn its way into the critical path. It should have to, and
the bar should be written down before the model is built rather than negotiated
afterwards by whoever is most enthusiastic.

Five conditions. I would not promote without all five, and the third is the one
almost nobody has.

**1. A fallback that is exercised, not documented.** Every decision the model serves
must have a rules-based or simpler-model path that produces an acceptable, if worse,
answer. The fallback must run in production regularly &mdash; a percentage of live
traffic, continuously &mdash; because an untested fallback is a comment in a runbook
and will not work on the night it is needed. This is what makes the failure
containable rather than catastrophic.

**2. Per-decision observability, not per-model.** The model's health must be
measurable separately for each decision it serves: fraud precision, routing success,
risk calibration, conversion. Aggregate model metrics are useless here, because the
failure mode of a shared backbone is one decision degrading while the average holds.

**3. A measured mean time to attribution.** Induce a degradation in a staging
environment carrying replayed production traffic. Measure how long it takes the
on-call rotation to identify the shared backbone as the cause. If that number is
unknown, the organization does not know what an incident costs and is not ready to
take the trade. This is the number Section 5 asked for and nobody publishes.

**4. Independent rollback.** It must be possible to revert one decision path to its
previous behavior without reverting the others. In practice this usually means
versioned embeddings with pinning, since rolling back the backbone itself cannot be
made granular.

**5. Regional and segment validation before scale.** A model trained predominantly
on one market's behavior can skew where regional payment behavior is
under-represented, producing both false positives and
negatives.<sup class="cite">c-012</sup> Cross-border and long-tail segments need
their own operating-point measurements before the model governs them, not after.

## Why the burden of proof runs this way

There is a fair objection to all of the above: it is conservative, it is expensive,
and taken literally it would have blocked most of the good infrastructure of the
last decade.

The response is about **asymmetry of consequence**, and it is the reason this paper
does not generalise beyond its domain.

If a payments foundation model is deployed as a supporting system and turns out to
be excellent, the cost is a slower rollout and some duplicated inference spend. The
organization arrives at the same place, later, having spent more.

If it is deployed as the primary decision-maker and turns out to be subtly wrong,
the cost is money moving incorrectly at the rate of arriving traffic, across four
decision types simultaneously, with attribution slowed by the very correlation that
made the architecture attractive.

Those two errors are not the same size, and where the errors are not the same size,
the burden of proof belongs on the side with the larger one. That is not conservatism
about machine learning. It is the ordinary standard for infrastructure where failure
is expensive, and it is the standard this industry already applies to databases,
ledgers, and settlement systems without anyone finding it controversial.

The model is not the problem. The model is good. The question is only whether it is
load-bearing, and load-bearing is a decision about the building rather than about the
material.
