import pandas as pd

# Definir o caminho dos arquivos
file_path = r'c:\Users\aclarari\Desktop\NOVO CASE\DADOS\base_original.csv'
output_file_path = r'c:\Users\aclarari\Desktop\NOVO CASE\DADOS\base_auxiliar_data.csv'

# Ler o arquivo CSV original
df = pd.read_csv(file_path)

# Converter a coluna date_added para datetime e extrair o ano
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')
df['year_added'] = df['date_added'].dt.year

# Calcular a diferença entre release_year e year_added
df['year_difference'] = df['year_added'] - df['release_year'] 

# Criar a nova tabela auxiliar com show_id, release_year, date_added e year_difference
aux_df = df[['show_id', 'release_year', 'date_added', 'year_difference']]

# Salvar a nova tabela auxiliar em um novo arquivo CSV
aux_df.to_csv(output_file_path, index=False)

print(f"A nova tabela auxiliar foi salva em {output_file_path}")
