# -*- coding: utf-8 -*-
import json
import re

# Load existing INITIAL_QUESTIONS from data.js
with open('data.js', 'r', encoding='utf-8') as f:
    text = f.read()

# Match top-level question IDs (exclude d_ discussion IDs)
q_ids = [m for m in re.findall(r'"id":\s*"([^"]+)"', text) if not m.startswith('d_')]
print(f"Total question IDs in data.js: {len(q_ids)} (Unique: {len(set(q_ids))})")

with open(r'C:\Users\dharm\.gemini\antigravity-ide\brain\4d2782f7-7c34-4bed-82e0-d7028cb5b4e9\.system_generated\logs\transcript_full.jsonl', 'r', encoding='utf-8') as f:
    for line in f:
        obj = json.loads(line)
        if obj.get('type') == 'USER_INPUT':
            content = obj.get('content', '')

pattern = re.compile(r'\[([0-9]+[A-Z0-9]*)\]\(https://codeforces\.com/problemset/problem/([^)]+)\)\s*\n\s*\[([^\]]+)\]\([^)]+\)\s*\n\s*([^\n]+)\s*\n\s*([0-9]{3,4})')
matches = pattern.findall(content)

prompt_map = {}
for m in matches:
    qid = m[0]
    if qid not in prompt_map:
        prompt_map[qid] = {
            'id': qid,
            'url_path': m[1],
            'name': m[2],
            'raw_tags': m[3],
            'rating': int(m[4])
        }

print(f"Unique questions from prompt: {len(prompt_map)}")
existing_set = set(q_ids)
already_in = [qid for qid in prompt_map if qid in existing_set]
new_to_add = [qid for qid in prompt_map if qid not in existing_set]

print(f"Already in data.js: {len(already_in)}")
print(f"New questions to add: {len(new_to_add)}")
print(f"Sample 10 new questions to add: {new_to_add[:10]}")
