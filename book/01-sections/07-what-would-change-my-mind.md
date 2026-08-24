# Section 7. What would change my mind

A position that cannot be dislodged by evidence is not a position, it is a
preference. So this section names, in advance, what would move mine &mdash; written
before anyone gets the chance to produce it, which is the only time such a list is
worth anything.

## Five things that would change the conclusion

**A published attribution measurement.** If any company operating a consolidated
backbone in the payment path published mean time to attribution during induced
degradation, and it were comparable to a decomposed system's, the containment
argument in Sections 3 and 4 would be substantially weakened. This is the single
piece of evidence that matters most, and its absence is the load-bearing gap in the
whole category. I would rather have this than any accuracy result.

**A production A/B on architecture rather than capability.** Consolidated backbone
against task-specific models, same traffic, same training data, decision quality
reported at fixed operating points, plus latency at p99 and correlated-error rate
across decision types. If consolidation won on quality *and* held on containment,
Section 6's promotion criteria would be the right process arriving at the opposite
answer, and I would accept that.

**Adyen's stated plan working.** Adyen says it expects "to move the whole pipeline
to deep learning architectures in the short future."<sup class="cite">c-026</sup> If
that happens and the company reports the latency and uptime constraints resolved in
a critical flow, the strongest piece of empirical evidence in this paper turns into
evidence for the other side. I have written this paper knowing that the company
whose failed attempt anchors my argument intends to try again, and I would consider
their success a more informative result than my reasoning.

**Regulatory clarity that entangled objectives are acceptable.** A good deal of
Section 4's governance objection assumes that jointly optimizing fraud and conversion
in one representation creates an explainability problem for a declined transaction.
If supervisors examined this arrangement and found it adequate for adverse-action
reasoning, the accountability half of my objection loses most of its force, leaving
only the operational half.

**Cheap, granular rollback.** If versioned representations with per-decision pinning
become standard tooling rather than bespoke engineering, the "unit of reversion is
the whole brain" problem stops being structural and becomes a solved one. Much of
Section 3 is contingent on rollback being coarse. It does not have to stay that way.

## What would not change it

Symmetrically, and more importantly: better headline numbers would not change it.

Another vendor reporting another multiplier &mdash; more fraud caught, more
conversion, higher detection &mdash; is evidence about capability, and this paper has
not disputed capability once. Stripe's move from 59% to 97% on a named attack
class<sup class="cite">c-028</sup> is a genuinely strong result and it is compatible
with every word of my argument, because the argument was never that the model
predicts badly. A capability result cannot answer a containment question, and the
accumulation of capability results does not eventually add up to one.

Nor would an appeal to inevitability. "Everything consolidates eventually" is a
prediction, not a measurement, and it has been right about some layers of the stack
and wrong about others.

## The disclosure point, restated as a request

The finding this research changed its mind on partway through deserves to be the last
substantive thing said, because it is the most actionable.

I began by treating unverifiability as a property of the category &mdash; that
transactional foundation models are inherently unmeasurable from outside. Three
sources corrected that. Plaid states results at fixed operating points, naming the
action rate and the approval rate its numbers hold at.<sup class="cite">c-019</sup>
Stripe names a baseline and a specific attack class.<sup class="cite">c-028</sup>
Adyen published an approach that did not work. Practitioners observe that companies
in this space "are putting their methods, and even their failures, on the public
record."<sup class="cite">c-023</sup>

So the honest, narrower finding is that Razorpay's disclosure sits **below a bar its
own peers already clear**.<sup class="cite">c-024</sup> That is a fixable problem,
and fixing it costs nothing but a clause.

An 8&ndash;10% success-rate improvement, measured against what baseline, over what
window. Eight times more international card fraud detected, at what false-positive
rate. Five times more disputes identified, on what merchant segment. Each of those
is one subordinate clause away from being a number a reader can use, and the company
has the data, because you cannot claim the multiplier without it.

And there is a recency defense that should be granted plainly: the model was
announced days before this research began. Nothing has had time to be independently
verified. That is an absence of scrutiny rather than evidence of failure, and if a
named merchant publishes its own before-and-after next quarter, this paper's second
section becomes obsolete in the best possible way.

## Back to the number

Which returns us to the 29 milliseconds.

It was never the important thing. It was a symptom, and the disease is that the
distance between *a claim about a system* and *a specification a competent reader
will design against* has collapsed to nearly nothing. A document can now be
generated that is fluent, technical, cited in appearance, internally consistent, and
load-bearing on a quantity that came from nowhere &mdash; and the parts of it that
are true make the invented part harder to see, not easier.

The defense is not skepticism, which does not scale and which I did not have. I liked
the figure. It was the most concrete thing in the document. The defense is
mechanical: a rule that a claim without a locator in a captured source does not get
made, applied by something that does not care how good the sentence sounds.

This paper was written under that rule. It has thirty-one claims in its ledger; one
of them failed verification and is therefore cited nowhere in these pages, which is
the system working rather than a defect in it. Two claims I originally wrote were
withdrawn and replaced when I found the primary sources and discovered that the
secondhand renderings had improved on them.

That is what verification actually feels like from the inside. Not catching a liar.
Catching yourself, holding a number you liked, that turned out to have no source.

The architectural argument may be wrong. The containment reasoning in Section 3 is
deduction, its central claim is marked low confidence in the ledger for that reason,
and Section 5 is an admission that the measurement which would settle the question
has never been published by anyone. If someone runs that study and it goes the other
way, this paper was a well-sourced argument for the wrong conclusion.

But it will have been checkable, and the thing it argued against was not.
