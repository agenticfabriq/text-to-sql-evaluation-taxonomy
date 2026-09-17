# Text-to-SQL Evaluation Taxonomy

A shared vocabulary for measuring text-to-SQL and data-agent systems honestly:
how answers are graded, how systems fail, how often they refuse, and how
stable they are from run to run.

It exists because the same system can rank first on one benchmark and third
on another without getting any better or worse — the grading rule and the
answer shape changed, not the capability. If you're comparing vendors or
tuning your own pipeline, you need to know which of those you're looking at.

**Canonical site:** https://agenticfabriq.github.io/text-to-sql-evaluation-taxonomy/
**Maintainer:** [Agentic Fabriq](https://www.agenticfabriq.com/mnemiq), publisher of the open-source [mnemiq](https://github.com/agenticfabriq/mnemiq) engine and the [Beacon](https://github.com/agenticfabriq/beacon) grader
**Content & data:** CC BY 4.0 · **Code:** Apache-2.0

---

## Dimensions

| Dimension | Question | File |
|---|---|---|
| Grading rule | When is an answer counted correct? | [`taxonomy/grading-rule.yaml`](taxonomy/grading-rule.yaml) |
| Answer shape | How does the result's form differ from the reference? | [`taxonomy/answer-shape.yaml`](taxonomy/answer-shape.yaml) |
| Failure mode | Why was a wrong answer wrong? | [`taxonomy/failure-mode.yaml`](taxonomy/failure-mode.yaml) |
| Refusal | Did the system decline, and was that right? | [`taxonomy/refusal.yaml`](taxonomy/refusal.yaml) |
| Stability | Does the system give the same verdict on repeated runs? | [`taxonomy/stability.yaml`](taxonomy/stability.yaml) |
| Pre-execution check | What was verified before SQL touched data? | [`taxonomy/pre-execution-check.yaml`](taxonomy/pre-execution-check.yaml) |
| Semantic context | What context did the model get about the schema? | [`taxonomy/semantic-context.yaml`](taxonomy/semantic-context.yaml) |
| Benchmark corpus | Which public question set, and what does it reward? | [`taxonomy/benchmark-corpus.yaml`](taxonomy/benchmark-corpus.yaml) |

## Five things this vocabulary makes visible

1. **Accuracy does not transfer across databases.** Report per-schema spread, not
   just a mean.
2. **Exact match and got-the-facts can rank systems in opposite orders.** Always
   state the grading rule next to the number.
3. **A score without a refusal rate is incomplete.** A system that never
   declines looks more accurate than one that declines when it should.
4. **A single run hides instability.** Report case-flip rate over ≥3 runs.
5. **Vendor-reported numbers on private sets aren't comparable to public ones.**
   Label the corpus.

## Data

[`data/published-comparison-2026-09.csv`](data/published-comparison-2026-09.csv)
reproduces the headline comparison from the
[mnemiq launch article](https://www.agenticfabriq.com/blog/mnemiq/launch) in
machine-readable form, tagged with this taxonomy's grading-rule IDs. **These
are first-party results published by the maintainer**; methodology is in the
[technical report](https://www.agenticfabriq.com/mnemiq/mnemiq-technical-report.pdf),
and the grader is open so anyone can re-run them.

## How to cite

See [`CITATION.cff`](CITATION.cff).

## About the maintainer

Agentic Fabriq publishes [mnemiq](https://www.agenticfabriq.com/mnemiq), an
Apache-2.0 text-to-SQL engine where an LLM proposes SQL and deterministic
checks decide whether it runs. The taxonomy is engine-agnostic and applies to
any text-to-SQL system.
