# Alternativa-1
Mi dirección de GitHub para este repositorio es:[GitHub](https://github.com/andmansim/Alternativa-1.git)
https://github.com/andmansim/Alternativa-1.git

He realizado dos estudios estadísticos, uno de coches y otro de un restaurante. 
El código es el siguiente:

# Coches
```
#5.1.1 Dibuja una gráfica que muestre la relación entre las variables del dataset.
import pandas as pd
import pylab as plt
import seaborn as sns
import numpy as np
import warnings

warnings.filterwarnings('ignore')

df = pd.read_csv('auto-mpg.csv')
print('Infomación del csv-------------------------------------------\n')
print(df.head)
print(df.info())
df_copia = df.copy()
#transformamos los datos de la columna horsepower de str a int
for i in range(len(df)):
    if df.horsepower[i] == '?':
        df.horsepower[i] = 0

print('\nCambio de tipo de la columna horsepower-----------------------------------\n')

df.horsepower = pd.to_numeric(df.horsepower)
print(df.info())
df = df.drop('car name', axis= 1)

#Representación

sns.pairplot(df, height=1.2)
plt.show()

#5.1.2 ¿Entre qué conjunto de variables se puede considerar que hay una relación?
#Variables con relación directa, es decir, linealmente dependientes de manera ascendente: displacement - weight, weight - horsepower, displacement - horsepower
#Variables con relación inversa, es decir, linealmente dependientes de manera descendente: weight - mpg, mpg - horsepower, mpg - displacement, horsepower - acceleration

#5.1.3 Calcula el coeficiente de correlación entre las variables del dataset y dibújalos en una gráfica. 
# Modifica la respuesta del paso anterior si lo consideras necesario según los coeficientes calculados.

print('\nMatriz de correlación----------------------------------------------------\n')
#mapa de correlación, este muestra la relación entre las variables

print(df.corr())
sns.heatmap(df.corr())
plt.show()
#Para que sean linealmente dependientes unas variables de otras, su correlación debe ser de 1 o -1., directa e inverda respectivamente. 
#En la relación directa hay que añadir cylinders - weight, cylinders - displacement y quitar la de horsepower - weight
#En la relación inversa hay que añador cylinder - mpg


#5.1.4 Dibuja un diagrama de dispersión entre el peso y la potencia, 
# pintando los puntos del gráfico según el número de cilindros.

print('\nDiagrama de dispersón peso, potencia--------------------------------------------\n')
plt.scatter(x =df.cylinders, y = df.weight/10, color = 'red', marker = '*', label = 'weight/10')#Se divide entre 10 para que estén más juntas las escalas
plt.scatter(x =df.cylinders, y = df.horsepower, color = 'green', marker = '^', label = 'horsepower')
plt.title('Diagrama dispersión peso-potencia respecto cylinder')
plt.xlabel('Cylinder')
plt.ylabel('Weight, Horsepower')
plt.show()

#5.1.5 Dibuja un diagrama de dispersión entre el peso y la potencia, pintando los puntos del gráfico 
# según el año de fabricación. 

# Comparando este nuevo gráfico con el anterior, ¿podemos decir qué criterio tiene más capacidad para agrupar 
# los coches o mejor dicho es un factor discriminatorio mayor que el otro?

plt.scatter(x =df['model year'], y = df.weight/10, color = 'red', marker = '*', label = 'weight/10')#Se divide entre 10 para que estén más juntas las escalas
plt.scatter(x =df['model year'], y = df.horsepower, color = 'green', marker = '^', label = 'horsepower')
plt.title('Diagrama dispersión peso-potencia respecto model year')
plt.xlabel('Model year')
plt.ylabel('Weight, Horsepower')
plt.show()
#Comparando ambos gráficos podemos ver que el primero se agrupa principalmente en 3 cilindradas(4,6,8), 
# en cambio en el segundo está más repartido por los años

#5.1.6 Saca el mismo gráfico que dibujaste en el ejercicio 5.1.5, esta vez solamente para los coches fabricados 
# en el año 70.

def filtrar(df, año):
    h = []
    w = []
    y = []
    for i in range(len(df)):
        if df['model year'][i] == año:
            h.append(df['horsepower'][i])
            w.append(df['weight'][i])
            y.append(df['model year'][i])
    return y, h, w
        
year, horse, weight = filtrar(df, 70)
weight2 = list(map(lambda x: x / 10, weight))
plt.scatter(x = year, y = weight2, color = 'red', marker = '*', label = 'weight')#Se divide entre 10 para que estén más juntas las escalas
plt.scatter(x =year, y = horse, color = 'green', marker = '^', label = 'horsepower')
plt.title('Diagrama dispersión peso-potencia respecto años 70')
plt.xlabel('Model year 70')
plt.ylabel('Weight, Horsepower')
plt.show()


#5.1.7 Saca el mismo gráfico que dibujaste en el ejercicio 5.1.5, esta vez solamente para los coches 
# fabricados en el año 80. 
# ¿Cuáles son las diferencias más destacables entre las relaciones dibujadas del año 70 y del año 80?

year, horse, weight = filtrar(df, 80)
weight3 = list(map(lambda x: x / 10, weight))
plt.scatter(x = year, y = weight3, color = 'red', marker = '*', label = 'weight')#Se divide entre 10 para que estén más juntas las escalas
plt.scatter(x =year, y = horse, color = 'green', marker = '^', label = 'horsepower')
plt.title('Diagrama dispersión peso-potencia respecto años 80')
plt.xlabel('Model year 80')
plt.ylabel('Weight, Horsepower')
plt.show()
#Diferencias entre los dos años:
#1. En los años 70 los coches tenían un mayor peso y potencia que en los 80
#2. En los 80, al rededor de 150 no se fabrcó ningún coche con ese peso o potencia
#3. Pasa lo mismo en los 70 pero al rededor de 400
#4. Se fabricaron más coches en los 70
```

# Restaurante
```
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


#5.2.3 Calcula qué porcentaje de los clientes que dan propina son hombres y qué porcentaje son mujeres?
df = df[df['tip']>= 0.0]
a = df.groupby('sex')['tip'].count()
b = round(a.loc['Female']/a.sum() * 100, 2) #Porcieto de propina mujeres
b1 = round(a.loc['Male']/a.sum() * 100, 2) #Porcieto de propina mujeres
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
ax1.bar(media_size.index ,media_size['total_bill'])
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
# él puede conseguir mayor cantidad de propinas!!

#Las recomendaciones al camareron son: Que mande a los grupos de hombres de dos pesonas a la zona de no fumadores. 
#Que recomiende platos más caros porque los que más gastan son los que más propina dan. 
```
