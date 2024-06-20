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
        time.sleep(1)
        print(pdf, nome)
        time.sleep(3)
        assistente(pdf)
        time.sleep(5)
        limpar()
        time.sleep(5)
        leitor(nome)
        time.sleep(5)

    print('\nResultados em resultados.txt na pasta do programa\n')
    input('Digite enter para encerrar o programa')
    
if __name__ == "__main__":
    main()