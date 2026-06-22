'''
O "append" adiciona o valor zipado em um array/lista
A menos que use for para percorrer o ap
'''

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