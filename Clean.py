import pandas as pd

df = pd.read_csv('GamingStudy_data.csv', encoding = 'utf-8', index_col = 0)

print('Header:\n', df.head())
print('Descripción:\n', df.describe().T, '\n')

list = list(df.columns)
print('Columnas:\n', list, '\n')
print('Tipos:\n', df.dtypes, '\n')

print('Valores Nulos en Total:\n', df.isnull().sum(), '\n')
percent_missing = df.isnull().sum() * 100 / len(df)
missing_value_df = pd.DataFrame({'Columna': df.columns,
                                 'Porcentaje de Valores Nulos': percent_missing})
print('Porcentaje de Valores Nulos por Columna:\n', missing_value_df, '\n')

# COLUMNAS DE TIPO STRING
# - Eliminar espacios en blanco al inicio
# - Llenar valores nulos
str_cols = df.select_dtypes('object')
for i in str_cols:
    df[i] = df[i].map(lambda x: x.strip() if isinstance(x, str) else x)
    df[i] = df[i].fillna('None')

'''
# - Identificar valores únicos
for i in str_cols:
    print(i, df[i].unique())
'''

# COLUMNAS DE TIPO NUMÉRICO
# - Llenar valores nulos
num_cols = df.select_dtypes(include=['number']).columns
for i in num_cols:
    df[i] = df[i].fillna(-1)

# Capitalizar los nombres de algunas columnas
df.columns = df.columns.str.replace('earnings', 'Earnings')
df.columns = df.columns.str.replace('whyplay', 'WhyPlay')
df.columns = df.columns.str.replace('highestleague', 'HighestLeague')
df.columns = df.columns.str.replace('streams', 'Streams')
df.columns = df.columns.str.replace('accept', 'Accept')

# Capitalizar los valores de algunas columnas
df['Earnings'] = df['Earnings'].str.capitalize()
df['WhyPlay'] = df['WhyPlay'].str.capitalize()
df['League'] = df['League'].str.capitalize()

# Identificar y reemplazar símbolos desconocidos
df['Degree'].loc[df['Degree'].str.contains('Bachelor')] = "Bachelor's (or equivalent)"
df['Degree'].loc[df['Degree'].str.contains('Master')] = "Master's (or equivalent)"
df['Birthplace'].loc[df['Birthplace'].str.contains('Cura')] = 'Curaçao'

df.to_csv('output.csv')
