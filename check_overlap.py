# -*- coding: utf-8 -*-
import json
import re

# 1. Load existing data.js
with open('data.js', 'r', encoding='utf-8') as f:
    text = f.read()

existing_ids = set(re.findall(r'"id":\s*"([^"]+)"', text))
print('Existing in data.js:', len(existing_ids))

# 2. Extract from transcript_full.jsonl
with open(r'C:\Users\dharm\.gemini\antigravity-ide\brain\4d2782f7-7c34-4bed-82e0-d7028cb5b4e9\.system_generated\logs\transcript_full.jsonl', 'r', encoding='utf-8') as f:
    for line in f:
        obj = json.loads(line)
        if obj.get('type') == 'USER_INPUT':
            content = obj.get('content', '')

pattern = re.compile(r'\[([0-9]+[A-Z0-9]*)\]\(https://codeforces\.com/problemset/problem/([^)]+)\)\s*\n\s*\[([^\]]+)\]\([^)]+\)\s*\n\s*([^\n]+)\s*\n\s*([0-9]{3,4})')
matches = pattern.findall(content)

prompt_ids = set(m[0] for m in matches)
print('Found in prompt:', len(matches), 'with unique IDs:', len(prompt_ids))
new_ids = prompt_ids - existing_ids
print('Brand new IDs to add:', len(new_ids))
print('Combined total will be:', len(existing_ids.union(prompt_ids)))
