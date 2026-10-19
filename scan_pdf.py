import re

file_path = r"C:\Users\dharm\Downloads\infosys_sp_dse_questions_part2.csv"
with open(file_path, "rb") as f:
    data = f.read()

pages = re.findall(rb'/Type\s*/Page\b', data)
print(f"Number of /Page objects: {len(pages)}")

images = re.findall(rb'/Subtype\s*/Image\b', data)
print(f"Number of /Image objects: {len(images)}")

# Check if there is any text stream or fonts
fonts = re.findall(rb'/Type\s*/Font\b', data)
print(f"Number of /Font objects: {len(fonts)}")

text_streams = re.findall(rb'/Filter\s*/FlateDecode', data)
print(f"FlateDecode streams: {len(text_streams)}")
