import re
import os

file_path = r"C:\Users\dharm\Downloads\infosys_sp_dse_questions_part2.csv"
with open(file_path, "rb") as f:
    data = f.read()

# Find image objects
img_pattern = re.compile(rb'(\d+)\s+0\s+obj\s*<<\s*.*?/Subtype\s*/Image.*?/Filter\s*/DCTDecode.*?stream\r?\n(.*?)\r?\nendstream', re.DOTALL)
matches = img_pattern.findall(data)
print(f"Found {len(matches)} DCTDecode (JPEG) images in PDF.")

out_dir = r"C:\Users\dharm\Downloads\infosysinterview\extracted_images"
os.makedirs(out_dir, exist_ok=True)

for i, (obj_id, img_bytes) in enumerate(matches[:5]):
    out_path = os.path.join(out_dir, f"img_{i+1}_obj_{obj_id.decode()}.jpg")
    with open(out_path, "wb") as f:
        f.write(img_bytes)
    print(f"Saved {out_path} ({len(img_bytes)} bytes)")
