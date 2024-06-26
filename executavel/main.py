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