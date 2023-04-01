import pandas as pd

ruta="D:\\curso de python\\Datos\\python_data\\final\\pregunta1\dic\\paises.csv"
datos=pd.read_csv(ruta,header=0)
df=pd.DataFrame(datos)

print(df)


