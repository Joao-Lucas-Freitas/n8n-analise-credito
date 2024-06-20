import csv
import pandas as pd
from datetime import datetime
import math
import sys

def leitor(nome):

    input_file = 'saida.csv'
    output_file = 'dados.csv'

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
            if len(row) == 3:
                if 'Saldo' not in row[1] and 'Extrato' not in row[1] and 'SALDO' not in row[1]:
                    writer.writerow(row)

    df = pd.read_csv(output_file)

    inicio = df['Data'][0]
    fim = df['Data'][df['Data'].count()-1]

    date1 = datetime.strptime(inicio, '%d/%m/%Y')
    date2 = datetime.strptime(fim, '%d/%m/%Y')

    # Calcular a diferença em meses
    dias = (date2.year - date1.year) * 12 + (date2.month - date1.month) * 30 + date2.day - date1.day

    meses = int(math.ceil(dias / 30))
    
    if(meses == 0):
        meses = 1

    df_entradas = df[df['Valor'] > 0]
    df_saidas = df[df['Valor'] < 0]

    entrou = df_entradas['Valor'].sum()
    saiu = df_saidas['Valor'].sum()

    with open('resposta.txt', 'w') as file:
        original_stdout = sys.stdout
        sys.stdout = file

        print("\nNumero de entradas:", df_entradas['Valor'].count())
        print("Entrou:", entrou)
        print("Media de entradas por mes considerando", meses, "meses:", entrou / meses)

        print("\nNumero de saidas:", df_saidas['Valor'].count())
        print("Saiu:", saiu)
        print("Media de saidas por mes considerando", meses, "meses:", saiu / meses)

        print("\nSaldo do periodo:", entrou + saiu)
        print()

        transacoes_por_data = df.groupby('Data').size().reset_index(name='Numero de Transacoes')
        print(transacoes_por_data)

        print(transacoes_por_data['Numero de Transacoes'].sum())

        sys.stdout = original_stdout

#leitor('a')