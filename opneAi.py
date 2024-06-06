import openai
import csv
import pandas as pd
from datetime import datetime

# Configure sua chave de API da OpenAI
openai.api_key = ''

def pdf_to_csv(pdf_path):
    # Abra o arquivo PDF e leia o conteúdo
    with open(pdf_path, 'rb') as pdf_file:
        pdf_content = pdf_file.read()

    # Converta o conteúdo PDF em texto CSV usando a API da OpenAI
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": """
            Você é um assistente financeiro que recebe extratos e me ajuda a converter esses extratos para texto em formato csv que contenham todas as transações.
            Você só precisa escrever em texto mesmo em csv que e deve ter Data, Descrição, Valor (para o valor, se ele estiver usando vírgula troque por ponto)
            De forma que todas as transações estejam mapeadas nesse texto em forma csv.
            Sua única resposta deve ser esse arquivo, não fale mais nada.
            """},
            {"role": "user", "content": pdf_content.decode('utf-8')}
        ]
    )

    csv_text = response['choices'][0]['message']['content'].strip()
    return csv_text

def process_csv(input_csv_text, output_csv_file):
    input_file = 'temp_input.csv'
    with open(input_file, 'w', encoding='utf-8') as f:
        f.write(input_csv_text)

    with open(input_file, 'r', newline='', encoding='utf-8') as csvfile, open(output_csv_file, 'w', newline='', encoding='utf-8') as csvoutput:
        reader = csv.reader(csvfile)
        writer = csv.writer(csvoutput)

        # Ler o cabeçalho e escrevê-lo no novo arquivo
        header = next(reader)
        writer.writerow(header)

        # Percorrer cada linha do arquivo CSV
        for row in reader:
            # Se a coluna 'Descrição' não contém 'Saldo do dia', escreva a linha no novo arquivo
            if 'Saldo do dia' not in row[1]:
                writer.writerow(row)

    df = pd.read_csv(output_csv_file)

    inicio = df['Data'][0]
    fim = df['Data'][df['Data'].count()-1]

    date1 = datetime.strptime(inicio, '%d/%m/%Y')
    date2 = datetime.strptime(fim, '%d/%m/%Y')

    # Calcular a diferença em meses
    meses = (date2.year - date1.year) * 12 + date2.month - date1.month

    df_entradas = df[df['Valor'] > 0]
    df_saidas = df[df['Valor'] < 0]

    entrou = df_entradas['Valor'].sum()
    saiu = df_saidas['Valor'].sum()

    print("\nNúmero de entradas:", df_entradas['Valor'].count())
    print("Entrou:", entrou)
    print("Média de entradas por mês considerando", meses, "meses:", entrou / meses)

    print("\nNúmero de saídas:", df_saidas['Valor'].count())
    print("Saiu:", saiu)
    print("Média de saídas por mês considerando", meses, "meses:", saiu / meses)

    print("\nSaldo do período:", entrou + saiu)
    print()

# Caminho para o seu PDF
pdf_path = 'extratos/brooklyn role play.pdf'

# Caminho para o CSV de saída
output_csv_file = 'gpt_filtrado.csv'

# Converta o PDF em CSV
csv_text = pdf_to_csv(pdf_path)

# Processe o CSV gerado
process_csv(csv_text, output_csv_file)
