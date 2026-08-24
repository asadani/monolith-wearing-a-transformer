# Research brief: Domain foundation models in payments

## Question
Do transaction-native foundation models such as Razorpay's Vulcan deliver the
operational gains claimed for them, is there evidence that a shared transformer
backbone beats task-specific models on structured payment data, and does the
monolithic-versus-modular architectural argument in the source documents rest on
anything measurable?

## Decision this feeds
Whether the two documents in this directory can be published as analysis, and at
what strength. Specifically: which numbers may be stated as fact, which must be
attributed to Razorpay as a claim, and whether the architectural conclusion is an
evidenced finding or an essay. Audience is an engineering-leadership readership
that will recognise a vendor benchmark on sight.

## Sub-questions

1. **The Vulcan numbers.** Do the headline figures — 4 billion transactions,
   3 trillion data points, ~3,000 signals, 29ms inference, +8–10% success rate,
   8x international fraud detection, 5x dispute detection — trace to Razorpay's
   own publication? Does any of them state a baseline, a measurement window, or a
   sample of merchants?

2. **Independent corroboration.** Has anyone outside Razorpay measured a payments
   foundation model in production? Stripe's Payments Foundation Model is the
   obvious comparator: what has Stripe actually published, and is its evidence any
   more checkable?

3. **The tabular premise.** Is there peer-reviewed evidence that transformer
   backbones outperform gradient-boosted trees on structured transactional data —
   or does the literature still favour GBDTs? The source documents assert the
   shift as settled and name TabPFN, FT-Transformer and TabICL.

4. **The architecture claim.** What supports "monolithic agentic AI hits a
   ceiling" and the microservices analogy? Is that drawn from evidence about
   transactional foundation models, or from commentary about LLM agents, which is
   a different class of system?

5. **Serving reality.** Is a 29ms end-to-end budget for a transformer at payment
   scale corroborated anywhere, and what would it imply about model size,
   batching, and hardware?

6. **The strongest case against.** What is the best available evidence that this
   architecture underdelivers — GBDTs still winning on tabular benchmarks, foundation
   models failing to transfer, or the operational cost of a shared backbone?

## Out of scope

- **Indian payments regulation** (DPDP, RBI localisation) beyond where it
  constrains where the model may run. It is a compliance question, not an
  architecture one.
- **General LLM agent frameworks** as a subject in their own right. They enter
  only via sub-question 4, where the documents borrow their argument.
- **Other domains** — healthcare, insurance, supply chain. The documents gesture
  at them; the evidence here is payments-specific.
- **Razorpay as a company** — funding, market share, competitive position.
- **Whether "India's first" is true.** A priority claim, cheap to dispute, and it
  changes nothing about whether the architecture works.

## What a good answer looks like

Every number in the source documents sorted into three piles: **stated by
Razorpay** (citable as a claim, with the wording and the absence of method
recorded), **independently corroborated** (citable as fact), and **unsupported**
(cut). Plus a clear verdict on sub-question 3, because the whole architecture
argument rests on transformers being the right tool for tabular data — if the
literature says otherwise, the documents' premise is weaker than they present it.

**What would change the conclusion:** an independent measurement of a payments
foundation model in production — a merchant publishing its own before-and-after,
a regulator's audit, or a reproducible benchmark on transactional data with the
configuration published. Absent that, every performance figure is a vendor claim
about an unrunnable system, and the report must say so in those words.

## Lens
`technical`, 2-year window. T1 is the artifact or a benchmark you could rerun;
T2 is first-party engineering write-ups and independent reproducible benchmarks
that publish method; T3 is practitioner reports with specifics; **T4 is vendor
benchmarks and marketing — which is where every Vulcan performance number starts.**

## Known traps

From the lens: a vendor benchmark is strong evidence of what the vendor claims
and weak evidence of what you will see; "it scales" with no number attached.

Specific to this question:

- Launch-day churn. Vulcan was announced days ago and a dozen outlets restated
  one release. Twelve URLs, one origin.
- NVIDIA and AWS are named partners, not independent validators.
- The source documents' superscript markers point to no bibliography, so an
  apparent citation may resolve to nothing at all.
- Confirmation risk is high in the other direction too: it would be easy to
  dismiss the whole thing as marketing. The tabular-transformer literature is
  real and must be read on its own terms.
