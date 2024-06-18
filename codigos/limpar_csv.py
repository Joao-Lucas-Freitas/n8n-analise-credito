import csv

def limpar():

    # Caminhos dos arquivos
    input_file_path = 'csvs/entrada.csv'
    middle_file_path = 'csvs/meio.csv'
    output_file_path = 'csvs/saida.csv'

    def limpar_csv(input_file, output_file):
        with open(input_file, 'r', newline='', encoding='utf-8') as csvfile, \
            open(output_file, 'w', newline='', encoding='utf-8') as csvoutput:
            
            reader = csv.reader(csvfile)
            writer = csv.writer(csvoutput)
            
            # Ler e escrever o cabeçalho
            header = next(reader)
            writer.writerow(header)
            
            # Processar as linhas do CSV
            for row in reader:
                # Limpar conteúdo de cada célula da linha
                cleaned_row = [cell.replace('```csv\n', '').replace('\n```', '').replace('`', '').replace('"', '') 
                            for cell in row]
                writer.writerow(cleaned_row)

    def limpar_aspas(input_file, output_file):
        # Ler o conteúdo do arquivo original
        with open(input_file, 'r', encoding='utf-8') as csvfile:
            content = csvfile.read()
        
        # Remover todas as aspas do conteúdo
        cleaned_content = content.replace('"', '')

        # Escrever o conteúdo limpo no arquivo de saída
        with open(output_file, 'w', newline='', encoding='utf-8') as csvoutput:
            csvoutput.write(cleaned_content)

    # Chamar a função para limpar o CSV
    limpar_csv(input_file_path, middle_file_path)
    limpar_aspas(middle_file_path, output_file_path)

    print(f"O arquivo CSV limpo foi salvo em: {output_file_path}")

#limpar()