"""
Exercício
Exiba os índices da lista
0 Maria
1 Helena
2 Luiz
"""
# Minha resolução
# indice = 0
lista =['Maria', 'Helena', 'Luiz']

# for nome in lista:
#     print(indice, nome)
#     indice +=1

# resolução
lista.append('João') # poderia adicionar nomes à lista
indices = range(len(lista)) # pego o tamanho da lista
# range vai começar do zero e vai até o último índice
for indice in indices:
    print(indice, lista[indice], type(lista[indice]))