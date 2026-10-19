# -*- coding: utf-8 -*-
"""
Helper script to merge Part 2 of Infosys SP/DSE questions (Q0474 to Q0945)
with Part 1 (Q0001 to Q0473) to create the complete 945-question Infosys Database.
"""

import csv
import json
import re
import os

part1_path = r'C:\Users\dharm\Downloads\infosys_sp_dse_questions_part1.csv'
part2_candidates = [
    r'C:\Users\dharm\Downloads\infosys_sp_dse_questions_part2.csv',
    r'C:\Users\dharm\Downloads\infosys_sp_dse_questions.csv',
    'infosys_sp_dse_questions_part2.csv',
    'infosys_sp_dse_questions.csv'
]

found_part2 = None
for p in part2_candidates:
    if os.path.exists(p) and p != part1_path:
        found_part2 = p
        break

if not found_part2:
    print("Part 2 file not found yet. Please place 'infosys_sp_dse_questions_part2.csv' or the full 'infosys_sp_dse_questions.csv' in C:\\Users\\dharm\\Downloads\\.")
    exit(0)

print(f"Found Part 2 / Full file at: {found_part2}")

all_rows = []
seen_ids = set()

# Read Part 1
if os.path.exists(part1_path):
    with open(part1_path, 'r', encoding='utf-8', errors='ignore') as f:
        reader = csv.DictReader(f)
        for r in reader:
            qid = r.get('id', '').strip()
            if qid and qid not in seen_ids:
                seen_ids.add(qid)
                all_rows.append(r)

print(f"Loaded {len(all_rows)} rows from Part 1.")

# Read Part 2 / Full
with open(found_part2, 'r', encoding='utf-8', errors='ignore') as f:
    reader = csv.DictReader(f)
    added = 0
    for r in reader:
        qid = r.get('id', '').strip()
        if qid and qid not in seen_ids:
            seen_ids.add(qid)
            all_rows.append(r)
            added += 1

print(f"Added {added} new rows from {found_part2}. Total unique Infosys questions: {len(all_rows)}.")

# Convert to infosys-db.js
infosys_questions = []
for row in all_rows:
    qid = row.get('id', '').strip()
    title = row.get('title', '').strip()
    if not qid or not title:
        continue
    
    primary_topic = row.get('primary_topic', '').strip()
    all_topics_raw = row.get('all_topics', '').strip()
    topics = [t.strip().lower() for t in re.split(r'[,/]', all_topics_raw) if t.strip()]
    if not topics and primary_topic:
        topics = [primary_topic.lower()]
    
    roles_raw = row.get('roles', '').upper()
    if 'SP' in roles_raw and 'DSE' in roles_raw:
        exam_type = 'BOTH'
    elif 'SP' in roles_raw or 'HACKWITHINFY' in roles_raw or 'POWER PROGRAMMER' in roles_raw:
        exam_type = 'SP'
    elif 'DSE' in roles_raw or 'SE' in roles_raw or 'INFYTQ' in roles_raw:
        exam_type = 'DSE'
    else:
        exam_type = 'SP'
        
    role_label = "Specialist Programmer (9.5 LPA)" if exam_type == 'SP' else (
        "Digital Specialist Engineer (6.5 LPA)" if exam_type == 'DSE' else "SP & DSE Combined"
    )
    
    cf_rating = int(row.get('cf_rating', '0') or '0')
    claim = row.get('source_claim', 'previous-year compilation').strip()
    years = row.get('years', '2024').strip()
    source_types = row.get('source_types', 'Web Compilation').strip()
    statement = row.get('statement', '').strip() or title
    sample = row.get('sample', '').strip()
    constraints = row.get('constraints', '').strip()
    notes = row.get('notes', '').strip()
    
    weight = 0.75
    if 'actual' in claim: weight += 0.15
    elif 'memory-based' in claim: weight += 0.10
    if '2026' in years: weight += 0.08
    elif '2025' in years or '2024' in years: weight += 0.04
    weight = min(0.99, round(weight, 2))
    
    key_pattern = f"Pattern: {primary_topic}. {notes[:140] if notes else statement[:140]}"
    core_concepts = [primary_topic]
    for t in topics:
        if t not in [c.lower() for c in core_concepts]:
            core_concepts.append(t.title())
    
    item = {
        "id": qid,
        "examType": exam_type,
        "role": role_label,
        "title": title,
        "source": f"{source_types} ({years}) [{claim}]",
        "year": int(re.search(r'202[0-9]', years).group(0)) if re.search(r'202[0-9]', years) else 2024,
        "frequency": "Very High" if weight >= 0.90 else ("High" if weight >= 0.82 else "Medium"),
        "difficulty": f"{cf_rating} CF" if cf_rating else "1200-1400 CF",
        "rating": cf_rating,
        "topics": topics,
        "primaryTopic": primary_topic,
        "problemStatement": statement,
        "constraints": constraints,
        "sampleTestCase": {
            "input": sample if sample else "Array / Input sequence according to statement",
            "output": "Optimized objective value or target boolean",
            "explanation": notes if notes else "Follows optimal subproblem substructure."
        },
        "keyPattern": key_pattern,
        "coreConcepts": core_concepts[:4],
        "predictionWeight": weight,
        "sourceClaim": claim
    }
    infosys_questions.append(item)

js_code = f"""/**
 * Infosys SP & DSE Question Database (Full Exam Archive: 2021-2026)
 * Total Confirmed & PYQ Questions: {len(infosys_questions)}
 */

const INFOSYS_QUESTION_DB = {json.dumps(infosys_questions, indent=2, ensure_ascii=False)};

if (typeof window !== 'undefined') {{
  window.INFOSYS_QUESTION_DB = INFOSYS_QUESTION_DB;
}}
if (typeof module !== 'undefined' && module.exports) {{
  module.exports = INFOSYS_QUESTION_DB;
}}
"""

with open('infosys-db.js', 'w', encoding='utf-8') as f:
    f.write(js_code)

print(f"Successfully updated infosys-db.js with all {len(infosys_questions)} Infosys questions!")
