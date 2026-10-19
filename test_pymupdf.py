import fitz # PyMuPDF
import os

pdf_path = r"C:\Users\dharm\Downloads\infosys_sp_dse_questions_part2.csv"
doc = fitz.open(pdf_path)
print(f"Total pages: {len(doc)}")

# Check text extraction
for pno in range(min(5, len(doc))):
    page = doc[pno]
    text = page.get_text()
    print(f"Page {pno+1} text length: {len(text)}")
    if text.strip():
        print(f"Text sample: {text[:200]}")

# Render page 1 and page 2 to PNG images
pix1 = doc[0].get_pixmap(dpi=150)
pix1.save("page_1.png")
print("Saved page_1.png")

pix2 = doc[1].get_pixmap(dpi=150)
pix2.save("page_2.png")
print("Saved page_2.png")
