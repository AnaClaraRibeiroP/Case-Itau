import pandas as pd

# Caminho do arquivo original e caminho para salvar o arquivo auxiliar
file_path = r'c:\Users\aclarari\Desktop\NOVO CASE\DADOS\base_original.csv'
output_file = r'c:\Users\aclarari\Desktop\NOVO CASE\DADOS\base_auxiliar_country.csv'

# Carregar o arquivo CSV original
df = pd.read_csv(file_path)

# Criar uma lista para armazenar os dados do DataFrame auxiliar
aux_data = []

# Iterar sobre as linhas do DataFrame original
for index, row in df.iterrows():
    # Verificar se a coluna 'country' não está vazia
    if pd.notna(row['country']):
        # Dividir os nomes da coluna 'country' por vírgula
        names = row['country'].split(', ')
        # Para cada nome, adicionar uma entrada com show_id e o nome para aux_data
        for name in names:
            aux_data.append({'show_id': row['show_id'], 'country': name})

# Criar o DataFrame auxiliar a partir dos dados coletados
df_auxiliar = pd.DataFrame(aux_data)

# Salvar o DataFrame auxiliar em um novo arquivo CSV
df_auxiliar.to_csv(output_file, index=False)

print(f'Arquivo base_auxiliar_country.csv salvo com sucesso em {output_file}')
