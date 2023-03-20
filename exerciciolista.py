'''
Faça uma lista de compas com listas
O usuário deve ter a possibilidade de 
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com
erros de índices inexistentes na lista
'''

# MINHA RESOLUÇÃO

# import os
lista_compras = []
while True:
    print('Selecione uma opção' )
    acao = input('[i]nserir [a]pagar [l]istar: ').lower()
    if acao == 'i':
        produto = input('Valor: ')
        lista_compras.append(str(produto))
        # print(lista_compras)
    elif acao == 'a':   
        excluir_str = input('Digite o índice a ser excluído: ')
        try:
            excluir_int = int(excluir_str)
            tamanho_lista = len(lista_compras)
            if excluir_int <= tamanho_lista:
                del lista_compras[excluir_int]
            else:
                print('Este índice não é válido.')
                continue
        except ValueError:
            print('Digite um número inteiro.')
            continue
    elif acao == 'l':
        for indice, nome in enumerate(lista_compras):
            print(indice, nome)
    else: 
        print('Digite "a", "i" ou "l"')
        continue
    # os.system('clear')
    