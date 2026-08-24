# Section 3. What we un-learned about decoupling

Fifteen years of payment engineering can be summarized as one long argument about
boundaries. Where to put them, what to pay for them, and what breaks when they are
removed. The argument was not about elegance and it was not about fashion, though
both were used as ammunition at various points. It was about a single question that
every senior engineer eventually learns to ask before any other:

*When this part is wrong, what else is wrong?*

That question is the whole of it. Everything the industry built between the
mid-2000s monolith and the service topologies of today &mdash; the circuit
breakers, the timeouts, the bounded contexts, the separate deployment pipelines,
the independent scaling groups, the per-service on-call rotations &mdash; is
machinery for producing a narrow answer to it.

## The pattern has a name

The name is the bulkhead. It is defined as a technique "for isolating parts of an
application into pools or compartments so that failure of one component will not
cascade to other components,"<sup class="cite">c-030</sup> and the metaphor is
naval: a ship's hull is divided into watertight sections so that a breach floods
one compartment rather than the vessel.

I should say where that definition comes from, because this paper opened by
objecting to a citation that pointed at nothing. The pattern's canonical source is
Michael Nygard's *Release It!*, published in 2007. I did not open that book. What I
am citing is an encyclopedia's account of the pattern the book introduced, which is
a weaker citation than the book itself would be, and it is the one I actually have.

The definition is enough for the argument, because the argument turns on a single
word in it: **cascade**. A bulkhead does not prevent failure. Nothing prevents
failure. A bulkhead determines the *extent* of failure &mdash; it converts an
unbounded event into a bounded one. The ship still has a hole in it. It is a hole in
compartment four.

## Blast radius is the entire argument

Once you see boundaries as blast-radius machinery, most of the microservices debate
collapses into something considerably less interesting than it was made to sound.

Service decomposition was never primarily about development velocity, though that
was the pitch on the conference circuit and it is what most organizations bought.
Velocity is a second-order benefit and, for a large number of teams, it never
arrived at all &mdash; distributed systems are harder to change than local ones, and
a great many companies discovered this the expensive way. The durable benefit was
narrower and less exciting: when the fraud scorer degrades, checkout still
completes. When the routing optimizer starts returning nonsense, authorization still
runs on a fallback path. When one model's feature pipeline goes stale, the other
three do not.

That is not a performance property. It is a **containment** property, and it is the
one that determines what three in the morning looks like.

A payment system is unusual in how sharply this matters. Most software fails softly:
a page renders wrong, a report is late, a recommendation is poor. Payment
infrastructure fails in money, in both directions, as fast as traffic arrives, and
it fails while the merchant is watching a real-time dashboard of transactions
not completing. The cost of a failure is not the failure. It is the failure
multiplied by the minutes it takes to work out which component is wrong.

Boundaries are how you divide that multiplication down.

## What a shared backbone does to the boundary

Now put the proposal from Section 1 against that.

One transformer, trained jointly, serving routing, fraud, risk and checkout
personalization. Every decision in the payment path drawing on the same learned
representation of transaction behavior. The efficiency case is real and I do not
want to be cute about it: shared representation genuinely is more sample-efficient,
genuinely does let a signal learned in fraud inform routing, and genuinely does cut
the number of independently maintained feature pipelines from four to one.

The architectural cost is the exact thing the bulkhead was for. A shared backbone
serving all four decisions removes the compartment boundary that separates them,
which makes its failure a single point of failure **by construction rather than by
misconfiguration**.<sup class="cite">c-031</sup>

The distinction between those two phrases is the reason this section exists.

A single point of failure by misconfiguration is a bug. Somebody put the replica in
the same availability zone as the primary; somebody forgot the timeout; somebody
scaled the group down to one. Bugs of that class get found, filed and fixed, and the
architecture is unchanged afterward.

A single point of failure by construction is not a bug. It is the design working as
intended. There is no configuration change that restores the compartment, because
the compartment was traded away deliberately in exchange for the shared
representation. You can add redundancy &mdash; more replicas of the same model, more
regions, faster failover &mdash; and none of it touches the failure mode that
matters here, which is not the model being *down* but the model being *wrong*.

Redundancy protects against a component that has stopped answering. It does nothing
whatsoever against a component that is answering confidently and incorrectly across
every decision it serves. Five replicas of a drifted model produce the same drifted
answer five times, quickly.

## The failure mode that has no page

Consider how each architecture behaves under a subtle degradation &mdash; not an
outage, but a distribution shift that moves the model's calibration.

In the decomposed system, the fraud model's false-positive rate climbs. Somebody
notices, because the fraud model has an owner, a dashboard, a precision metric and
an alert threshold. The routing optimizer is unaffected, because it is a different
model with different inputs. The blast radius is one decision type, one team, one
rollback.

In the consolidated system, the shared representation shifts. Fraud gets worse.
Routing gets worse. Risk gets worse. Checkout personalization gets worse. They get
worse *together*, and correlated degradation across four unrelated metrics is
precisely the signal monitoring is worst at attributing, because every downstream
dashboard moves at once and none of them points at the cause. The first hypothesis
in the incident channel will not be "the backbone drifted." It will be "something is
wrong with traffic," and it will take a while.

Rollback is worse still. In the decomposed system you roll back one model and the
other three keep their current versions. In the consolidated system, rolling back
the backbone reverts every improvement every team shipped through it since the last
known-good checkpoint. The unit of reversion is no longer a change. It is the whole
brain.

## The honest counter-case

There is a real argument on the other side and it deserves stating at full strength,
because a paper that only argues one way is doing the same thing as the document
that started this one.

**Boundaries are not free, and their cost is also paid in incidents.** A decomposed
system has four feature pipelines that can independently go stale, four sets of
training-serving skew, four deployment paths, and a coordination problem whenever a
signal needs to cross a boundary. Distributed systems introduce failure modes that
monoliths simply do not have: partial failure, network partitions, cascading
timeouts, and the delightful class of bug where two services disagree about the
state of the same transaction. Nobody who has operated one believes the boundaries
are pure benefit.

**And "four models" is not four bulkheads.** In most real payment stacks those
models already share a feature store, a streaming platform, an inference cluster and
an identity graph. The compartment walls are thinner than the architecture diagram
suggests. Consolidating the models may remove less isolation than this section
implies, because a good deal of it was already gone.

I accept both points, and they narrow the claim rather than defeat it. Decomposition
is not safe and consolidation is not dangerous; the narrower thing worth saying is
that **consolidation moves a specific, well-understood, containable class of failure
into a class that is none of those things**, and that this trade should be made
deliberately, with the containment cost named, rather than as a side effect of
adopting an architecture because it is the shape of the moment.

Which raises the obvious question, and it is what Section 4 is about: has anyone
actually tried this?
