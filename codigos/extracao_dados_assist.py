from openai import OpenAI
from PyPDF2 import PdfReader
import time
import csv

def assistente(pdf_path):

    def extract_pages_to_strings(pdf_path):
        # Abre o arquivo PDF
        with open(pdf_path, "rb") as file:
            reader = PdfReader(file)
            num_pages = len(reader.pages)

            # Lista para armazenar o texto de cada página
            pages = []

            # Loop para extrair o texto de cada página
            for page_num in range(num_pages):
                page = reader.pages[page_num]
                page_text = page.extract_text()
                pages.append(page_text)

            return pages
        
    def novo_csv(path):
        with open(path, mode='w', newline='', encoding='utf-8'):
            pass   
        
    def escrever_csv(conteudo, path):
        with open(path, mode='a', newline='', encoding='utf-8') as arquivo_csv:
            escritor_csv = csv.writer(arquivo_csv)
            escritor_csv.writerow([conteudo])
        
    csv_path = "csvs/entrada.csv"
    novo_csv(csv_path)
    escrever_csv("Data,Descricao,Valor", csv_path)

    pages = extract_pages_to_strings(pdf_path)

    ID = ""

    client = OpenAI(api_key="")

    for page in pages:

        thread = client.beta.threads.create(
            messages=[
                {
                    'role': 'user',
                    'content': page
                }
            ]
        )

        run = client.beta.threads.runs.create(
            thread_id=thread.id, 
            assistant_id=ID
        )

        #print("Run Created")

        while run.status != 'completed':
            run = client.beta.threads.runs.retrieve(thread_id=thread.id, run_id=run.id)
            time.sleep(0.5)

        #print("Run Completed\n")

        message_response = client.beta.threads.messages.list(thread_id=thread.id)
        messages = message_response.data

        latest_message = messages[0]
        escrever_csv(latest_message.content[0].text.value, csv_path)


