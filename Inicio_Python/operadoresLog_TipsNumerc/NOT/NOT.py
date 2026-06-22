# Operador Lógico 'not'
# Usado para inverter expressões
# not True = False
# not False = True

senha  = input('Senha: ')

if not senha: # Variavel vazia é 'False'
    print('Você não digitou nada!')
    print(senha)

print(not True) # False
print (not False) # True
