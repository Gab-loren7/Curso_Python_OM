x = 10
y = 15
# Operadores lógicos formam expressões lógicas
conjuncao = x < 20 and y >= 20
disjuncao = x < 20 or y >= 20
negacao = not x < 20

expressao = x < 20 and y > 10 and not True != False or x == y
#Podemos usar parênteses para explicitar a ordem das operações
expressao = (x < 20 and y > 10) and not (True != False or x == y)

'''
1. Unários (-x, +y)
2. Multiplicativo (*, /, %)
3. Aditivo (+, -)
4. Comparativo (==, !=, >, <)
5. Negação (not)
6. Conjunção (and)
7. Disjunção (or)
8. Atribuição (=, +=, -=)
'''