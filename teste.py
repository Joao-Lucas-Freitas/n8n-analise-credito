import PyPDF2
import re
import csv
import pandas as pd
from datetime import datetime

# Função para extrair texto do PDF
def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
    return text

# Regex pattern para capturar data, descrição e valor
pattern = re.compile(r'(\d{2}/\d{2}/\d{4})\s+(.+?)\s+(-?\s*R\$\s*[\d.,]+)')

# Função para separar linhas combinadas
def separate_combined_lines(text):
    lines = text.split('\n')
    separated_lines = []
    for line in lines:
        # Verifica se a linha contém mais de uma data
        matches = pattern.findall(line)
        if len(matches) > 1:
            for match in matches:
                date, description, value = match
                separated_lines.append(f"{date} {description} {value}")
        elif len(matches) == 1:
            date, description, value = matches[0]
            separated_lines.append(f"{date} {description} {value}")
        else:
            separated_lines.append(line)
    return separated_lines

# Função para processar o texto extraído com filtro
def process_text(text):
    lines = separate_combined_lines(text)
    extracted_data = []
    for line in lines:
        match = pattern.match(line)
        if match:
            date = match.group(1)
            description = match.group(2)
            value = match.group(3)
            # Adicione aqui a lógica para filtrar as linhas indesejadas
            if should_include_line(date, description, value):
                extracted_data.append([date, description, value])
    return extracted_data

# Função para decidir se uma linha deve ser incluída
def should_include_line(date, description, value):
    if "Saldo do dia" in description:
        return False
    return True

# Função para salvar os dados extraídos em um arquivo CSV
def save_to_csv(data, csv_path):
    with open(csv_path, 'w', newline='', encoding='utf-8') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(['Data', 'Descrição', 'Valor'])
        csvwriter.writerows(data)

# Caminho para o arquivo PDF e CSV
pdf_path = 'extratos/brooklyn role play.pdf'
csv_path = 'transacoes.csv'

# Extração, processamento e salvamento
text = extract_text_from_pdf(pdf_path)
data = process_text(text)
save_to_csv(data, csv_path)

# Criar um DataFrame com os dados extraídos
df = pd.DataFrame(data, columns=['Data', 'Descrição', 'Valor'])
inicio = df['Data'][0]
fim = df['Data'][df['Data'].count()-1]

date1 = datetime.strptime(inicio, '%d/%m/%Y')
date2 = datetime.strptime(fim, '%d/%m/%Y')

# Calcular a diferença em meses
meses = (date2.year - date1.year) * 12 + date2.month - date1.month
# Remover o símbolo de moeda e converter para float
df['Valor'] = df['Valor'].str.replace(r'[^\d,-]', '', regex=True).str.replace(',', '.').astype(float)

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

print("\nSaldo atual:", entrou + saiu)
print()

transacoes_por_data = df.groupby('Data').size().reset_index(name='Número de Transações')
print(transacoes_por_data)
