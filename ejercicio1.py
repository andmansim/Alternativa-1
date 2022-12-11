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


#mapa de correlación, este muestra la relación entre las variables
def mapa_corr(df):
    plt.figure(figsize=(7, 7))
    plt.title('Mapa de correalción')
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
mapa_corr(df)

#5.1.2 ¿Entre qué conjunto de variables se puede considerar que hay una relación?
#Para que sean linealmente dependientes unas variables de otras, su correlación debe ser de 1 o -1. 
#Los datos que más se aproximan a ellos son: cylinders - weight , cylinders - splacement, weight - splacement, splacement - mpg, clinders - mpg, mpg - weight 

#5.1.3 Calcula el coeficiente de correlación entre las variables del dataset y dibújalos en una gráfica. 
# Modifica la respuesta del paso anterior si lo consideras necesario según los coeficientes calculados.
print('\nMatriz de correlación----------------------------------------------------\n')
print(df.corr())
mapa_corr(df)
#No hace falta modificar la relación que he dicho antes, dado que me he basado en la matriz de correlación, al ser la mejor gráfica para representar la relación entre todas las variables numéricas


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

#5.1.6 Saca el mismo gráfico que dibujaste en el ejercicio 5.1.5, esta vez solamente para los coches fabricados en el año 70.

for i in range(len(df)):
    if df['model year'][i] == 70:
        df['horse_model'][i] = df['horsepower'][i]
        df['weight_model'][i] = df['weight'][i]
        
print(df['horse_model'])
print(df['weight_model'])
'''plt.scatter(x ='70', y = df.weight/10, color = 'red', marker = '*', label = 'weight/10')#Se divide entre 10 para que estén más juntas las escalas
plt.scatter(x ='70', y = df.horsepower, color = 'green', marker = '^', label = 'horsepower')
plt.title('Diagrama dispersión peso-potencia respecto model year')
plt.xlabel('Model year')
plt.ylabel('Weight, Horsepower')
plt.show()
'''

#5.1.7 Saca el mismo gráfico que dibujaste en el ejercicio 5.1.5, esta vez solamente para los coches fabricados en el año 80. 
# ¿Cuáles son las diferencias más destacables entre las relaciones dibujadas del año 70 y del año 80?