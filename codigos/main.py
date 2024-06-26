from extracao_dados_assist import assistente
from leitorCSV import leitor
from limpar_csv import limpar
import time

def main():
    pdfs = []
    print('Seja bem vindo ao extrator de dados de extratos bancários!')
    print('Adicione o pdf na pasta extratos.')

    #pdf = input('Digite o nome do pdf: ')
    pdf = 'extratos/Maria Anthonia Gomes Mota.pdf'

    pdfs.append(pdf)
    
    for pdf in pdfs:
        nome = pdf.replace('.pdf', '')
        print(pdf, nome)
        assistente(pdf)
        limpar()
        leitor(nome)
    
if __name__ == "__main__":
    main()