## Tipos Numéricos
num_inteiro = 2 #int
num_fracionario = 2.0 #float
num_complexo = 2j #complex
print(num_complexo.real) #Parte real
print(num_complexo.imag) #Parte imaginária

## Operadores Algébricos
soma = num_inteiro + 3 # Operador +
subtracao = num_inteiro - 3 # Operador +
multiplicacao = num_fracionario * 2 # Operador *
divisao = num_complexo / 2 # Operador /
modulo = multiplicacao % 2 # Operador %
potencia = num_inteiro ** 2 # Operador **

## Operadores de Comparação
igualdade = num_inteiro == 2 # Operador ==
diferença = num_fracionario != 3 #Operador !=
maior_que = num_inteiro > 2 # > Não implementado para complex
maior_igual = num_inteiro >= 2 # > Não implementado para complex
menor_que = num_inteiro < 2 # < Não implementado para complex
menor_que = num_inteiro <= 2 # < Não implementado para complex

multiplicando = 2 #int
multiplicador = 2.3 #float
div_complexo = 2.3j
#Qual o tipo da variável resultado a cada passo?
resultado = multiplicando * multiplicador # Tipo de resultado?
resultado = resultado / div_complexo # E agora?
# R: O tipo é ampliado para float.
resultado = 1 / 2 # E nesse caso, o que acontece?
resultado = 1 / 2.0 # E agora? Tem diferença?
# R: em ambos os casos, o resultado é um float
parcela = 10000 / 3 #Cuidado com a limitação dos tipos!
print(parcela)
# Parcela = 3333.3333333333335
# Operações com float tem precisão limitada
print(1.1 + 2.2 == 3.3)