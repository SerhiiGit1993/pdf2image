import fitz

pdf_file = "input.pdf"
output_folder = "output/"

pdf_document = fitz.open(pdf_file)

for page_number in range(pdf_document.page_count):
    page = pdf_document.load_page(page_number)
    image = page.get_pixmap(matrix=fitz.Matrix(300 / 72, 300 / 72))

    image_path = f"{output_folder}page_{page_number + 1}.png"
    image.save(image_path)

pdf_document.close()
