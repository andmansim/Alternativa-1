'''
Ejercicio 5.2
En un restaurante, un camarero registró los siguientes datos sobre todos los clientes durante un intervalo de 
dos meses y medio a principios de 1990.
El restaurante, ubicado en un centro comercial suburbano, era parte de una cadena nacional y 
servía un menú variado. En cumplimiento de la ley local, el restaurante ofrecía además sentarse en una sección 
para no fumadores a los clientes que así lo solicitaban.

5.2.1 Saca todas las estadísticas principales de las variables del dataset.
5.2.2 Comprueba si hay valores perdidods en el dataset y si fuera así en qué registros existen estos valores.

5.2.3 Clacula qué porcentaje de los clientes que dan propina son hombres y qué porcentaje son mujeres?
5.2.4 Agrupa los datos según estas variables, calculando el tamaño, la mediana y la media para cada grupo:

'sex'
'smoker'
'day'
'time'
'size'
5.2.5 Dibuja una gráfica que muestre para cada grupo de personas servidas en el restaurante, el promedio de las propinas pagadas.
5.2.6 Dibuja una gráfica que muestre la relación entre las variables del dataset, pintando los datos según las siguientes variables:

'sex'
'smoker'
'day'
'time'
'size'
5.2.7 Teniendo en cuenta todos los calculos realizados sobre este dataset y las gráficas dibujadas anteriormente, ¿cuáles serían los factores diferenciadores que más afectan a la cantidad de las proponia recibidas por el camarero?
5.2.8 Calcula el tercer cuartil para la variable 'tip' y filtra todo el dataset según este valor para que el DataFrame resultante solamente contenga valores iguales o mayores que esa cantidad de propinas.
5.2.9 Dibuja los histogramas que se pueden obtener para las siguientes variables del dataset obtenido en el paso anterior:

'smoker'
'day'
'time'
'size'
5.2.10 Considerando todo el análisis realizado anteriormente, haz una recomendación al camarero para que lo tenga en cuenta a la hora de repartir los clientes entre el personal del restaurante, y muestra que de esa manera él puede conseguir mayor cantidad de proponas!!

'''
import pandas as pd
#5.2.1 Saca todas las estadísticas principales de las variables del dataset.

df = pd.read_csv('tips.csv')
print(df.head())
print('\nInfromación del df\n')
print(df.info())
print('\nColumnas del df\n')
print(df.columns)
print('\nDescripción básica del df\n')
print(df.describe)

#5.2.2 Comprueba si hay valores perdidods en el dataset y si fuera así en qué registros existen estos valores.

#5.2.3 Clacula qué porcentaje de los clientes que dan propina son hombres y qué porcentaje son mujeres?
#5.2.4 Agrupa los datos según estas variables, calculando el tamaño, la mediana y la media para cada grupo:

'sex'
'smoker'
'day'
'time'
'size'
#5.2.5 Dibuja una gráfica que muestre para cada grupo de personas servidas en el restaurante, el promedio de las propinas pagadas.
#5.2.6 Dibuja una gráfica que muestre la relación entre las variables del dataset, pintando los datos según las siguientes variables:

'sex'
'smoker'
'day'
'time'
'size'
#5.2.7 Teniendo en cuenta todos los calculos realizados sobre este dataset y las gráficas dibujadas anteriormente, ¿cuáles serían los factores diferenciadores que más afectan a la cantidad de las proponia recibidas por el camarero?
#5.2.8 Calcula el tercer cuartil para la variable 'tip' y filtra todo el dataset según este valor para que el DataFrame resultante solamente contenga valores iguales o mayores que esa cantidad de propinas.
#5.2.9 Dibuja los histogramas que se pueden obtener para las siguientes variables del dataset obtenido en el paso anterior:

'smoker'
'day'
'time'
'size'
#5.2.10 Considerando todo el análisis realizado anteriormente, haz una recomendación al camarero para que lo tenga en cuenta a la hora de repartir los clientes entre el personal del restaurante, y muestra que de esa manera él puede conseguir mayor cantidad de proponas!!