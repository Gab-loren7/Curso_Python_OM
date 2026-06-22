nome = 'Gabriel Lorenssetti'
altura = 1.75
peso = 80
idade = 18
imc = peso / (altura * altura)
print(imc)

#FString

# Para concatenar variaveis, coloque "f" antes das aspas.
linha_1 = f'{nome} tem {altura:.2f} de altura.' # (:.2f) = duas casas depois da vírgula.
linha_2 = f'\nPesa {peso} quilos e seu imc é {imc:.0f}.'
print(linha_1, linha_2)
## Gabriel Lorenssetti tem 1.75 de altura. Pesa 80 quilos e seu imc é 26. ##

#Format
formato = '{} tem {} anos e {} de altura'.format(nome, idade, altura) # os valores dos parametros de format, completam as chaves {}
print(formato)

## Gabriel Lorenssetti tem 18 anos e 1.75 de altura ##