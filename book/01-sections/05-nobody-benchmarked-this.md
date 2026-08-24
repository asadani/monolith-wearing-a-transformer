# Section 5. Nobody benchmarked this

Here is the sentence this paper would most like to write, and cannot:

*In a controlled comparison on production payment traffic, a consolidated
transformer backbone serving routing, fraud, risk and checkout was measured against
an equivalent set of task-specific models, and the result was X.*

That study does not exist. Not in a form I could find, not from any of the companies
building these systems, not in the academic literature, and not in the trade
analysis that covers them. The most consequential architectural decision in this
category has no published head-to-head measurement behind it, on either side.

I want to be precise about what kind of absence that is, because the distinction
governs how much weight the rest of this paper can carry. There are three states
that get mistaken for each other constantly:

1. **Checked and absent.** The evidence was looked for and is not there.
2. **Not checked.** Nobody looked, or the search ran out of road.
3. **Unknowable from public sources.** The data exists inside a company and is not
   disclosed.

The consolidated-versus-decomposed comparison is the third. Every company in a
position to run it has run some version of it internally &mdash; you do not deploy
one of these without an A/B test &mdash; and none of them has published the design.
What reaches the outside is the outcome of the winning arm, stated as a product
claim.

## The literature that gets cited instead

When the case for a transformer backbone needs academic support, it reaches for the
tabular deep learning literature, and this is where the argument quietly breaks.

The benchmark most often cited for the opposing position &mdash; that gradient-boosted
trees still beat neural networks on structured data &mdash; scopes its own finding
explicitly. It reports that "tree-based models remain state-of-the-art on
medium-sized data ($\sim$10K samples)."<sup class="cite">c-009</sup> Ten thousand
samples. The parenthesis is the authors' own, in their own abstract, and it is a
scope condition rather than a hedge.

The system under discussion in this paper is trained on four billion payments and
three trillion data points.<sup class="cite">c-003</sup>

That is a gap of roughly five to eight orders of magnitude depending on which
quantity you compare, and it means the literature cited to justify a transformer
backbone measures a data regime so far from the deployment regime that it **neither
supports nor refutes** the payments architecture.<sup class="cite">c-016</sup>

This cuts both ways, and I should be explicit that it does not rescue my position
either. The "trees beat neural nets on tabular data" result is the single most
commonly deployed objection to models like these, and at four billion samples that
result is out of scope. Anyone using it as an argument against a payments foundation
model &mdash; and it gets used that way constantly &mdash; is citing a finding about
ten thousand rows to dispute a system trained on four billion. My argument in
Sections 3 and 4 has to stand on containment, not on accuracy, because the accuracy
literature does not reach.

The other pillar has a similar problem. The leading tabular foundation model's
strong results were established largely in closed evaluation settings, and its
authors state plainly that "the majority of this research remains confined to closed
environments," leaving its robustness in open ones an open
question.<sup class="cite">c-010</sup> A closed evaluation is a benchmark where the
distribution is fixed and known. A payment network is the opposite of that by
definition: adversaries adapt, merchants change mix, issuers change policy, and the
distribution moves because someone is being paid to move it.

## The one measured comparison, and why it is not about payments

There is exactly one study in this corpus that measures a monolithic architecture
against a modular one on the same task. It is in network configuration repair, and
it found that "agentic architectures outperform base LLMs in repair efficacy (by 12%
on average) and safety (by 17% on average)."<sup class="cite">c-013</sup>

That result runs against the consolidation thesis: the decomposed, coordinated
design beat the single-model baseline on both quality and safety. It is also, I must
say clearly, **a different class of system in a different domain**, and I would not
accept it as evidence if it pointed the other way.

I raise it for one reason. The source documents that started this inquiry cited the
monolithic-versus-modular question as settled in favour of consolidation, resting
that on an untraceable claim and on evidence drawn from a different class of system
&mdash; while the one measured comparison actually present in the corpus found
modular designs winning.<sup class="cite">c-018</sup> The evidence on this question
is genuinely mixed and thin. That is the finding. Anyone telling you the direction
is established, in either direction, is telling you about their priors.

## What the vendors have shown, which is not nothing

Set the academic literature aside, because the strongest evidence in this category
is operational and comes from the companies themselves.

Stripe reports that after deploying its payments foundation model, "our detection
rate for attacks on large users significantly increased&mdash;from 59% to
97%"<sup class="cite">c-028</sup> for card-testing attacks. Plaid reports its
sequential model "prevented 26.5% more dollar value in returns at a fixed 1% action
rate."<sup class="cite">c-019</sup> A consultancy analysis of the category reports
conversion uplift of up to 6% and an 86% reduction in manual risk rules across 60
enterprise pilots, though it reports ceilings rather than typical
results.<sup class="cite">c-020</sup>

These are vendor-published and they are real. A jump from 59% to 97% on a named
attack class, against a stated baseline, is a substantial result that no amount of
architectural argument talks away. Something is working.

But notice what none of them measures. Every one is a **capability** result: the
model detects more, prevents more, converts better. Not one is a **containment**
result. None of them reports what happened when the model was wrong, how long
attribution took, what the rollback cost, or how correlated the degradation was
across the decisions it served.

That asymmetry is not a conspiracy. Capability results are what a launch post is
for, and containment results are what a post-incident review is for, and companies
publish the former far more readily than the latter. It does mean the public
evidence base is structurally biased toward the case for consolidation, because the
costs this paper is about are the costs that do not get written up.

## What would settle it

The study is not hard to specify, which is part of why its absence is frustrating.
Take production traffic. Serve one arm from a consolidated backbone and one from
task-specific models with equivalent training data. Report:

- decision quality per task at fixed operating points, not headline multipliers;
- p99 latency under peak load, in the critical flow;
- **mean time to attribution** during an induced degradation &mdash; the number this
  entire paper is really about;
- rollback blast radius, measured in reverted changes rather than minutes;
- correlated-error rate across the four decision types.

Three of those five have never been published by anyone in this category. Until they
are, the architectural argument is settled by whoever writes more confidently, which
is how the document in Section 1 came to recommend re-coupling a payment system on
the authority of a latency figure that did not exist.
