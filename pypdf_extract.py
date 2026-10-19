import pypdf
import sys

file_path = r"C:\Users\dharm\Downloads\infosys_sp_dse_questions_part2.csv"

reader = pypdf.PdfReader(file_path)
print(f"Total pages: {len(reader.pages)}")
print("Metadata:", reader.metadata)

# Check if there are attachments / embedded files in the PDF
attachments = {}
try:
    if reader.attachments:
        print("Attachments found:", list(reader.attachments.keys()))
        for name, content in reader.attachments.items():
            print(f"Attachment {name}: {len(content)} bytes")
except Exception as e:
    print("Attachments check error:", e)

# Extract text from first 5 pages
for i in range(min(5, len(reader.pages))):
    page = reader.pages[i]
    text = page.extract_text()
    print(f"--- PAGE {i+1} (length: {len(text)}) ---")
    if text:
        print(text[:300])
    else:
        print("[EMPTY TEXT]")
