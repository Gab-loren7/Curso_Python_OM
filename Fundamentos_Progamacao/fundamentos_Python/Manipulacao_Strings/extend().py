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