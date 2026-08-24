# Domain foundation models in payments — verification report

**Verdict: the two documents in this directory should not be published as
analysis without substantial correction. The architecture they describe may well
be sound; nothing in the public record establishes that it is, and the documents
present vendor claims and at least one invented number as though it does.**

Three problems, in descending order of severity.

---

## 1. A number that does not exist

The architectural analysis states that Vulcan delivers "inference decisions within
an ultra-low latency budget of 29 milliseconds", repeats the figure four times,
and places it in a comparison table against a "200–800 ms" conventional baseline.
Each instance carries a superscript citation marker.

**No such figure exists in the record.** Razorpay's first-party materials — the
product page, the engineering blog, the launch release — describe decision speed
only qualitatively, and none of them states a numeric latency figure of any
kind[^c-008]. The product page says "Decisions made in milliseconds"[^c-001]; the
blog and the release say "real time" and "instantly". Two targeted searches
returned nothing.

An independent auditor working from a fresh context confirmed the absence, and
rejected my own first wording of it — I had written that Razorpay describes speed
"only as milliseconds", which is false, since that word appears in one artifact of
three. The corrected claim is bound explicitly to the three captured artifacts,
because an absence claim scoped to "all public materials" cannot be discharged by
three files.

One trap worth carrying forward: the blog's phrase "at that exact millisecond"
describes how quickly a routing path degrades. It is not a latency figure.

The "200–800 ms" baseline is equally untraceable. A fabricated number is bad; a
fabricated number inside a comparison table, cited, is worse, because the table is
the artifact a reader screenshots.

## 2. An attribution that resolves to nothing

The documents assert that "a recent study finds that monolithic agentic AI often
hits a ceiling", with rising costs and declining accuracy on niche tasks. That
claim **failed verification** and is not cited anywhere in this report. The vendor
article it points at renders its body in JavaScript, so only navigation was
captured; a targeted search for the phrasing surfaced adjacent research on agentic
token costs but nothing matching.

This matters because the claim is load-bearing: it is the empirical support for
the documents' central architectural recommendation.

The one measured comparison in this corpus points the other way. In network
configuration repair, agentic architectures outperformed base models on repair
efficacy by 12% and on safety by 17%[^c-013] — though that is a different domain,
and the sources disagree enough that the question stays open[^c-018].

There is also a category problem. The monolith-versus-microservices argument is
borrowed from commentary about LLM agents. A structured-data transformer serving
payment decisions is a different class of system, and the transfer is the
documents' inference rather than their source's claim.

## 3. Vendor claims presented as findings

These are real and correctly quoted. They are also unverifiable.

Razorpay's own page states an 8–10% improvement in success rates, 5x more disputed
transactions identified, and 8x more international card fraud detected[^c-001].
The training scale — 3 trillion data points across 4 billion payments — comes from
Razorpay's chief executive in a named interview[^c-003], with NVIDIA H100s and AWS
as the stated infrastructure[^c-004]. The named merchants check out against the
launch release[^c-007].

What is missing everywhere is method. No baseline, no measurement window, no
control, no confidence interval — including in Razorpay's own engineering blog,
which contains no benchmark, holdout or accuracy figure at all.

This is not only my reading. Independent trade analysis reaches it directly:
enterprises "still lack baselines, testing methodology, confidence intervals and
independent validation needed for assessment"[^c-005], and the baseline for the
8–10% figure has not been released[^c-006].

So every performance figure traces to a single origin, and no independent party
has measured the system[^c-015]. Twelve URLs circulating after launch are one
source, not twelve. NVIDIA and AWS are commercial partners in the announcement,
not validators.

---

## What the literature actually says

The documents present the shift from gradient-boosted trees to transformers on
tabular data as settled. It is not, and more importantly **the evidence on both
sides is about a different machine**.

The most-cited benchmark for tree-based models scopes its finding explicitly to
medium-sized data of around ten thousand samples[^c-009]. Vulcan claims four
billion transactions — roughly five orders of magnitude apart. Meanwhile the
leading tabular foundation model's results were established largely in closed
evaluation settings, with open-environment robustness still an open
question[^c-010].

The honest position is that the literature neither supports the documents' premise
nor refutes it[^c-016]. That cuts both ways: it would be equally wrong to wave the
GBDT benchmark at Vulcan and declare the architecture disproven. Nobody has
benchmarked this regime in public.

## The comparator

Stripe's payments foundation model is the obvious parallel, and the contrast is
instructive. Stripe's own engineering write-up reports that after deployment "our
detection rate for attacks on large users significantly increased—from 59% to
97%"[^c-028] on card-testing attacks. Both Stripe's figures and Razorpay's are
vendor-published, so this is a contrast in **disclosure**, not in verified
performance[^c-017] — but Stripe names a baseline and a specific attack class,
which is the minimum an outside reader needs to weigh a claim, and which Razorpay
does not provide.

This supersedes the trade-press rendering of the same result carried in the first
pass[^c-011], which reported it as a 64% improvement against an 80% target. The
first-party number is different, better scoped, and the one that should be cited.

An adviser quoted in the same coverage warns that where regional payment behaviour
is under-represented, such a model's predictions may skew in both
directions[^c-012]. That is worth carrying: an India-only training corpus presents
the same structural risk in reverse.

---

## What can be published

**As fact:** that Razorpay claims these gains; the training scale and
infrastructure, attributed to a named executive; the merchant names; that the
tabular literature is silent at this scale; that the comparator discloses more
method.

**Only with attribution:** every performance figure, in the form "Razorpay says",
with the absence of a baseline stated in the same breath.

**Cut:** the 29ms figure and its 200–800ms counterpart; the "hits a ceiling"
claim; and the framing that treats the GBDT-to-transformer shift as settled.

## Limitations

- **No T1 sources, and there cannot be.** The model is unrunnable outside
  Razorpay, so no benchmark can be rerun. Of 11 sources: 3 T2, 4 T3, 4 T4.
- **Recency cuts against depth.** Vulcan was announced days before this research.
  Nothing has had time to be independently verified — an absence of scrutiny, not
  evidence of failure.
- **Single-source dependency:** the independent critique rests on one outlet. If
  it were withdrawn, the baseline objection would rest on my reading alone.
- **Not read:** the body of the network-repair paper, whose cost comparison I saw
  only in a search summary and deliberately did not cite; the ACM tabular survey;
  Stripe's own publication of its results.
- **One claim failed verification** and is cited nowhere above.

---

## What three later sources changed

Three sources added after the first pass revise its central finding, and revise
it against me.

**The category is not opaque. One vendor is.** That first report treated
unverifiability as a property of transactional foundation models. It is not.
Plaid states its results at named operating points — 26.5% more dollar value in
returns prevented **at a fixed 1% action rate**, and default risk down 13.6% **at
a 70% approval rate**[^c-019]. An operating point is the whole game: without one,
a detection improvement is unreadable, because it can always be bought with false
positives. A consultancy survey of the category states a sample — 60 enterprise
pilots — even while reporting ceilings rather than typical results[^c-020]. And
practitioners note that firms in this category have put methods, and failures, on
the public record[^c-023].

So the finding narrows and hardens: **Razorpay sits below a disclosure bar its
peers already clear**[^c-024]. That is a more specific criticism than the first
report made, and a fairer one.

## Third pass: the primaries, and what changed on contact with them

The second pass carried two architectural data points at one remove, through a
practitioner summarising Adyen's and Stripe's published work rather than through
those publications themselves. Both have now been obtained. **Both changed**, and
flagging that is not pedantry — a secondhand attribution presented as a finding is
the precise failure this report opens by documenting.

**Adyen.** The rendering was *tried, failed, kept trying*. The primary is more
specific and more useful: Adyen reports trying "bigger artifacts and complex deep
learning models" that combine multiple decisions and finding they would often
"compromise the engineering requirements (latency, uptime) of online deployments in
a critical flow"[^c-025]. What failed was not accuracy. It was latency and uptime,
in the synchronous path — which is precisely the architectural objection, stated by
a company that attempted the consolidation.

The same source carries the half a selective reader would drop, and it must be
carried alongside: Adyen keeps investigating that direction and is "expecting to
move the whole pipeline to deep learning architectures in the short
future"[^c-026]. Adyen is therefore not a witness against consolidation. It is a
witness that consolidation is operationally hard in a critical flow *today*, while
intending to get there.

Its current architecture is the third option the monolith-versus-microservices
framing hides: "a collection of machine learning models of various natures that
share awareness and knowledge"[^c-027], optimized globally rather than merged.

**Stripe.** The 59%-to-97% figure is confirmed first-party[^c-028]. The phrase
attributed to Stripe is not. "An addition, not a replacement" is **not Stripe's
wording** — the word *replace* appears in neither Stripe primary; that was the
practitioner's paraphrase, and this report repeated it as a quotation. It is
withdrawn, and c-021 is superseded. What the primaries do support is narrower and
architecturally stronger: the model "compresses payments into atomic embeddings,
which we then leverage across multiple card testing use cases, such as training
classifiers on sequences of embeddings"[^c-029] — a representation layer feeding
specialists rather than a decision-maker standing in for them.

**The decoupling rationale.** The bulkhead pattern is captured as a technique "for
isolating parts of an application into pools or compartments so that failure of one
component will not cascade to other components"[^c-030]. Its canonical source,
Nygard's *Release It!* (2007), was **not obtained**; this is an encyclopedia's
account of the pattern that book introduced, and any text resting on it must say
so.

From that plus Adyen's report, the central architectural claim: a shared backbone
serving routing, fraud, risk and checkout removes the compartment boundary the
bulkhead exists to create, making its failure a single point of failure **by
construction rather than by misconfiguration**[^c-031]. This is recorded at low
confidence and it is deduction, not measurement. Nobody has benchmarked a
consolidated payments backbone against a decomposed one in production; if they had,
this report would cite it instead of reasoning.

## References

[^c-008]: Razorpay's first-party Vulcan materials - the product page, the engineering blog and the launch press release - describe decision speed only qualitatively: 'Decisions made in milliseconds' on the product page, and 'real time' or 'instantly' elsewhere. None states a numeric latency figure of any kind, and no 29-millisecond inference budget appears in any of them.
    — *Vulcan: AI payments foundation model (Razorpay)*, Razorpay, 2026-08. https://razorpay.com/foundation-model/
      [T4] section: the three first-party artifacts captured: s-001, s-003, s-004
    Note: FIRST WORDING FAILED THE AUDITOR. It said Razorpay describes speed 'only as milliseconds', which is false: that word appears in s-001 alone, while s-003 and s-004 use 'real time' and 'instantly'. It also scoped the absence to 'Razorpay's public materials' and 'no first-party source', which three snapshots cannot discharge. This is the auditor's narrower wording, bound explicitly to the three captured artifacts. Caution recorded by the auditor: s-003's phrase 'at that exact millisecond' describes how fast a routing path degrades, NOT inference latency, and must not be repurposed as a speed claim.

[^c-001]: Razorpay's own product page states three headline gains for Vulcan: an 8-10% improvement in success rates, 5x more disputed transactions identified, and 8x more international card fraud detected.
    — *Vulcan: AI payments foundation model (Razorpay)*, Razorpay, 2026-08. https://razorpay.com/foundation-model/
      [T4] quote: "8-10% improvement in success rates ... 5X more disputed transactions identified ... 8X more international card fraud detected"
    Note: First-party marketing. Under the technical lens this is T4: a claim about a system nobody outside Razorpay can run.

[^c-013]: In network configuration repair, agentic architectures outperformed base models on repair efficacy by 12% and on safety by 17% on average.
    — *Evaluating Agentic Configuration Repair for Computer Networks*, arXiv, 2026-06. https://arxiv.org/abs/2606.06212
      [T2] quote: "agentic architectures outperform base LLMs in repair efficacy (by 12% on average) and safety (by 17% on average)"
    Note: Runs against the documents' framing that modular agentic designs are the compromise option. Different domain, and the cost comparison reported elsewhere is in the paper body which was not read.

[^c-018]: The documents' architectural conclusion rests on an untraceable claim and on evidence from a different class of system, while the one measured comparison in the corpus found modular agentic designs outperforming a monolithic baseline on efficacy and safety.
    — *Evaluating Agentic Configuration Repair for Computer Networks*, arXiv, 2026-06. https://arxiv.org/abs/2606.06212
      [T2] quote: "agentic architectures outperform base LLMs in repair efficacy (by 12% on average) and safety (by 17% on average)"
    CONTESTED (mixed) by: s-010
    Note: THE ANSWER TO SUB-QUESTION 4. c-014 failed outright, and the evidence that does exist is from network configuration repair, not payments. Marked mixed because the retrieved evidence points against the documents' framing while the vendor commentary they cite points for it, and neither is about a transactional foundation model.

[^c-003]: Razorpay's chief executive states that Vulcan was trained on 3 trillion data points collected across 4 billion digital payments.
    — *Vulcan understands the language of money: Harshil Mathur on Razorpay's AI push*, Hindustan Times, 2026-08. https://www.hindustantimes.com/business/vulcan-understands-the-language-of-money-harshil-mathur-on-razorpay-s-ai-push-101786987475914.html
      [T3] quote: "Training the model on 3 trillion data points collected across 4 billion digital payments"
    Note: Attributed to Harshil Mathur in a named publication, which is better provenance than an anonymous release, but still the vendor describing its own system.

[^c-004]: The training and inference hardware is reported as NVIDIA H100 GPUs, with AWS supplying the cloud infrastructure.
    — *Vulcan understands the language of money: Harshil Mathur on Razorpay's AI push*, Hindustan Times, 2026-08. https://www.hindustantimes.com/business/vulcan-understands-the-language-of-money-harshil-mathur-on-razorpay-s-ai-push-101786987475914.html
      [T3] quote: "this mostly includes the top-end H100 GPUs. AWS provided the scalable cloud infrastructure as well as architectural g"
    Note: NVIDIA and AWS are named commercial partners in the launch, so this is not third-party corroboration of anything beyond the hardware itself.

[^c-007]: Razorpay names Blinkit, redBus and Bachatt as merchants in the early deployment.
    — *Razorpay Launches Vulcan, India's First AI Payments Foundation Model, Fueled by NVIDIA and AWS*, AWS press centre (Razorpay release), 2026-08. https://press.aboutamazon.com/aws-international/2026/8/razorpay-launches-vulcan-indias-first-ai-payments-foundation-model-fueled-by-nvidia-and-aws-re-architecting-payments-for-a-350-bn-e-comm-future-by-2030
      [T4] quote: "Blinkit, Bachatt"
    Note: The merchant names check out against the launch release; what is absent is any per-merchant measurement.

[^c-005]: Independent trade analysis finds that the Vulcan figures come without the baselines, testing methodology, confidence intervals or independent validation an enterprise would need to assess them.
    — *Razorpay built one AI for payments, fraud and checkout*, DataQuest India, 2026-08. https://www.dqindia.com/news/razorpay-vulcan-8x-fraud-detection-baseline-12398348
      [T3] quote: "enterprises still lack baselines, testing methodology, confidence intervals and independent validation needed for assessment"
    Note: THE CENTRAL FINDING, and it is reached independently rather than only by me. T3 trade press, but specific and named.

[^c-006]: The baseline for the 8-10% success-rate improvement has not been released, leaving open what the improvement was measured against.
    — *Razorpay built one AI for payments, fraud and checkout*, DataQuest India, 2026-08. https://www.dqindia.com/news/razorpay-vulcan-8x-fraud-detection-baseline-12398348
      [T3] quote: "according to Razorpay, but the baseline has not been released. What was this 8-10% improvement measured against?"

[^c-015]: Every performance figure attributed to Vulcan originates with Razorpay, and no independent party has measured the system; the gap is not that the numbers are contradicted but that nothing outside the vendor exists to check them against.
    — *Vulcan: AI payments foundation model (Razorpay)*, Razorpay, 2026-08. https://razorpay.com/foundation-model/
      [T4] quote: "8-10% improvement in success rates ... 8X more international card fraud detected"
    — *Razorpay built one AI for payments, fraud and checkout*, DataQuest India, 2026-08. https://www.dqindia.com/news/razorpay-vulcan-8x-fraud-detection-baseline-12398348
      [T3] quote: "enterprises still lack baselines, testing methodology, confidence intervals and independent validation needed for assessment"
    Note: THE ANSWER TO SUB-QUESTION 1 AND 2. Under the technical lens a vendor benchmark is strong evidence of what the vendor claims and weak evidence of what a buyer will see. There is no T1 or T2 source in this corpus for any Vulcan performance figure, and there cannot be while the model is unrunnable outside Razorpay.

[^c-009]: The benchmark most often cited for tree-based models beating deep learning scopes its finding to medium-sized data of around ten thousand samples.
    — *Why do tree-based models still outperform deep learning on typical tabular data? (Grinsztajn, Oyallon, Varoquaux)*, arXiv / NeurIPS 2022 Datasets and Benchmarks, 2022-07. https://arxiv.org/abs/2207.08815
      [T2] quote: "tree-based models remain state-of-the-art on medium-sized data ($\sim$10K samples)"
    Note: Decisive for scope: this is five orders of magnitude below the 4 billion transactions Vulcan claims, so it neither supports nor refutes the Vulcan architecture. The source documents cite the GBDT-versus-transformer debate as though it settles their case.

[^c-010]: The leading tabular foundation model's strong results have been established largely in closed evaluation settings, and its robustness in open environments was still an open question as of that evaluation.
    — *Realistic Evaluation of TabPFN v2 in Open Environments*, arXiv, 2025-05. https://arxiv.org/abs/2505.16226
      [T2] quote: "the majority of this research remains confined to closed environments ... Can TabPFN v2 maintain good performance in open environments?"
    Note: Disconfirming for the documents' premise that tabular transformers are an established win.

[^c-016]: The tabular-model literature cited to justify a transformer backbone measures a data regime roughly five orders of magnitude smaller than the system it is used to justify, so it neither supports nor refutes the payments architecture.
    — *Why do tree-based models still outperform deep learning on typical tabular data? (Grinsztajn, Oyallon, Varoquaux)*, arXiv / NeurIPS 2022 Datasets and Benchmarks, 2022-07. https://arxiv.org/abs/2207.08815
      [T2] quote: "tree-based models remain state-of-the-art on medium-sized data ($\sim$10K samples)"
    — *Realistic Evaluation of TabPFN v2 in Open Environments*, arXiv, 2025-05. https://arxiv.org/abs/2505.16226
      [T2] quote: "the majority of this research remains confined to closed environments ... Can TabPFN v2 maintain good performance in open environments?"
    Note: THE ANSWER TO SUB-QUESTION 3, and it cuts both ways: the GBDT benchmark cannot be used to dismiss Vulcan either. The source documents present the debate as settled in the transformer's favour; the honest position is that nobody has benchmarked this regime in public.

[^c-028]: Stripe reports that after deploying its Payments Foundation Model, its detection rate for card-testing attacks on large users increased from 59% to 97% overnight.
    — *Using AI to optimize payments performance with the Payments Intelligence Suite*, Stripe, 2025. https://stripe.com/blog/using-ai-optimize-payments-performance-payments-intelligence-suite
      [T4] quote: "our detection rate for attacks on large users significantly increased-from 59% to 97%"
    Note: SUPERSEDES the trade-press version in c-011. First-party, and it states both a baseline and an attack class -- the disclosure Razorpay omits. Vendor-published, so T4.

[^c-017]: The comparator vendor discloses more method than Razorpay does, naming a baseline detection rate and a specific attack class, which is the minimum an outside reader needs to weigh a claim.
    — *Stripe's semantics-of-money AI turns heads. Can it adapt?*, The Stack, 2025. https://www.thestack.technology/stripes-semantics-of-money-ai-turns-heads-c/
      [T3] quote: "a 64% improvement in the rate of detecting card-testing ... compared to a two-year slog to achieve an 80%"
    — *Razorpay built one AI for payments, fraud and checkout*, DataQuest India, 2026-08. https://www.dqindia.com/news/razorpay-vulcan-8x-fraud-detection-baseline-12398348
      [T3] quote: "according to Razorpay, but the baseline has not been released. What was this 8-10% improvement measured against?"
    Note: Both figures are vendor-sourced, so this is a contrast in disclosure rather than in verified performance. Confidence is low because the Stripe figure reaches me through trade press, not from Stripe's own publication.

[^c-011]: Stripe's comparable payments foundation model was reported to improve card-testing detection on large businesses by 64% quickly, against a two-year effort to reach an 80% rate.
    — *Stripe's semantics-of-money AI turns heads. Can it adapt?*, The Stack, 2025. https://www.thestack.technology/stripes-semantics-of-money-ai-turns-heads-c/
      [T3] quote: "a 64% improvement in the rate of detecting card-testing ... compared to a two-year slog to achieve an 80%"
    Note: Comparator case. Still a vendor-sourced figure, reported by trade press. Its value here is that Stripe states a baseline and an attack class, which Razorpay does not.

[^c-012]: An adviser quoted in independent coverage of Stripe's model warns that where regional payment behaviour is under-represented its predictions may skew, producing both false positives and negatives.
    — *Stripe's semantics-of-money AI turns heads. Can it adapt?*, The Stack, 2025. https://www.thestack.technology/stripes-semantics-of-money-ai-turns-heads-c/
      [T3] quote: "its predictions may be skewed, potentially leading to both false positives and negatives"
    Note: Named outside expert, not a measurement. Relevant to Vulcan because an India-only training corpus is the same structural risk in reverse.

[^c-019]: Plaid reports its sequential model preventing 26.5% more dollar value in returns at a fixed 1% action rate, and reducing default risk by 13.6% at a 70% approval rate.
    — *Plaid: sequential foundation model*, Plaid, 2025. https://plaid.com/blog/sequential-foundation-model/
      [T4] quote: "prevented 26.5% more dollar value in returns at a fixed 1% action rate ... reduced the default risk by 13.6% at a 70% approval rate"
    Note: THE DISCLOSURE CONTRAST. Vendor-published like Razorpay's, but both figures name an operating point -- a fixed action rate and a fixed approval rate. Without one, a detection improvement is unreadable, because it can always be bought with false positives. This is precisely what Razorpay's multipliers omit.

[^c-020]: A consultancy analysis of the category reports conversion uplift of up to 6%, cost reductions of up to 5%, and an 86% reduction in manual risk rules across 60 enterprise pilots.
    — *The power of transaction foundation models: building the unified intelligence layer for payments*, Thoughtworks, 2026. https://www.thoughtworks.com/en-in/insights/articles/power-of-transaction-foundation-models-building-the-unified-intelligence-layer-for-payments
      [T3] quote: "conversion uplift of up to 6%, cost reductions of up to 5% and an 86% reduction in manual risk rules across 60 enterprise pilots"
    Note: States a sample (60 pilots), which is more than Razorpay offers, but 'up to' reports a ceiling rather than a typical result and the pilots are not identified. Thoughtworks sells delivery consulting into this category.

[^c-023]: Companies in this category have published methods and failures on the public record, which establishes a disclosure norm rather than an industry-wide opacity.
    — *Transaction foundation models (Dwayne Gefferie)*, Dwayne Gefferie (Substack), 2025. https://dwaynegefferie.substack.com/p/transaction-foundation-models
      [T3] quote: "these companies are putting their methods, and even their failures, on the public record"
    Note: Reframes the critique fairly: the problem is not that transactional foundation models are inherently unverifiable, but that one vendor's disclosure falls below a standard its peers already meet.

[^c-024]: Razorpay's disclosure is the outlier in its category rather than the norm: peers state operating points, sample sizes, and in one case a failed attempt, while Razorpay states bare multipliers with no baseline.
    — *Plaid: sequential foundation model*, Plaid, 2025. https://plaid.com/blog/sequential-foundation-model/
      [T4] quote: "prevented 26.5% more dollar value in returns at a fixed 1% action rate ... reduced the default risk by 13.6% at a 70% approval rate"
    — *Razorpay built one AI for payments, fraud and checkout*, DataQuest India, 2026-08. https://www.dqindia.com/news/razorpay-vulcan-8x-fraud-detection-baseline-12398348
      [T3] quote: "enterprises still lack baselines, testing methodology, confidence intervals and independent validation needed for assessment"
    Note: REVISES THE FIRST REPORT. That report treated unverifiability as a property of the category. These three sources show it is not: the comparators disclose operating points and sample sizes. The finding is narrower and harder -- Razorpay is below a bar its peers clear.

[^c-025]: Adyen reports trying bigger artifacts and complex deep learning models that combine multiple decisions, and finding they would often compromise the engineering requirements - latency and uptime - of online deployments in a critical flow.
    — *The AI behind Uplift (Andreu Mora, Adyen)*, Adyen, 2024. https://www.adyen.com/knowledge-hub/the-ai-behind-uplift
      [T4] quote: "bigger artifacts and complex deep learning models ... compromise the engineering requirements (latency, uptime) of online deployments in a critical flow."
    Note: SUPERSEDES c-022, which reached this at one remove as 'tried, failed, and will keep trying'. The primary is more specific and more useful: what failed was not accuracy but latency and uptime IN A CRITICAL FLOW, which is precisely the architectural objection. First-party vendor writing, so still T4.

[^c-026]: Adyen states it continues to investigate that approach and expects to move its whole pipeline to deep learning architectures in the short future.
    — *The AI behind Uplift (Andreu Mora, Adyen)*, Adyen, 2024. https://www.adyen.com/knowledge-hub/the-ai-behind-uplift
      [T4] quote: "We do however keep on investigating this line of thinking ... expecting to move the whole pipeline to deep learning architectures in the short future"
    Note: THE HONEST OTHER HALF, and it must be carried alongside c-025. Adyen is not a witness against consolidation. It is a witness that consolidation is operationally hard in a critical flow today, while intending to get there. Quoting the first half alone would be the same selective use this paper criticises.

[^c-027]: Adyen's current architecture is a collection of machine learning models of various natures that share awareness and knowledge, optimized globally toward a shared objective rather than merged into one model.
    — *The AI behind Uplift (Andreu Mora, Adyen)*, Adyen, 2024. https://www.adyen.com/knowledge-hub/the-ai-behind-uplift
      [T4] quote: "consists of a collection of machine learning models of various natures that share awareness and knowledge"
    Note: The alternative architecture, evidenced: coordinated specialists with a shared objective, not one backbone. This is the concrete shape of the 'supporting system' position.

[^c-029]: Stripe describes its foundation model as compressing payments into atomic embeddings that it then leverages across multiple use cases, including training classifiers on sequences of those embeddings.
    — *The ML flywheel: How we continually improve our models to reduce card testing*, Stripe, 2025. https://stripe.com/blog/the-ml-flywheel-how-we-continually-improve-our-models-to-reduce-card-testing
      [T4] quote: "It also compresses payments into atomic embeddings, which we then leverage across multiple card testing use cases, such as training classifiers on sequences of embeddings"
    Note: REPLACES c-021, whose 'an addition, not a replacement' was a practitioner's paraphrase and is NOT Stripe's wording -- the word 'replace' does not appear in either Stripe primary. What the primaries do support is architecturally stronger and more precise: the foundation model is a representation layer feeding downstream classifiers, not a decision-maker standing in for them.

[^c-030]: The bulkhead pattern isolates parts of an application into pools or compartments so that the failure of one component will not cascade to others, named for the watertight sections of a ship's hull.
    — *Bulkhead pattern (Wikipedia)*, Wikipedia, 2026. https://en.wikipedia.org/wiki/Bulkhead_pattern
      [T4] quote: "for isolating parts of an application into pools or compartments so that failure of one component will not cascade to other components"
    Note: THE SOURCE SECTION 3 NEEDED, and its provenance must be stated in the text. Nygard's Release It! (2007) was NOT obtained; this is an encyclopedia's account of the pattern it introduced. A paper that opens on an invented citation cannot cite a book it has not opened.

[^c-031]: A shared backbone serving routing, fraud, risk and checkout from one model removes the compartment boundary that the bulkhead pattern exists to create, making its failure a single point of failure by construction rather than by misconfiguration.
    — *Bulkhead pattern (Wikipedia)*, Wikipedia, 2026. https://en.wikipedia.org/wiki/Bulkhead_pattern
      [T4] quote: "for isolating parts of an application into pools or compartments so that failure of one component will not cascade to other components"
    — *The AI behind Uplift (Andreu Mora, Adyen)*, Adyen, 2024. https://www.adyen.com/knowledge-hub/the-ai-behind-uplift
      [T4] quote: "compromise the engineering requirements (latency, uptime) of online deployments in a critical flow."
    Note: THE PAPER'S CENTRAL ARCHITECTURAL CLAIM. It is deduction from a definition plus one practitioner report, not a measurement, and the text must present it that way. Nobody has benchmarked a consolidated payments backbone against a decomposed one in production; if they had, this paper would cite it instead of reasoning.

