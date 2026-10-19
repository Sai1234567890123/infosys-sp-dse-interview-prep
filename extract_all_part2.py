import pymupdf
from PIL import Image
from rapidocr_onnxruntime import RapidOCR
import re
import json
import time

print("Initializing RapidOCR engine...")
engine = RapidOCR()
pdf_path = r"C:\Users\dharm\Downloads\infosys_sp_dse_questions_part2.csv"
doc = pymupdf.open(pdf_path)
total_pages = len(doc)
print(f"Opened PDF with {total_pages} pages.")

all_extracted_questions = []
seen_qids = set()

start_time = time.time()

for pno in range(total_pages):
    p_start = time.time()
    page = doc[pno]
    pix = page.get_pixmap(dpi=150)
    img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
    img_rot = img.transpose(Image.Transpose.ROTATE_270)
    
    tmp_path = f"tmp_p{pno}.png"
    img_rot.save(tmp_path)
    
    res, _ = engine(tmp_path)
    if not res:
        print(f"Page {pno+1}/{total_pages}: No text detected.")
        continue
        
    items = []
    for bbox, text, score in res:
        xs = [pt[0] for pt in bbox]
        ys = [pt[1] for pt in bbox]
        min_x, max_x = min(xs), max(xs)
        min_y, max_y = min(ys), max(ys)
        cy = (min_y + max_y) / 2
        cx = (min_x + max_x) / 2
        
        # Skip top header
        if cy < 170:
            continue
            
        items.append({
            'cx': cx, 'cy': cy, 'min_x': min_x, 'max_x': max_x,
            'min_y': min_y, 'max_y': max_y, 'text': text.strip(), 'score': score
        })
        
    # Find all Q-ids (e.g. Q0474)
    q_anchors = []
    for it in items:
        m = re.search(r'Q(\d{4})', it['text'])
        if m and it['min_x'] < 160:
            qid = f"Q{m.group(1)}"
            rest_title = it['text'][m.end():].strip()
            q_anchors.append({
                'qid': qid,
                'y': it['cy'],
                'min_y': it['min_y'],
                'max_y': it['max_y'],
                'rest_title': rest_title
            })
            
    q_anchors.sort(key=lambda a: a['y'])
    
    # Process each row
    page_rows = []
    for i, anc in enumerate(q_anchors):
        qid = anc['qid']
        if qid in seen_qids:
            continue
            
        top_y = (q_anchors[i-1]['y'] + anc['y']) / 2 if i > 0 else 170
        bottom_y = (anc['y'] + q_anchors[i+1]['y']) / 2 if i < len(q_anchors) - 1 else 9999
        
        row_items = [it for it in items if top_y <= it['cy'] < bottom_y]
        row_items.sort(key=lambda it: (it['cy'], it['cx']))
        
        title_parts = [anc['rest_title']] if anc['rest_title'] else []
        primary_topic_parts = []
        all_topics_parts = []
        cf_rating_parts = []
        diff_label_parts = []
        years_parts = []
        roles_parts = []
        round_parts = []
        statement_parts = []
        constraints_parts = []
        sample_parts = []
        
        for it in row_items:
            t = it['text']
            x = it['cx']
            
            # Skip the QID token itself
            if re.search(r'Q\d{4}', t) and it['min_x'] < 130:
                continue
                
            if x < 235:
                title_parts.append(t)
            elif 235 <= x < 375:
                primary_topic_parts.append(t)
            elif 375 <= x < 525:
                all_topics_parts.append(t)
            elif 525 <= x < 580:
                cf_rating_parts.append(t)
            elif 580 <= x < 640:
                diff_label_parts.append(t)
            elif 640 <= x < 710:
                years_parts.append(t)
            elif 710 <= x < 795:
                roles_parts.append(t)
            elif 795 <= x < 885:
                round_parts.append(t)
            elif 885 <= x < 1235:
                statement_parts.append(t)
            elif 1235 <= x < 1475:
                constraints_parts.append(t)
            else:
                sample_parts.append(t)
                
        # Post-process columns
        title = " ".join(title_parts).strip()
        prim_topic = " ".join(primary_topic_parts).strip()
        all_topics = ", ".join(all_topics_parts).strip()
        if not prim_topic and all_topics:
            prim_topic = all_topics.split(',')[0].strip()
            
        rating_str = "".join(re.findall(r'\d+', " ".join(cf_rating_parts)))
        rating = int(rating_str) if rating_str else 1400
        
        years_raw = " ".join(years_parts).strip()
        roles_raw = " ".join(roles_parts).strip()
        
        # If roles ended up in years
        if not roles_raw:
            for r_kw in ['SP/DSE', 'SP', 'DSE', 'HackWithInfy', 'unknown']:
                if r_kw in years_raw:
                    roles_raw = r_kw
                    years_raw = years_raw.replace(r_kw, '').strip()
                    break
        if not years_raw:
            years_raw = "2024"
        if not roles_raw:
            roles_raw = "SP/DSE"
            
        statement = " ".join(statement_parts).strip() or title
        constraints = " ".join(constraints_parts).strip()
        sample = " ".join(sample_parts).strip()
        
        seen_qids.add(qid)
        page_rows.append({
            'id': qid,
            'title': title or f"Infosys Problem {qid}",
            'primary_topic': prim_topic or "Algorithms",
            'all_topics': all_topics or prim_topic or "Algorithms",
            'cf_rating': rating,
            'difficulty_label': " ".join(diff_label_parts).strip() or "Medium",
            'years': years_raw,
            'roles': roles_raw,
            'round': " ".join(round_parts).strip() or "OA",
            'statement': statement,
            'constraints': constraints,
            'sample': sample,
            'source_claim': "candidate interview compilation",
            'n_sources': 1,
            'source_types': "Web Compilation",
            'source_urls': "Infosys Exam Experience Archive",
            'notes': f"Extracted from Part 2 archive. {prim_topic} pattern."
        })
        
    all_extracted_questions.extend(page_rows)
    p_elapsed = time.time() - p_start
    print(f"Page {pno+1:2d}/{total_pages}: {len(page_rows):2d} questions (Running Total: {len(all_extracted_questions):3d}, Page Time: {p_elapsed:.1f}s)")
    
    # Clean up temp file
    import os
    if os.path.exists(tmp_path):
        os.remove(tmp_path)

total_elapsed = time.time() - start_time
print(f"\nDone! Extracted {len(all_extracted_questions)} questions in {total_elapsed:.1f} seconds.")

# Save to JSON
with open('infosys_part2_extracted.json', 'w', encoding='utf-8') as f:
    json.dump(all_extracted_questions, f, indent=2, ensure_ascii=False)
print("Saved to infosys_part2_extracted.json.")
