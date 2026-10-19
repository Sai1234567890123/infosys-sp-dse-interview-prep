import pymupdf

doc = pymupdf.open(r"C:\Users\dharm\Downloads\infosys_sp_dse_questions_part2.csv")
p = doc[0]

# Try 90 clockwise
pix_90 = p.get_pixmap(dpi=150, matrix=pymupdf.Matrix(pymupdf.Identity).prerotate(90))
pix_90.save("page_1_rot90.png")

# Try 270 (90 counter-clockwise)
pix_270 = p.get_pixmap(dpi=150, matrix=pymupdf.Matrix(pymupdf.Identity).prerotate(270))
pix_270.save("page_1_rot270.png")

print("Saved page_1_rot90.png and page_1_rot270.png")
