'''
Ejercicio 5.1
Conseguimos el Dataset de Auto MPG que contiene datos del consumo de combustible de diversos modelos de coches.

5.1.1 Dibuja una gráfica que muestre la relación entre las variables del dataset.
5.1.2 ¿Entre qué conjunto de variables se puede considerar que hay una relación?
5.1.3 Calcula el coeficiente de correlación entre las variables del dataset y dibújalos en una gráfica. Modifica la respuesta del paso anterior si lo consideras necesario según los coeficientes calculados.
5.1.4 Dibuja un diagrama de dispersión entre el peso y la potencia, pintando los puntos del gráfico según el número de cilindros.
5.1.5 Dibuja un diagrama de dispersión entre el peso y la potencia, pintando los puntos del gráfico según el año de fabricación. Comparando este nuevo gráfico con el anterior, ¿podemos decir qué criterio tiene más capacidad para agrupar los coches o mejor dicho es un factor discriminatorio mayor que el otro?
5.1.6 Saca el mismo gráfico que dibujaste en el ejercicio 5.1.5, esta vez solamente para los coches fabricados en el año 70.
5.1.7 Saca el mismo gráfico que dibujaste en el ejercicio 5.1.5, esta vez solamente para los coches fabricados en el año 80. ¿Cuáles son las diferencias más destacables entre las relaciones dibujadas del año 70 y del año 80?

'''
#5.1.1
import pandas as pd

df = pd.read_csv('auto-mpg.csv')
print(df.head)