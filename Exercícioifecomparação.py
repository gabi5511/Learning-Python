#

primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

if primeiro_valor >=segundo_valor:
    aparece = f'{primeiro_valor=} é maior do que {segundo_valor=}'
    print(aparece)
elif segundo_valor>=primeiro_valor:
    aparece = f'{segundo_valor=}é maior do que {primeiro_valor=}'
    print(aparece)

# Correção do Execício
# primeiro_valor = input('Digite um valor: ')
# segundo_valor = input('Digite outro valor: ')

# if primeiro_valor >= segundo_valor:
#     print(
#         f'{primeiro_valor=} é maior ou igual '
#         f'ao que {segundo_valor=}'
#     )
# else:
#     print(
#         f'{segundo_valor=} é maior '
#         f'do que {primeiro_valor=}'
#     )