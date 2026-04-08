# append(x) Adiciona um novo item com valor x ao final do vetor.

i=1
lista=[]

while i < 11:
    lista.append(i)
    i += 1
print(lista)

lista2 = ["a", "b", "c"]

for valor in lista2:
    lista.append(valor)
    
print(lista)