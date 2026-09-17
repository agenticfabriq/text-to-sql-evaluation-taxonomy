"""Validate taxonomy files and the published comparison. pip install pyyaml"""
import csv, glob, sys, yaml

ids = set()
for f in sorted(glob.glob("taxonomy/*.yaml")):
    d = yaml.safe_load(open(f))
    assert d["id"].startswith("tsqlet:"), f"{f}: dimension id must start with tsqlet:"
    for t in d["terms"]:
        assert t["id"].startswith(d["id"] + "/"), f"{f}: bad id {t['id']}"
        assert t["id"] not in ids, f"duplicate {t['id']}"
        assert t.get("label") and t.get("definition"), f"{f}: {t['id']} needs label and definition"
        ids.add(t["id"])

# Every term-shaped reference inside a taxonomy file must resolve.
for f in sorted(glob.glob("taxonomy/*.yaml")):
    text = open(f).read()
    import re
    for ref in re.findall(r"tsqlet:[a-z-]+/[a-z0-9-]+", text):
        assert ref in ids, f"{f}: unknown term {ref}"

# The comparison CSV: corpora and grading rules must be taxonomy terms once filled in.
rows = list(csv.DictReader(open("data/published-comparison-2026-09.csv")))
unconfirmed = 0
for r in rows:
    assert r["corpus_id"] in ids, f"csv: unknown corpus {r['corpus_id']}"
    g = r["grading_rule_id"]
    if g == "CONFIRM":
        unconfirmed += 1
    else:
        assert g in ids, f"csv: unknown grading rule {g}"
    float(r["score_pct"])
    assert r["claim_type"] in {"first-party", "third-party", "independent"}, f"csv: claim_type {r['claim_type']}"

print(f"ok: {len(ids)} terms; comparison rows {len(rows)}, {unconfirmed} awaiting grading-rule confirmation")
if unconfirmed and "--strict" in sys.argv:
    sys.exit("comparison rows still marked CONFIRM")
