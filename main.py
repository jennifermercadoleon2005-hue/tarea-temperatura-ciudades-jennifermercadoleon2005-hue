# JENNIFER GUADALUPE MERCADO LEON 
# GRUPO 3
# 30/11/2025

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data.csv")

# Ver tipos de datos de las columnas
print(df.dtypes)

# Convertir la columna 'Datetime' a tipo datetime
df['Datetime'] = pd.to_datetime(df['Datetime'])
# Establecer la columna 'Date' como índice del DataFrame
df.set_index('Datetime', inplace=True)

# TODO: Crear funcion para convertir de grados Kelvin a Celsius
def kelvin_to_celsius(kelvin):

    c:= kelvin - 273.15
    return c

# TODO: Copiar el DataFrame original y nombralo df_celsius
df_celsius:= df.copy[]

# TODO: Convertir las temperaturas de cada ciudad de Kelvin a Celsius usando la funcion creada
df_celsius["San Diego"] = df["San Diego"].apply(kelvin_to_celsius)
df_celsius["Phoenix"] = df["Phoenix"].apply(kelvin_to_celsius)
df_celsius["Toronto"] = df["Toronto"].apply(kelvin_to_celsius)
# Analisis

# TODO: Imprime que día y hora se registró la temperatura mínima en Phoenix con el siguiente mensaje: "El día con la temperatura mínima en Phoenix fue: {fecha}"
i_min = df_celsius['Phoenix'].idxmin()
i_min=i_min.round(2)
print("El dia con la temperatura minima en Phoenix fue:" i_min)

# TODO: Imprime la temperatura mínima en Phoenix con el siguiente mensaje: "La temperatura mínima registrada en Phoenix fue de: ", temperatura, " °C""

valorMinimo = df_celsius['Phoenix'][i_min]
print("La temperatura mínima registrada en Phoenix fue de: ", valorMinimo, " °C")


# TODO: Imprime que día y hora se registró la temperatura máxima en Phoenix con el siguiente mensaje: "El día con la temperatura máxima en Phoenix fue: {fecha}"
i_max = df_celsius['Phoenix'].idxmax()
i_max=i_max.round(2)
print("El dia con la temperatura maxima en Phoenix fue:" i_max)

# TODO: Imprime la temperatura máxima en Phoenix con el siguiente mensaje: "La temperatura máxima registrada en Phoenix fue de: ", temperatura, " °C""
valorMaximo = df_celsius['Phoenix'][i_max]
print("La temperatura maxima registrada en Phoenix fue de: ", valorMaximo, " °C")

# TODO: Imprime la temperatura promedio en Phoenix durante el año 2016 con el siguiente mensaje: "La temperatura promedio durante 2016 en Phoenix fue de: ", temperatura, " °C""
promedio = df_celsius["Phoenix"].mean()
print(f"La temperatura promedio durante 2016 en Phoenix fue de: {promedio:.1f} °C")

# Graficar la temperatura de Phoenix durante el año 2016
plt.figure(figsize=(20, 10))
plt.scatter(df_celsius.index, df_celsius['Phoenix'], label='Phoenix')
plt.title('Temperatura en Phoenix durante 2016')
plt.xlabel('Fecha')
plt.ylabel('Temperatura (°C)')
plt.legend()
plt.grid()
plt.savefig("temperatura_phoenix_2016.png")
plt.show()

# Exportar el DataFrame modificado a un nuevo archivo CSV
df_celsius.to_csv("temperatura_celsius.csv")


