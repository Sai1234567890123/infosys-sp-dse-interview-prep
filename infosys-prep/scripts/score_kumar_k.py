"""Score the Kumar K list (sheet 1q-90q) with the same match % and prediction index as the CF lists.

Reads the Infosys question CSV and notes (same inputs as build3.py) plus the Kumar K notes in
sheet_1q_25q/kumar_k_notes_{a,b,c}.py, and writes sheet_1q_25q/kumar_k_scores.json.
Usage: python3 scripts/score_kumar_k.py [data_dir]   (run from infosys-prep/; data_dir defaults to the project folder)
"""
import csv, glob, json, sys
from collections import defaultdict

D = sys.argv[1] if len(sys.argv) > 1 else "/mnt/project-files/infosys-prep/"
inf = list(csv.DictReader(open(D + "infosys_sp_dse_questions.csv", encoding="utf-8")))


def num(x, d=None):
    try:
        return int(float(x))
    except Exception:
        return d


inotes = {}
for f in sorted(glob.glob(D + "raw_notes/inf_notes*.jsonl")):
    for line in open(f, encoding="utf-8", errors="replace"):
        try:
            o = json.loads(line)
        except Exception:
            continue
        if o.get("id"):
            inotes[o["id"]] = o


def pats(n):
    p = n.get("patterns") or []
    return [p] if isinstance(p, str) else [x for x in p if isinstance(x, str)]


# Same weights as build3.py
CLAIM = {"actual": 1.0, "memory-based recollection": 0.7, "previous-year compilation": 0.4}
def recency(years):
    ys = [num(y) for y in years.split(",") if num(y)]
    if not ys: return 0.5
    y = max(ys)
    return 1.0 if y >= 2025 else 0.8 if y >= 2023 else 0.6
def round_w(r):
    r = (r or "").lower()
    return 0.6 if "interview" in r else 0.8 if r in ("", "unknown") else 1.0
for q in inf:
    q["_p"] = pats(inotes.get(q["id"], {}))
    ns = num(q["n_sources"], 1) or 1
    q["_w"] = CLAIM.get(q["source_claim"], 0.5) * recency(q["years"]) * round_w(q["round"]) * min(2.0, 1 + 0.25 * (ns - 1))

R2 = defaultdict(float)
for q in inf:
    if (num(q["cf_rating"]) or 0) >= 1300:
        for p in q["_p"]:
            R2[p] += q["_w"] / len(q["_p"])
R2max = max(R2.values()) if R2 else 1
R2n = {p: v / R2max for p, v in R2.items()}
oa = [num(q["cf_rating"]) for q in inf if num(q["cf_rating"]) and "interview" not in q["round"].lower()]
def fit_raw(r): return sum(1 for x in oa if abs(x - r) <= 150)
fmax = max(fit_raw(r) for r in range(800, 3001, 100)) or 1
def jac(a, b):
    a, b = set(a), set(b)
    return len(a & b) / len(a | b) if a and b else 0.0
infp = [(q, set(q["_p"]), {t.strip() for t in q["all_topics"].split(",") if t.strip()}, num(q["cf_rating"]))
        for q in inf if (num(q["cf_rating"]) or 0) >= 1200]


def score(p, topics, r):
    best, bq = 0.0, None
    for q, qp, qt, qr in infp:
        if not qp and not qt: continue
        rc = max(0.0, 1 - abs(r - qr) / 800) if qr else 0.5
        s = 0.6 * jac(p, qp) + 0.25 * jac(topics, qt) + 0.15 * rc
        if s > best: best, bq = s, q
    rp = max([R2n.get(x, 0) for x in p] or [0])
    return round(100 * best), (f'{bq["id"]} {bq["title"]}' if bq else ""), round(100 * (0.5 * best + 0.35 * rp + 0.15 * fit_raw(r) / fmax))


if __name__ == "__main__":
    sys.path.insert(0, "sheet_1q_25q")
    from kumar_k_notes_a import NOTES as A
    from kumar_k_notes_b import NOTES as B
    from kumar_k_notes_c import NOTES as C
    notes = {**A, **B, **C}
    out = {}
    for sid, n in notes.items():
        if n["rating"] is None:
            out[sid] = {"match_pct": 0, "prediction_index": 0, "nearest_infosys_question": ""}
            continue
        m, near, pred = score(set(n["pats"]), set(n["topics"]), n["rating"])
        out[sid] = {"match_pct": m, "prediction_index": pred, "nearest_infosys_question": near}
    json.dump(out, open("sheet_1q_25q/kumar_k_scores.json", "w"), indent=1, ensure_ascii=False)
    print(len(out), "scored")
