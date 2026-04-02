import pypandoc
import os

files = [
    "plot/chapters/prologue.md",
    "plot/chapters/chapter_01.md",
    "plot/chapters/chapter_02.md",
    "plot/chapters/chapter_03.md",
    "plot/chapters/chapter_04.md",
    "plot/chapters/chapter_05.md",
    "plot/chapters/chapter_06.md",
    "plot/chapters/chapter_07.md",
    "plot/chapters/chapter_08.md",
    "plot/chapters/chapter_09.md",
    "plot/chapters/chapter_10.md",
    "plot/chapters/chapter_11.md",
]

combined_md = ""

for f in files:
    if os.path.exists(f):
        with open(f, "r", encoding="utf-8") as file:
            content = file.read()
            # Ensure there is a page break or at least some spacing between chapters
            # Pandoc doesn't natively support page breaks in markdown without raw openxml, but we can try adding a pagebreak block
            combined_md += content + "\n\n\\newpage\n\n"

with open("combined.md", "w", encoding="utf-8") as f:
    f.write(combined_md)

# Convert to docx
output_filename = "Ksiazka.docx"
pypandoc.convert_file(
    "combined.md", "docx", outputfile=output_filename, extra_args=["--toc"]
)

print(f"Utworzono plik {output_filename}")
