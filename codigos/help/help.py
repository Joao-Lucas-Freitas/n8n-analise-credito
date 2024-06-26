import pdfplumber


def extract_pages_to_strings(pdf_path):
        pages = []
        try:
            with pdfplumber.open(pdf_path) as pdf:
                for page in pdf.pages:
                    pages.append(page.extract_text())
        except Exception as e:
            print(f"An error occurred: {e}")
        return pages

pages = extract_pages_to_strings('extratos/Icaro.pdf')
i = 0
for page in pages:
    i+=1
    if(i == 13):
        print("Pagina:",i)
        print(page)
