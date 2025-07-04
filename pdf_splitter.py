from PyPDF2 import PdfReader, PdfWriter

# Load your PDF file (update the filename to your actual PDF in the same folder)
input_pdf = PdfReader("your_pdf_file.pdf")  # Example: "BSc_BT.pdf"

# Define chapter page ranges (1-indexed, inclusive)
# Format: "Chapter_Name": (start_page, end_page)
chapter_ranges = {
    "Chapter_1":  (3, 11),
    "Chapter_2":  (12, 21),
    "Chapter_3":  (22, 33),
    "Chapter_4":  (34, 45),
    "Chapter_5":  (46, 70),
    "Chapter_6":  (71, 79),
    "Chapter_7":  (80, 88),
    "Chapter_8":  (89, 108),
    "Chapter_9":  (109, 128),
    "Chapter_10": (129, 137),
}

# Iterate over each chapter and create a separate PDF file
for chapter_name, (start, end) in chapter_ranges.items():
    writer = PdfWriter()

    # PyPDF2 uses 0-based indexing, so subtract 1 from start
    for page_num in range(start - 1, end):
        writer.add_page(input_pdf.pages[page_num])

    # Save the chapter as a new PDF file
    output_filename = f"{chapter_name}.pdf"
    with open(output_filename, "wb") as output_file:
        writer.write(output_file)

    print(f"✅ Saved {output_filename}")

print("🎉 All chapters have been successfully split and saved.")
