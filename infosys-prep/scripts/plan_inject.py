import sys
P = "/mnt/project-files/infosys-prep/website/index.html"
html = open(P, encoding="utf-8").read()
if 'id="tab-plan"' in html:
    print("plan already present"); sys.exit(0)
section = open("/tmp/claude-0/-home-claude/b6d6127f-6e68-5a0a-9e95-739a8441dfc4/scratchpad/site/plan_section.html", encoding="utf-8").read()
script = open("/tmp/claude-0/-home-claude/b6d6127f-6e68-5a0a-9e95-739a8441dfc4/scratchpad/site/plan_script.js", encoding="utf-8").read()
btn = '    <button role="tab" data-tab="plan" aria-selected="false">Plan</button>\n'
anchor_btn = '    <button role="tab" data-tab="method"'
assert html.count(anchor_btn) == 1
html = html.replace(anchor_btn, btn + anchor_btn, 1)
anchor_sec = '  <section id="tab-method"'
assert html.count(anchor_sec) == 1
html = html.replace(anchor_sec, section + anchor_sec, 1)
arr_old = "['start','inf','cf','greedy','top','method']"
assert html.count(arr_old) == 1
html = html.replace(arr_old, "['start','inf','cf','greedy','top','plan','method']", 1)
anchor_js = "top.forEach(q => $('top-list').append(renderCf(q)));"
assert html.count(anchor_js) == 1
html = html.replace(anchor_js, anchor_js + "\n" + script, 1)
open(P, "w", encoding="utf-8").write(html)
print("plan injected")
