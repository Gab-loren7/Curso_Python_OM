# extend (iterable): Acrescenta os itens de iterable ao final do vetor. Se iterable for outro vetor, ele deve ter exatamente o mesmo código de tipo; senão, ocorrerá uma TypeError. Se iterable não for um vetor, ele deve ser iterável e seus elementos devem ser do tipo correto para ser acrescentado ao vetor.

listaNums = []
i = 1

while i < 11:
    listaNums.append(i)
    i += 1
print(listaNums)
    
listaLetras = ['a', 'b', 'c', 'd']

listaNums.extend(listaLetras)
print(listaNums)