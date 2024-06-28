from extracao_dados_assist import assistente
from leitorCSV import leitor
from limpar_csv import limpar
import time

def main():
    pdfs = []
    print('Seja bem vindo ao extrator de dados de extratos bancários!')
    print('Adicione o pdf na pasta extratos.')
    print('Nome de exemplo a ser digitado: Icaro')

    pdf = input('Digite o nome do pdf: ')
    pdf = pdf + '.pdf'

    pdfs.append(pdf)
    
    for pdf in pdfs:
        nome = pdf.replace('.pdf', '')
        print(pdf, nome)
        assistente(pdf)
        limpar()
        leitor(nome)

    print('\nResultados em resultados.txt na pasta do programa\n')
    print('Lembre de abrir de fechar a aba de resultados e abrir de novo para atualizar o arquivo!')
    input('Digite enter para encerrar o programa')
    
if __name__ == "__main__":
    main()


    texto = "15/04/2024,Pix enviado Raelly Martins Goncalves,-20.00/\n15/04/2024,Pix recebido Leonardo Vanzeler Cardoso,20.00/\n15/04/2024,Pix enviado Raelly Martins Goncalves,-20.00/\n15/04/2024,Pix recebido Leonardo Vanzeler Cardoso,20.00/\n15/04/2024,Pix enviado Raelly Martins Goncalves,-10.00/\n15/04/2024,Pix recebido Risomar Cardoso Da Silva,10.00/\n15/04/2024,Pix enviado Raelly Martins Goncalves,-10.00/\n15/04/2024,Pix recebido Alzeni Monteiro Cardoso,10.00/\n15/04/2024,Pix enviado Jamili Nascimento Salles,-1.90/\n15/04/2024,Pix enviado Raelly Martins Goncalves,-20.00/\n15/04/2024,Pix enviado Kiwify,-67.00/\n15/04/2024,Pix enviado Uber Do Brasil Tecnologia Ltda,-5.42/\n15/04/2024,Compra no débito Panificadora Panini Macapa Bra,-2.25"
    valores = texto.split('\n')
    valores

    def extract_values(text):
    # Use regex para encontrar todos os valores numéricos no texto
    values = re.findall(r'[-]?\d+\.\d+', text)
    # Converta os valores para float e some
    total = sum(float(value) for value in values)
    return total

for item in _input.all():
    # Supondo que o texto das transações está em item.json['transactionText']
    transaction_text = item.json['text']
    item.json['totalValue'] = extract_values(transaction_text)