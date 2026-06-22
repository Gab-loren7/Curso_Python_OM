'''
O "append" adiciona o valor zipado em um array/lista
O "extend" adiciona o valor deszipado em um array/lista
'''

vendedores = ['João','Alon','Amanda','Camila']
novas_contratacoes = ['Gabriel','Sofia']

vendedores.append(novas_contratacoes) ## Valores add Zipados
print(vendedores)

vendedores.extend(novas_contratacoes) ## Valores add Deszipados
print(vendedores)

listaNums = []
i = 1

while i < 11:
    listaNums.append(i)
    i += 1
print(listaNums)
    
listaLetras = ['a', 'b', 'c', 'd']

listaNums.extend(listaLetras)
print(listaNums)