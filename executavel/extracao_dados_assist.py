from openai import OpenAI
import pdfplumber
import time
import csv
from dotenv import load_dotenv
import os

def assistente(pdf_path):

    def extract_pages_to_strings(pdf_path):
        pages = []
        try:
            with pdfplumber.open(pdf_path) as pdf:
                for page in pdf.pages:
                    pages.append(page.extract_text())
        except Exception as e:
            print(f"An error occurred: {e}")
        return pages
        
    def novo_csv(path):
        with open(path, mode='w', newline='', encoding='utf-8'):
            pass   
        
    def escrever_csv(conteudo, path):
        with open(path, mode='a', newline='', encoding='utf-8') as arquivo_csv:
            escritor_csv = csv.writer(arquivo_csv)
            escritor_csv.writerow([conteudo])
        
    csv_path = "entrada.csv"
    novo_csv(csv_path)
    escrever_csv("Data,Descricao,Valor", csv_path)

    pages = extract_pages_to_strings(pdf_path)

    load_dotenv()

    api_key = os.getenv('API_KEY')

    ID = os.getenv('ASSIST_ID')

    client = OpenAI(api_key=api_key)

    i = 0
    for page in pages:
        i+=1
        print("Pagina:", i)

        # print(page)

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

        if messages:
            latest_message = messages[0]
            if latest_message:
                if latest_message.content:
                    escrever_csv(latest_message.content[0].text.value, csv_path)
        else:
            print("No messages found.")
        


