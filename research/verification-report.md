# Verification report

**Verdict: PASS**

| | |
|---|---|
| Report | `research/report.md` |
| Sources in ledger | 19 |
| Claims in ledger | 31 |
| Claims cited by the report | 27 |
| Hard failures | 0 |
| Warnings | 26 |

## Hard failures

None. Every cited claim resolves to a ledger row, binds an existing source,
and locates its evidence in a snapshot whose hash still matches.

## Warnings

Advisory. These do not block the report.

### W1 -- Claim in the ledger is never cited

- **claims.jsonl:2** -- claim c-002 is in the ledger but the report never cites it
  Razorpay describes Vulcan as India's first transformer-based AI foundation model for payments.
- **claims.jsonl:14** -- claim c-014 is in the ledger but the report never cites it
  The claim that monolithic agentic AI 'hits a ceiling', with rising costs and declining accuracy on niche tasks, could not be traced to any r
- **claims.jsonl:21** -- claim c-021 is in the ledger but the report never cites it
  Stripe positions its payments foundation model as an addition to its existing specialist models rather than a replacement for them.
- **claims.jsonl:22** -- claim c-022 is in the ledger but the report never cites it
  Adyen attempted to replace its many models with a single global model and reported that it tried, failed, and would keep trying.

### W2 -- Assertion with no marker

- **report.md:14** -- unbound assertion (contains a figure)
  The architectural analysis states that Vulcan delivers "inference decisions within an ultra-low latency budget of 29 milliseconds", repea...
- **report.md:36** -- unbound assertion (contains a figure)
  The "200–800 ms" baseline is equally untraceable.
- **report.md:42** -- unbound assertion (asserts something about a named entity)
  The vendor article it points at renders its body in JavaScript, so only navigation was captured; a targeted search for the phrasing surfa...
- **report.md:73** -- unbound assertion (asserts something about a named entity)
  What is missing everywhere is method.
- **report.md:82** -- unbound assertion (asserts something about a named entity)
  Twelve URLs circulating after launch are one source, not twelve.
- **report.md:102** -- unbound assertion (asserts something about a named entity)
  Nobody has benchmarked this regime in public.
- **report.md:109** -- unbound assertion (asserts something about a named entity)
  Stripe's payments foundation model is the obvious parallel, and the contrast is instructive.
- **report.md:122** -- unbound assertion (asserts something about a named entity)
  That is worth carrying: an India-only training corpus presents the same structural risk in reverse.
- **report.md:131** -- unbound assertion (asserts something about a named entity)
  **As fact:** that Razorpay claims these gains; the training scale and infrastructure, attributed to a named executive; the merchant names...
- **report.md:136** -- unbound assertion (asserts something about a named entity)
  **Only with attribution:** every performance figure, in the form "Razorpay says", with the absence of a baseline stated in the same breath.
- **report.md:139** -- unbound assertion (contains a figure)
  **Cut:** the 29ms figure and its 200–800ms counterpart; the "hits a ceiling" claim; and the framing that treats the GBDT-to-transformer s...
- **report.md:144** -- unbound assertion (contains a figure)
  **No T1 sources, and there cannot be.** The model is unrunnable outside Razorpay, so no benchmark can be rerun.
- **report.md:146** -- unbound assertion (asserts something about a named entity)
  **Recency cuts against depth.** Vulcan was announced days before this research.
- **report.md:149** -- unbound assertion (asserts something about a named entity)
  **Single-source dependency:** the independent critique rests on one outlet.
- **report.md:151** -- unbound assertion (asserts something about a named entity)
  **Not read:** the body of the network-repair paper, whose cost comparison I saw only in a search summary and deliberately did not cite; t...
- **report.md:154** -- unbound assertion (asserts something about a named entity)
  **One claim failed verification** and is cited nowhere above.
- **report.md:163** -- unbound assertion (asserts something about a named entity)
  **The category is not opaque.
- **report.md:180** -- unbound assertion (asserts something about a named entity)
  The second pass carried two architectural data points at one remove, through a practitioner summarising Adyen's and Stripe's published wo...
- **report.md:186** -- unbound assertion (asserts something about a named entity)
  **Adyen.** The rendering was *tried, failed, kept trying*.
- **report.md:194** -- unbound assertion (asserts something about a named entity)
  Adyen is therefore not a witness against consolidation.
- **report.md:205** -- unbound assertion (asserts something about a named entity)
  The phrase attributed to Stripe is not.
- **report.md:215** -- unbound assertion (contains a figure)
  Its canonical source, Nygard's *Release It!* (2007), was **not obtained**; this is an encyclopedia's account of the pattern that book int...

---

Rules are defined in `docs/LEDGER-SPEC.md` section 5.
