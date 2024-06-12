import csv
import pandas as pd
from datetime import datetime

def leitor():

    input_file = 'csvs\saida.csv'
    output_file = 'csvs\dados_final.csv'

    # Abrir o arquivo CSV original e o novo arquivo para escrita
    with open(input_file, 'r', newline='', encoding='utf-8') as csvfile, open(output_file, 'w', newline='', encoding='utf-8') as csvoutput:
        reader = csv.reader(csvfile)
        writer = csv.writer(csvoutput)
        
        # Ler o cabeçalho e escrevê-lo no novo arquivo
        header = next(reader)
        writer.writerow(header)
        # Percorrer cada linha do arquivo CSV
        i = 1
        for row in reader:
            # Se a coluna 'Descrição' não contém 'Saldo do dia', escreva a linha no novo arquivo
            if len(row) > 0:
                if 'Saldo do dia' not in row[1]:
                    writer.writerow(row)

    df = pd.read_csv(output_file)

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

    # transacoes_por_data = df.groupby('Data').size().reset_index(name='Número de Transações')
    # print(transacoes_por_data)

    # print(transacoes_por_data['Número de Transações'].sum())