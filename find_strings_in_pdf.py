import re

file_path = r"C:\Users\dharm\Downloads\infosys_sp_dse_questions_part2.csv"
with open(file_path, "rb") as f:
    data = f.read()

# Let's search for ASCII strings of length >= 8
printable_strings = re.findall(rb'[A-Za-z0-9_\-\.\:\/\?\#\=\&\%\s]{8,}', data)
# Filter for words like http, github, leetcode, infosys, question, problem, etc.
interesting = []
keywords = [b'http', b'infosys', b'leetcode', b'question', b'dse', b'sp', b'hackwithinfy', b'problem', b'part', b'table', b'rating']

for s in printable_strings:
    s_lower = s.lower()
    for kw in keywords:
        if kw in s_lower:
            interesting.append(s.strip())
            break

print(f"Total interesting strings: {len(interesting)}")
for s in interesting[:30]:
    try:
        print(s.decode('latin1')[:120])
    except:
        pass
