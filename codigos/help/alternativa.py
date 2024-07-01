import fitz  # PyMuPDF

def extract_page_as_image(input_pdf, page_number, output_image_path):
    # Abre o arquivo PDF
    pdf_document = fitz.open(input_pdf)
    page = pdf_document.load_page(page_number - 1)  # As páginas são indexadas a partir de 0
    
    # Extrai a página como imagem
    pix = page.get_pixmap()
    pix.save(output_image_path)

def create_pdf_with_image(image_path, output_pdf_path):
    # Cria um novo PDF
    new_pdf = fitz.open()
    img_doc = fitz.open(image_path)
    pdf_bytes = img_doc.convert_to_pdf()
    img_pdf = fitz.open("pdf", pdf_bytes)
    new_pdf.insert_pdf(img_pdf)
    
    # Salva o novo PDF
    new_pdf.save(output_pdf_path)
    new_pdf.close()

# Exemplo de uso
input_pdf = "extratos/1.pdf"
output_image = "extratos/imagem.png"
output_pdf = "extratos/1-correto.pdf"
page_number = 3  # Página que você deseja extrair

# Extrai a página 3 como imagem
extract_page_as_image(input_pdf, page_number, output_image)

# Cria um novo PDF com a imagem extraída
create_pdf_with_image(output_image, output_pdf)

print(f"Novo PDF com a página {page_number} salva em: {output_pdf}")
