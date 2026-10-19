# -*- coding: utf-8 -*-
"""
Generate comprehensive DP solutions, dry-runs, intuitions, complexities,
and code snippets for all Batch 3 Codeforces DP questions.
"""

import json
import re

with open('batch3_extracted.json', 'r', encoding='utf-8') as f:
    batch3_raw = json.load(f)

print(f"Loaded {len(batch3_raw)} questions from Batch 3.")
