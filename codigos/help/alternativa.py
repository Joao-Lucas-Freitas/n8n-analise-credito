import fitz  # PyMuPDF
import re
import pandas as pd

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text 

def preprocess_text(text):
    # Remover espaços extras e normalizar o texto
    text = re.sub(r'\s+', ' ', text)
    return text

def extract_transactions(text):
    # Ajuste da regex para capturar valores monetários com sinais explícitos
    transactions = re.findall(r'(\d{2}/\d{2}/\d{4}).*?([-+]?\d+,\d{2})', text)
    return transactions

def classify_transactions(transactions):
    classified_transactions = []
    for date, amount in transactions:
        print(date, amount)  # Verificar o valor extraído
        # Remover espaços e substituir vírgulas por pontos decimais
        amount = amount.replace('.', '').replace(',', '.')
        amount = float(amount)
        if amount < 0:
            classified_transactions.append((date, amount, 'saida'))
        else:
            classified_transactions.append((date, amount, 'entrada'))
    return classified_transactions

def aggregate_transactions(df):
    total_entradas = df[df['Tipo'] == 'entrada']['Valor'].sum()
    total_saidas = df[df['Tipo'] == 'saida']['Valor'].sum()
    return total_entradas, total_saidas

def main(pdf_path):
    text = extract_text_from_pdf(pdf_path)
    text = preprocess_text(text)
    transactions = extract_transactions(text)
    
    # Filtrar transações para remover saldos diários e garantir que os valores estejam corretos
    filtered_transactions = [t for t in transactions if not re.search(r'\bsaldo\b', t[0], re.IGNORECASE)]
    classified_transactions = classify_transactions(filtered_transactions)
    
    df = pd.DataFrame(classified_transactions, columns=['Data', 'Valor', 'Tipo'])
    total_entradas, total_saidas = aggregate_transactions(df)
    return df, total_entradas, total_saidas

# Exemplo de uso
pdf_path = 'extratos/brooklyn.pdf'
df, total_entradas, total_saidas = main(pdf_path)
print("Transações extraídas:")
print(df)
print("\nTotal de Entradas:", total_entradas)
print("Total de Saídas:", total_saidas)
