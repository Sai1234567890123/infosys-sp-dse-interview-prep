import pymupdf
from PIL import Image
from rapidocr_onnxruntime import RapidOCR
import re
import json

engine = RapidOCR()
doc = pymupdf.open(r"C:\Users\dharm\Downloads\infosys_sp_dse_questions_part2.csv")

def extract_page(pno):
    page = doc[pno]
    pix = page.get_pixmap(dpi=150)
    img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
    img_rot = img.transpose(Image.Transpose.ROTATE_270)
    
    # Save temporary image for OCR
    tmp_path = f"tmp_page_{pno}.png"
    img_rot.save(tmp_path)
    
    res, _ = engine(tmp_path)
    if not res:
        return []
    
    # Filter out header elements (y < 180)
    items = []
    for bbox, text, score in res:
        xs = [pt[0] for pt in bbox]
        ys = [pt[1] for pt in bbox]
        min_x, max_x = min(xs), max(xs)
        min_y, max_y = min(ys), max(ys)
        cy = (min_y + max_y) / 2
        cx = (min_x + max_x) / 2
        
        # Skip header banner
        if cy < 170:
            continue
        items.append({
            'cx': cx, 'cy': cy, 'min_x': min_x, 'max_x': max_x,
            'min_y': min_y, 'max_y': max_y, 'text': text.strip(), 'score': score
        })
        
    # Find all Q-ids (Q0474, Q0475, etc.)
    q_anchors = []
    for it in items:
        # Check if text contains Q\d{4}
        m = re.search(r'Q(\d{4})', it['text'])
        if m and it['min_x'] < 150:
            qid = f"Q{m.group(1)}"
            # If QID is glued to title e.g. "Q0474Minimum candy"
            rest_title = it['text'][m.end():].strip()
            q_anchors.append({
                'qid': qid,
                'y': it['cy'],
                'min_y': it['min_y'],
                'max_y': it['max_y'],
                'rest_title': rest_title
            })
            
    q_anchors.sort(key=lambda a: a['y'])
    
    # If no Q-ids found, return empty
    if not q_anchors:
        return []
        
    # Establish row boundaries between consecutive anchors
    rows = []
    for i, anc in enumerate(q_anchors):
        top_y = (q_anchors[i-1]['y'] + anc['y']) / 2 if i > 0 else 170
        bottom_y = (anc['y'] + q_anchors[i+1]['y']) / 2 if i < len(q_anchors) - 1 else 9999
        
        row_items = [it for it in items if top_y <= it['cy'] < bottom_y]
        
        # Map row items to columns
        title_parts = [anc['rest_title']] if anc['rest_title'] else []
        primary_topic_parts = []
        all_topics_parts = []
        cf_rating = ""
        diff_label = ""
        years = ""
        roles = ""
        round_name = ""
        statement_parts = []
        constraints_parts = []
        sample_parts = []
        
        # Sort items in row by y then x
        row_items.sort(key=lambda it: (it['cy'], it['cx']))
        
        for it in row_items:
            t = it['text']
            x = it['cx']
            
            # If item is the Q-id anchor itself, skip
            if re.search(r'Q\d{4}', t) and it['min_x'] < 120:
                continue
                
            if x < 235:
                title_parts.append(t)
            elif 235 <= x < 375:
                primary_topic_parts.append(t)
            elif 375 <= x < 525:
                all_topics_parts.append(t)
            elif 525 <= x < 580:
                if not cf_rating:
                    cf_rating = t
            elif 580 <= x < 640:
                diff_label = t
            elif 640 <= x < 710:
                years = t
            elif 710 <= x < 795:
                roles = t
            elif 795 <= x < 885:
                round_name = t
            elif 885 <= x < 1235:
                statement_parts.append(t)
            elif 1235 <= x < 1475:
                constraints_parts.append(t)
            else:
                sample_parts.append(t)
                
        row_data = {
            'id': anc['qid'],
            'title': " ".join(title_parts).strip(),
            'primary_topic': " ".join(primary_topic_parts).strip(),
            'all_topics': ", ".join(all_topics_parts).strip(),
            'cf_rating': cf_rating,
            'difficulty_label': diff_label,
            'years': years,
            'roles': roles,
            'round': round_name,
            'statement': " ".join(statement_parts).strip(),
            'constraints': " ".join(constraints_parts).strip(),
            'sample': " ".join(sample_parts).strip()
        }
        rows.append(row_data)
        
    return rows

print("Testing extract_page(0)...")
res0 = extract_page(0)
print(f"Extracted {len(res0)} questions from page 0:")
for r in res0[:3]:
    print(r)
