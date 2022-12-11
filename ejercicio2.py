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
import pylab as plt
import seaborn as sns 
#5.2.1 Saca todas las estadísticas principales de las variables del dataset.

df = pd.read_csv('tips.csv')
print(df.head())
print('\nInfromación del df\n')
print(df.info())
print('\nColumnas del df\n')
print(df.columns)
print('\nDescripción básica del df\n')
print(df.describe())

#5.2.2 Comprueba si hay valores perdidods en el dataset y si fuera así en qué registros existen estos valores.
print('\nValores nulos\n')
print(df.isnull().sum())
#Como podemos ver, en principio no hay ningún valor nulo


#5.2.3 Clacula qué porcentaje de los clientes que dan propina son hombres y qué porcentaje son mujeres?
a = df.groupby('sex')['tip'].sum()
b = round(a.Female/a.sum() * 100, 2) #Porcieto de propina mujeres
b1 = round(a.Male/a.sum() * 100, 2) #Porcieto de propina mujeres
c = [b, b1]
fig, ax = plt.subplots(figsize=(7,4))
ax.bar(a.index ,c)
plt.xlabel('Female:' + str(b)+'%   Male:' +str(b1)+'%')
plt.show()

#5.2.4 Agrupa los datos según estas variables, calculando el tamaño, la mediana y la media para cada grupo:
'sex''smoker''day''time''size'

def agrupar(df, parametro):
    tamanio = df.groupby(parametro).size()
    media = df.groupby(parametro).mean()
    mediana = df.groupby(parametro).median()
    return tamanio, media, mediana
#sex
print('\n')
sex, media_sex, mediana_sex = agrupar(df, 'sex')
print('\nTamaño de sex\n')
print(sex)
print('\nMedia de sex\n')
print(media_sex)
print('\nMediana de sex\n')
print(mediana_sex)


#smoker
print('\n')
smoker, media_smoker, mediana_smoker = agrupar(df, 'smoker')
print('\nTamaño de smoker\n')
print(smoker)
print('\nMedia de smoker\n')
print(media_smoker)
print('\nMediana de smoker\n')
print(mediana_smoker)

#day
print('\n')
day, media_day, mediana_day = agrupar(df, 'day')
print('\nTamaño de day\n')
print(day)
print('\nMedia de day\n')
print(media_day)
print('\nMediana de day\n')
print(mediana_day)

#time
print('\n')
time, media_time, mediana_time = agrupar(df, 'time')
print('\nTamaño de time\n')
print(time)
print('\nMedia de time\n')
print(media_time)
print('\nMediana de time\n')
print(mediana_time)

#size
print('\n')
size, media_size, mediana_size = agrupar(df, 'size')
print('\nTamaño de size\n')
print(size)
print('\nMedia de size\n')
print(media_size)
print('\nMediana de size\n')
print(mediana_size)

#5.2.5 Dibuja una gráfica que muestre para cada grupo de personas servidas en el restaurante, 
# el promedio de las propinas pagadas.

fig, ax1 = plt.subplots(figsize=(7,4))
ax1.bar(mediana_size.index ,mediana_size['total_bill'])
plt.xlabel('Promedio propinas de cada grupo')
plt.show()

#5.2.6 Dibuja una gráfica que muestre la relación entre las variables del dataset, 
# pintando los datos según las siguientes variables:
'sex''smoker''day''time''size'
def representar(df, parametro):
    sns.scatterplot(x= 'tip', y = 'total_bill', hue= parametro, data = df)
    plt.show()
    
#Todas ellas respecto a total_bill y tip
representar(df, 'sex')
representar(df, 'smoker')
representar(df, 'day')
representar(df, 'time')
representar(df, 'size')

#Entre ellas
def representar1(df, parametro, parametro1):
    sns.countplot(x= parametro, hue = parametro1, data = df)
    plt.show()
    
representar1(df, 'day', 'sex')
representar1(df, 'day', 'smoker')
representar1(df, 'time', 'sex')
representar1(df, 'size', 'sex')

#5.2.7 Teniendo en cuenta todos los calculos realizados sobre este dataset y las gráficas dibujadas anteriormente, 
# ¿cuáles serían los factores diferenciadores que más afectan a la cantidad de las proponia recibidas por el 
# camarero?

#El camarero recibe más propina los hombes, los no fumadores , por la noche, los domingos, los sábados y los grupos de dos 
#El camarero recibe menos propina por el día, cuando va una persona, los viernes, los fumadores y las mujeres


#5.2.8 Calcula el tercer cuartil para la variable 'tip' y filtra todo el dataset según este valor para que el 
# DataFrame resultante solamente contenga valores iguales o mayores que esa cantidad de propinas.

q3 = round(df.tip.quantile(.75), 2)
print(q3)
df1 = df[df['tip']>= q3]
df1.reset_index(inplace = True, drop = True)
print(df1.head())


#5.2.9 Dibuja los histogramas que se pueden obtener para las siguientes variables del dataset obtenido en el paso 
# anterior:
'smoker''day''time''size'
def histo(df, parametro):
    fig, ax = plt.subplots(figsize=(7,4))
    ax.bar(df1[parametro], df1['tip'])
    plt.xlabel(f'Histograma tip con {parametro}')
    plt.show()
histo(df, 'smoker')
histo(df, 'day')
histo(df, 'time')
histo(df, 'size')

#5.2.10 Considerando todo el análisis realizado anteriormente, haz una recomendación al camarero para que lo 
# tenga en cuenta a la hora de repartir los clientes entre el personal del restaurante, y muestra que de esa manera 
# él puede conseguir mayor cantidad de proponas!!