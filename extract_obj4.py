import re

file_path = r"C:\Users\dharm\Downloads\infosys_sp_dse_questions_part2.csv"
with open(file_path, "rb") as f:
    data = f.read()

# Find obj 4
idx = data.find(b"4 0 obj")
stream_idx = data.find(b"stream\n", idx)
if stream_idx == -1:
    stream_idx = data.find(b"stream\r\n", idx)
    stream_start = stream_idx + len("stream\r\n")
else:
    stream_start = stream_idx + len("stream\n")

# Length is 113394
length_match = re.search(r'/Length\s+(\d+)', data[idx:stream_idx].decode('latin1'))
length = int(length_match.group(1))
img_data = data[stream_start:stream_start+length]

with open("obj4_page1.jpg", "wb") as f:
    f.write(img_data)
print(f"Saved obj4_page1.jpg with {len(img_data)} bytes.")
