import pandas as pd

file_path = 'clientes-centro-comercial.csv'

df = pd.read_csv(file_path)

num_rows = df.shape[0]
headers = df.columns.tolist()

print(f'Numero de filas: {num_rows}')
print(f'Headers columnas: {headers}')

# Sacar el minimo y maximo por genero de la edad,ingresos y puntos de compra
min_por_genero = df.groupby('Genero').agg({
    'Edad': 'min',
    'Ingresos Anuales (k$)': 'min',
    'Puntos en compras (1-100)': 'min'
})

max_por_genero = df.groupby('Genero').agg({
    'Edad': 'max',
    'Ingresos Anuales (k$)': 'max',
    'Puntos en compras (1-100)': 'max'
})

print("\n\nMinimum por Genero:")
print(min_por_genero)

print("\n\nMaximum por Genero:")
print(max_por_genero)

media = df.groupby('Genero').mean()
mediana = df.groupby('Genero').median()
desviacion_estandar = df.groupby('Genero').std()

print("Media:")
print(media)

print("\n\nMediana:")
print(mediana)

print("\n\nDesviación Estándar:")
print(desviacion_estandar)