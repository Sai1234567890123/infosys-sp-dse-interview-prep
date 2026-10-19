import pymupdf
from PIL import Image
from rapidocr_onnxruntime import RapidOCR
import re

engine = RapidOCR()
doc = pymupdf.open(r"C:\Users\dharm\Downloads\infosys_sp_dse_questions_part2.csv")

# Missing list
target_ids = ['Q0596', 'Q0599', 'Q0609', 'Q0669', 'Q0696', 'Q0699', 'Q0709', 'Q0790', 'Q0799', 'Q0900', 'Q0906', 'Q0909']

# Estimate page: each page has ~10.5 items starting at Q0474
# Let's search pages around (target - 474) / 10.5
found_recoveries = {}
for target in target_ids:
    num = int(target[1:])
    est_page = int((num - 474) / 10.4)
    # Search est_page - 2 to est_page + 2
    for pno in range(max(0, est_page - 2), min(len(doc), est_page + 3)):
        page = doc[pno]
        pix = page.get_pixmap(dpi=150)
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        img_rot = img.transpose(Image.Transpose.ROTATE_270)
        tmp = f"test_{target}.png"
        img_rot.save(tmp)
        res, _ = engine(tmp)
        import os; os.remove(tmp)
        if not res: continue
        
        # Look for the number num or close patterns
        target_digits = f"{num:04d}"
        for bbox, text, score in res:
            # Check for digits
            if target_digits in text or str(num) in text or (re.search(r'[QO0-9]{5}', text) and target[2:] in text):
                found_recoveries[target] = (pno, text, score)
                break
        if target in found_recoveries:
            break

print("Recoveries found:", found_recoveries)
