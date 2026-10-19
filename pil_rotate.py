from PIL import Image

img = Image.open("page_1.png")
# Rotate 270 degrees clockwise (90 counter-clockwise)
rot270 = img.transpose(Image.Transpose.ROTATE_270)
rot270.save("page_1_correct_horizontal.png")

# Also test ROTATE_90 just in case
rot90 = img.transpose(Image.Transpose.ROTATE_90)
rot90.save("page_1_other_rot.png")

print("Saved rotated images with PIL.")
