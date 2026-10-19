import zlib
import re

file_path = r"C:\Users\dharm\Downloads\infosys_sp_dse_questions_part2.csv"
with open(file_path, "rb") as f:
    data = f.read()

stream_pattern = re.compile(rb'stream\r?\n(.*?)\r?\nendstream', re.DOTALL)
streams = stream_pattern.findall(data)
print(f"Total streams found: {len(streams)}")

decompressed_texts = []
for i, s in enumerate(streams):
    try:
        decompressed = zlib.decompress(s)
        # Check if decompressed contains ASCII text strings
        text_chunks = re.findall(rb'\(([^\(\)]{3,})\)', decompressed)
        if text_chunks:
            sample = [t.decode('latin1', 'ignore') for t in text_chunks[:5]]
            decompressed_texts.append((i, len(text_chunks), sample))
    except Exception:
        pass

print(f"Streams with text strings: {len(decompressed_texts)}")
for idx, count, sample in decompressed_texts[:10]:
    print(f"Stream {idx}: {count} text strings -> {sample}")
