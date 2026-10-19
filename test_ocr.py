from rapidocr_onnxruntime import RapidOCR
import sys

engine = RapidOCR()
result, elapse = engine("page_1.png")

print(f"Elapsed: {elapse} s")
print(f"Detected {len(result) if result else 0} text elements.")

if result:
    for bbox, text, score in result[:25]:
        print(f"[{score:.2f}] {text} (y: {bbox[0][1]:.1f})")
