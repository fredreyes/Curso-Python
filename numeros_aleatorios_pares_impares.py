import random

lista = []
pares= []
impares = []
r = 0 

for r in range(20):
  lista.append(random.randint(0,100))
  z =(lista[r])
  if z%2 ==0:
    pares.append(lista[r])
    pares.sort()
  else:
    impares.append(lista[r])
    impares.sort()

concatenarListas = pares + impares 
"""print ('pares', pares)
print ('impares', impares)"""
print(concatenarListas)