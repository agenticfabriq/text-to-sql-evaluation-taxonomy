# Contributing
- Propose a new term or change with an issue first. Include a definition, one published evaluation it describes, and why no existing term covers it.
- Terms describe measurement practice, never products. PRs naming a vendor in a term label will be asked to generalize.
- Term IDs are never reused or renamed. Deprecated terms stay with `deprecated: true` and a pointer to the replacement.
- A row in `data/` needs a public `source_url`, its `grading_rule_id`, and an honest `claim_type` (`first-party` when the publisher is one of the systems compared).
- Run `python scripts/validate.py` before opening a PR.
