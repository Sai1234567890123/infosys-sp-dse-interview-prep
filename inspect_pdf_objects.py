import zlib
import re

file_path = r"C:\Users\dharm\Downloads\infosys_sp_dse_questions_part2.csv"
with open(file_path, "rb") as f:
    data = f.read()

# Let's find all object definitions in the PDF
obj_pattern = re.compile(rb'(\d+)\s+(\d+)\s+obj\r?\n(.*?)\r?\nendobj', re.DOTALL)
objects = obj_pattern.findall(data)
print(f"Total objects found: {len(objects)}")

types = {}
for obj_num, gen_num, body in objects:
    # check type
    m = re.search(rb'/Type\s*/(\w+)', body)
    t = m.group(1).decode('latin1') if m else "Unknown"
    types[t] = types.get(t, 0) + 1

print("Object types count:", types)

# Let's check the first few non-image streams
non_image_streams = []
for obj_num, gen_num, body in objects:
    if b'/Subtype /Image' not in body and b'stream' in body:
        sm = re.search(rb'stream\r?\n(.*?)\r?\nendstream', body, re.DOTALL)
        if sm:
            stream_data = sm.group(1)
            try:
                dec = zlib.decompress(stream_data)
                non_image_streams.append((obj_num.decode(), dec[:300]))
            except Exception as e:
                non_image_streams.append((obj_num.decode(), stream_data[:300]))

print(f"Non-image streams count: {len(non_image_streams)}")
for obj_id, preview in non_image_streams[:10]:
    print(f"--- Obj {obj_id} ---")
    print(preview[:150])
