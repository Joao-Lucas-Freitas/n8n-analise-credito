from extracao_dados_assist import assistente
from leitorCSV import leitor
from limpar_csv import limpar

def main():

    pdfs = ['extratos/Icaro Moreira Pazini.pdf', 'extratos/brooklyn role play.pdf', 'extratos/Maria Anthonia Gomes Mota.pdf']
    #pdfs = ['extratos/Maria Anthonia Gomes Mota.pdf']
    for pdf in pdfs:
        nome = pdf.replace('extratos/', '').replace('.pdf', '') 
        print(pdf, nome)
        assistente(pdf)
        limpar()
        leitor(nome)
    

if __name__ == "__main__":
    main()