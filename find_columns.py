from rapidocr_onnxruntime import RapidOCR
from PIL import Image

img = Image.open("page_1_correct_horizontal.png")
w, h = img.size
print(f"Image dimensions: width={w}, height={h}")

engine = RapidOCR()
res, _ = engine("page_1_correct_horizontal.png")

# Let's find header line (y < 350)
headers = []
for bbox, text, score in res:
    # bbox is [[x1, y1], [x2, y2], [x3, y3], [x4, y4]]
    xs = [pt[0] for pt in bbox]
    ys = [pt[1] for pt in bbox]
    min_x, max_x = min(xs), max(xs)
    min_y, max_y = min(ys), max(ys)
    if min_y < 350:
        headers.append((min_x, max_x, min_y, max_y, text))

headers.sort(key=lambda x: x[0])
print("Headers detected:")
for min_x, max_x, min_y, max_y, text in headers:
    print(f"X: [{min_x:.0f} - {max_x:.0f}], Y: [{min_y:.0f} - {max_y:.0f}] -> {text}")
