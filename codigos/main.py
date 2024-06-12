from extracao_dados_assist import assistente
from leitorCSV import leitor
from limpar_csv import limpar

def main():
    assistente()
    limpar()
    leitor()
    

if __name__ == "__main__":
    main()