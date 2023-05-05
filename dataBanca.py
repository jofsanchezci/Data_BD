import pandas as pd
from statistics import mean
import matplotlib.pyplot as plt


df=pd.read_csv('Model_creditoPersonal.csv',index_col=0)
#print(df.head())
#Promedio de edad de los usuarios
edad=list(df['Age'])
print('Descripción de los usuarios')
print('-----------------------------------------------------------')
print('El promedio de edad de los usuarios es: ', round(mean(edad),1))
print('-----------------------------------------------------------')
#Promedio de experiencia
exp=list(df['Experience'])
print('El promedio de la experiencia de los usuarios es: ', mean(exp))
print('-----------------------------------------------------------')
#Promedio de familiares
fam=list(df['Family'])
print('El promedo de familiares de los usuario es: ', mean(fam))
print('-----------------------------------------------------------')
#Promedio del nivel de educación
edu=list(df['Education'])
print('El promedio del nivel de educación de los usuarios es: ', mean(edu))
print('-----------------------------------------------------------')
print('-----------------------------------------------------------')
print('-----------------------------------------------------------')
print('Porcentaje de hipeteca')

#Cual es el porcentaje de usuarios que tiene hipeteca
hipoteca=list(df['Mortgage'])
cont=0
for i in hipoteca:
	if i!=0:
		cont+=1
ph=cont/len(hipoteca) #Promedio de hipoteca
print('El Porcentaje de usuarios con hipeteca es: ', ph)
#Lista de valores de hipoteca
lvh=[]
for i in range(len(hipoteca)):
	if hipoteca[i]!=0:
		lvh.append(hipoteca[i])

print('El valor más grande de hipeteca: ', max(lvh))
print('El valor más pequeño de hipeteca: ', min(lvh))
print('El valor promedio de la hipeteca es:', mean(lvh))


print('-----------------------------------------------------------')
print('-----------------------------------------------------------')
print('Comparar la hipeteca vs CCAvg')
CuentaA=list(df['CCAvg'])

lvh=[]
lAc=[]

for i in range(len(hipoteca)):
	if hipoteca[i]!=0:
		lvh.append(hipoteca[i])
		lAc.append(CuentaA[i])





plt.scatter(lAc, lvh)
plt.show()


plt.boxplot(lAc,vert=False,patch_artist=True)
plt.show()


plt.boxplot(lvh,vert=False,patch_artist=True)
plt.show()













