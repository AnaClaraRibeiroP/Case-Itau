import pandas as pd

# Caminho do arquivo original e caminho para salvar o arquivo auxiliar
file_path = r'c:\Users\aclarari\Desktop\NOVO CASE\DADOS\base_original.csv'
output_file = r'c:\Users\aclarari\Desktop\NOVO CASE\DADOS\base_auxiliar_type.csv'

# Carregar o arquivo CSV original
df = pd.read_csv(file_path)

# Criar uma lista para armazenar os dados do DataFrame auxiliar
aux_data = []

# Iterar sobre as linhas do DataFrame original
for index, row in df.iterrows():
    # Verificar se a coluna 'type' não está vazia
    if pd.notna(row['type']):
        # Dividir os valores da coluna 'type' por vírgula
        types = row['type'].split(', ')
        # Para cada tipo, adicionar uma entrada com show_id e o tipo para aux_data
        for type_value in types:
            aux_data.append({'show_id': row['show_id'], 'type': type_value})

# Criar o DataFrame auxiliar a partir dos dados coletados
df_auxiliar = pd.DataFrame(aux_data)

# Salvar o DataFrame auxiliar em um novo arquivo CSV
df_auxiliar.to_csv(output_file, index=False)

print(f'Arquivo base_auxiliar_type.csv salvo com sucesso em {output_file}')




