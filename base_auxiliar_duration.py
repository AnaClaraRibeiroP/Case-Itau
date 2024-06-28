import pandas as pd

# Caminho do arquivo original e caminho para salvar o arquivo auxiliar
file_path = r'c:\Users\aclarari\Desktop\NOVO CASE\DADOS\base_original.csv'
output_file = r'c:\Users\aclarari\Desktop\NOVO CASE\DADOS\base_auxiliar_duration.csv'

# Carregar o arquivo CSV original
df = pd.read_csv(file_path)

# Inicializar listas para armazenar os dados das novas colunas
movie_durations = []
tv_show_temps = []
titles = []
show_ids = []

# Iterar sobre as linhas do DataFrame original
for index, row in df.iterrows():
    # Inicializar variáveis para armazenar os valores de movie_duration e tv_show_temps
    movie_duration = None
    tv_show_temp = None
    
    # Verificar se a coluna 'duration' não está vazia
    if pd.notna(row['duration']):
        # Dividir o valor da coluna 'duration' para separar números e texto
        parts = row['duration'].split()
        if len(parts) == 2:  # Caso típico: '1 Season' ou '2 Seasons'
            num = int(parts[0])  # Extrair o número
            unit = parts[1]  # Extrair a unidade (Season ou Seasons)
            if unit == 'Season' or unit == 'Seasons':
                tv_show_temp = num
            else:
                movie_duration = num
    
    # Adicionar os valores para a linha atual
    movie_durations.append(movie_duration)
    tv_show_temps.append(tv_show_temp)
    titles.append(row['title'])
    show_ids.append(row['show_id'])

# Criar o DataFrame final com as colunas desejadas
df_final = pd.DataFrame({
    'show_id': show_ids,
    'title': titles,
    'movie_duration(min)': movie_durations,
    'tv_show_duration(temp)': tv_show_temps
})

# Salvar o DataFrame modificado em um novo arquivo CSV
df_final.to_csv(output_file, index=False)

print(f'Arquivo base_auxiliar_duration.csv salvo com sucesso em {output_file}')
