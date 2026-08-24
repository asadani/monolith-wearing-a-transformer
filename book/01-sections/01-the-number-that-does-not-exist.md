# Section 1. The number that does not exist

A research report crossed my desk describing a new payments foundation model.
Among its specifications was a latency figure: the model delivers inference
decisions within an ultra-low latency budget of **29 milliseconds**. The figure
appeared four times. Once in the prose. Once in a comparison table, against a
conventional-pipeline baseline of 200 to 800 milliseconds. Twice more in the
sections on serving infrastructure, where it was used to reason about what
hardware such a budget would demand.

Each instance carried a superscript citation marker.

The number does not exist.

Not in the vendor's product page, not in its engineering blog, not in the launch
press release, not in the chief executive's interview with a national
newspaper.<sup class="cite">c-008</sup> Those materials describe the model's
decision speed the way marketing describes speed: "decisions made in
milliseconds" on the product page, "real time" and "instantly" everywhere else.
None of them states a numeric latency figure of any kind. Two targeted searches
turned up nothing further.

The 200-to-800-millisecond baseline it was measured against does not exist
either.

I want to be careful about what I am accusing here, because the interesting part
is not that someone lied. Nobody did. A language model produced a document about
a real system, with real numbers in it, and somewhere in the generation a
plausible latency landed in a slot that wanted one. The citation marker came
along because the surrounding sentences had citation markers. The comparison
table needed a left-hand column, so a range appeared. Everything downstream then
treated it as a specification, including the paragraphs that reasoned about GPU
requirements from it.

That is the failure worth understanding. Not fabrication as an act, but
fabrication as a **shape**: a document that looks cited, reads as technical, and
carries one load-bearing quantity that came from nowhere. The apparatus of rigor
survives intact while the thing it is attached to evaporates.

I checked the number because a verification pass forced me to. Every factual
sentence in this paper is bound to a passage in a source captured to disk, and a
gate refuses to publish when a binding is missing. The 29 milliseconds had no
binding available, which is a different experience from doubting it. I was not
suspicious of the figure. I liked the figure. It was the most concrete thing in
the document.

## Why this opens a paper about architecture

Because the same document, on the strength of numbers assembled that way, made a
recommendation: that payment infrastructure should consolidate its many
task-specific models into a single shared transformer backbone. One model for
routing, fraud, risk, and checkout personalization, learning jointly, serving
every decision in the path.

That is not a small suggestion. It is a proposal to re-couple a system that an
industry spent fifteen years learning to decouple, in the one place where failure
is most expensive, on the authority of a document containing an invented
specification.

The recommendation might still be right. Architecture is not decided by the
provenance of the arguments made for it, and I will spend most of this paper
taking the case seriously. But there is a burden-of-proof question underneath,
and the 29 milliseconds is a useful way in, because it shows how little friction
there now is between *a claim about a system* and *a specification a reader will
design against*.

## What the rest of this paper does

The next section sets out what was actually announced, separated from what was
asserted about it. Then the argument proper: what decoupling was for, why a
shared backbone in the payment path is a single point of failure by
construction, and what the evidence does and does not settle.

The conclusion, stated here so you can disagree with it early: **a domain
foundation model is a strong supporting system and a poor primary one**, and the
distinction is not about model quality. It is about what you can reason about
when it is three in the morning and the thing is wrong.
