# Section 2. What was actually announced

Razorpay, an Indian payments company, announced a transformer-based foundation
model for payments called Vulcan. Stripped of the commentary that accreted around
it within forty-eight hours, here is what the company itself put on the record.

**The gains.** Its product page states three: an 8&ndash;10% improvement in
success rates, five times more disputed transactions identified, and eight times
more international card fraud detected.<sup class="cite">c-001</sup>

**The scale.** Three trillion data points across four billion digital payments,
attributed to the company's chief executive in a newspaper
interview.<sup class="cite">c-003</sup> The training and inference hardware is
reported as NVIDIA H100 GPUs with AWS supplying the cloud
infrastructure.<sup class="cite">c-004</sup>

**The deployments.** Blinkit, redBus and Bachatt are named in the launch
release.<sup class="cite">c-007</sup>

All of that is real, correctly quoted, and worth taking seriously. A company
processing that volume has access to a signal nobody outside it has, and the
architectural idea &mdash; that a shared representation of transaction behavior
could serve routing and fraud and risk at once &mdash; is a genuinely good idea
that several serious engineering organizations are pursuing.

## What is missing is the method

There is no baseline. No measurement window. No control. No confidence interval.
Not in the product page, not in the launch release, and not in the company's own
engineering blog, which contains no benchmark, holdout, test set, precision or
recall figure at all.

This is not only my reading. Independent trade analysis reached it directly,
noting that enterprises "still lack baselines, testing methodology, confidence
intervals and independent validation needed for
assessment,"<sup class="cite">c-005</sup> and that the baseline for the
8&ndash;10% figure has not been released &mdash; leaving open what the
improvement was measured against.<sup class="cite">c-006</sup>

Take the fraud figure, because it is the one that sounds most impressive. Eight
times more international card fraud detected. Against what detection rate?
Measured over what period? And &mdash; the question that decides whether the
number means anything &mdash; at what false-positive rate?

A fraud model can always detect more fraud. Decline everything and you detect all
of it. The only version of that claim which carries information is one that holds
the false-positive rate fixed, and no published Razorpay material does.

## The disclosure bar its peers clear

I originally wrote this section as a criticism of the category. That was wrong,
and three sources corrected it.

**Plaid**, publishing on its own sequential foundation model, states results at
named operating points: 26.5% more dollar value in returns prevented *at a fixed
1% action rate*, and default risk reduced 13.6% *at a 70% approval
rate*.<sup class="cite">c-019</sup> Both are vendor-published, exactly like
Razorpay's. The difference is the clause after the comma. An operating point is
what makes a detection number readable, because it fixes the thing that could
otherwise be traded away to manufacture the headline.

**Stripe**, writing first-hand about its own payments foundation model, names a
baseline and a specific attack class rather than a bare multiplier: "our detection
rate for attacks on large users significantly increased&mdash;from 59% to
97%"<sup class="cite">c-028</sup> for card-testing attacks. Same kind of company,
same kind of announcement, same commercial incentive. The difference is that a
reader can tell what improved and from where.

A consultancy survey of the category reports its figures with a stated sample of
60 enterprise pilots, though it reports ceilings &mdash; "up to" &mdash; rather
than typical results.<sup class="cite">c-020</sup> And practitioners observe that
firms in this space have been putting methods, and failures, on the public
record.<sup class="cite">c-023</sup>

So the honest finding is narrower and harder than the one I first reached.
Transactional foundation models are not inherently unverifiable. **Razorpay's
disclosure sits below a bar its own peers already
clear.**<sup class="cite">c-024</sup>

## Why launch coverage does not help

Something worth noticing about the dozen trade articles that appeared alongside
the announcement: they are one source. Each restates the same release. Counting
them as corroboration is a category error, and NVIDIA and AWS &mdash; both named
commercial partners in the launch &mdash; are participants rather than
validators.

There is also a recency problem that cuts in Razorpay's favor, and it should be
said plainly. The model was announced days before this research. Nothing has had
time to be independently verified. That is an absence of scrutiny, not evidence
of failure, and if a merchant publishes its own before-and-after next quarter,
much of this section becomes obsolete in the best way.
