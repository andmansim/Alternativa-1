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
def mapa_corr(df):
    plt.figure(figsize=(7, 7))
    plt.title('Mapa de correlación')
    sns.set(style='white')

    mask=np.triu(np.ones_like(df.corr(), dtype=bool))

    cmap=sns.diverging_palette(0, 10, as_cmap=True)


    sns.heatmap(df.corr(),
               mask=mask,
              cmap=cmap,
              center=0,
              square=True,
              annot=True,
              linewidths=0.5,
              cbar_kws={'shrink': 0.5})
    plt.show()
print(df.corr())
mapa_corr(df)
#Para que sean linealmente dependientes unas variables de otras, su correlación debe ser de 1 o -1., directa e inverda respectivamente. 
#Los datos que más se aproximan a ellos son: cylinders - weight , cylinders - displacement, weight - displacement, displacement - mpg, cylinders - mpg, mpg - weight 

#5.1.4 Dibuja un diagrama de dispersión entre el peso y la potencia, 
# pintando los puntos del gráfico según el número de cilindros.
print('\nDiagrama de dispersón peso, potencia--------------------------------------------\n')
#a = df.groupby('cylinders').sum()
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