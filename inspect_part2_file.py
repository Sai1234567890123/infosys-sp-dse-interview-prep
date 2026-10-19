import os
import re

file_path = r"C:\Users\dharm\Downloads\infosys_sp_dse_questions_part2.csv"
print("File size:", os.path.getsize(file_path))

with open(file_path, "rb") as f:
    header = f.read(500)
    print("Header bytes:")
    print(header[:200])

# Check for streams and text in PDF
with open(file_path, "rb") as f:
    content = f.read(100000)
    titles = re.findall(rb'/Title \((.*?)\)', content)
    print("Titles in metadata:", titles)
    producer = re.findall(rb'/Producer \((.*?)\)', content)
    print("Producer:", producer)
    creator = re.findall(rb'/Creator \((.*?)\)', content)
    print("Creator:", creator)
