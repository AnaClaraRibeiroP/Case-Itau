import pandas as pd
import numpy as np

# Caminho do arquivo original e caminho para salvar o arquivo auxiliar
file_path = r'c:\Users\aclarari\Desktop\NOVO CASE\DADOS\base_original.csv'
output_file = r'c:\Users\aclarari\Desktop\NOVO CASE\DADOS\base_auxiliar_director.csv'

# Carregar o arquivo CSV original
df = pd.read_csv(file_path)

# Inicializar um novo DataFrame para armazenar os dados finais
df_final = pd.DataFrame(columns=['show_id', 'director_in_cast', 'director', 'cast'])

# Iterar sobre as linhas do DataFrame original
for index, row in df.iterrows():
    # Verificar se há múltiplos diretores na linha atual
    if pd.notna(row['director']):
        directors = row['director'].split(', ')
    else:
        directors = [np.nan]  # Se não houver diretor especificado, colocar NaN
    
    for director in directors:
        # Verificar se o nome do diretor está presente na coluna 'cast'
        if pd.notna(row['cast']):
            cast = row['cast']
            show_id = row['show_id']
            if pd.notna(director) and director in cast:
                director_in_cast = 'YES'
                # Manter apenas o diretor que está presente na coluna 'cast'
                director_to_keep = director
            else:
                director_in_cast = 'NO'
                director_to_keep = np.nan
        else:
            cast = np.nan
            show_id = row['show_id']
            director_in_cast = 'NO'  # Se não houver informações de cast, considerar 'NO'
            director_to_keep = np.nan

        # Adicionar a linha ao DataFrame final
        df_final = pd.concat([df_final, pd.DataFrame({
            'show_id': [show_id],
            'director_in_cast': [director_in_cast],
            'director': [director_to_keep],
            'cast': [cast]
        })], ignore_index=True)

# Reordenar as colunas conforme especificado
df_final = df_final[['show_id', 'director_in_cast', 'director', 'cast']]

# Salvar o DataFrame modificado em um novo arquivo CSV
df_final.to_csv(output_file, index=False)

print(f'Arquivo base_auxiliar_director.csv salvo com sucesso em {output_file}')
