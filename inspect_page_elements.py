import pymupdf

doc = pymupdf.open(r"C:\Users\dharm\Downloads\infosys_sp_dse_questions_part2.csv")
page = doc[0]

print("Fonts on page 1:", page.get_fonts())
print("Text blocks:", page.get_text("blocks"))
print("Drawings count:", len(page.get_drawings()))
print("Words count:", len(page.get_text("words")))
