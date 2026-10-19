# -*- coding: utf-8 -*-
import json
import re

with open(r'C:\Users\dharm\.gemini\antigravity-ide\brain\4d2782f7-7c34-4bed-82e0-d7028cb5b4e9\.system_generated\logs\transcript_full.jsonl', 'r', encoding='utf-8') as f:
    for line in f:
        obj = json.loads(line)
        if obj.get('type') == 'USER_INPUT':
            content = obj.get('content', '')

pattern = re.compile(r'\[([0-9]+[A-Z0-9]*)\]\(https://codeforces\.com/problemset/problem/([^)]+)\)\s*\n\s*\[([^\]]+)\]\([^)]+\)\s*\n\s*([^\n]+)\s*\n\s*([0-9]{3,4})')
matches = pattern.findall(content)

with open('data.js', 'r', encoding='utf-8') as f:
    existing_text = f.read()
existing_ids = set(m for m in re.findall(r'"id":\s*"([^"]+)"', existing_text) if not m.startswith('d_'))

batch3 = []
seen = set()
for m in matches:
    qid = m[0]
    if qid not in existing_ids and qid not in seen:
        seen.add(qid)
        batch3.append({
            'id': qid,
            'contestId': int(re.match(r'^([0-9]+)', qid).group(1)),
            'index': re.search(r'([A-Z0-9]+)$', qid).group(1),
            'name': m[2],
            'raw_tags': m[3],
            'rating': int(m[4]),
            'link': f"https://codeforces.com/problemset/problem/{m[1]}"
        })

print(f"Total Batch 3 items: {len(batch3)}")
with open('batch3_extracted.json', 'w', encoding='utf-8') as f:
    json.dump(batch3, f, indent=2)

print("Saved batch3_extracted.json successfully.")
