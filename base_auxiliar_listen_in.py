import pandas as pd

# Caminho do arquivo original e caminho para salvar o arquivo auxiliar
file_path = r'c:\Users\aclarari\Desktop\NOVO CASE\DADOS\base_original.csv'
output_file = r'c:\Users\aclarari\Desktop\NOVO CASE\DADOS\base_auxiliar_listed_in.csv'

# Carregar o arquivo CSV original
df = pd.read_csv(file_path)

# Criar uma lista para armazenar os dados do DataFrame auxiliar
aux_data = []

# Iterar sobre as linhas do DataFrame original
for index, row in df.iterrows():
    # Verificar se a coluna 'listed_in' não está vazia
    if pd.notna(row['listed_in']):
        # Dividir os valores da coluna 'listed_in' por vírgula
        listed_ins = row['listed_in'].split(', ')
        # Para cada listed_in, adicionar uma entrada com show_id e o listed_in para aux_data
        for listed_in_value in listed_ins:
            aux_data.append({'show_id': row['show_id'], 'listed_in': listed_in_value})

# Criar o DataFrame auxiliar a partir dos dados coletados
df_auxiliar = pd.DataFrame(aux_data)

# Salvar o DataFrame auxiliar em um novo arquivo CSV
df_auxiliar.to_csv(output_file, index=False)

print(f'Arquivo base_auxiliar_listed_in.csv salvo com sucesso em {output_file}')
