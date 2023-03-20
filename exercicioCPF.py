"""

Calculo do primeiro dígito do CPF

CPF: 746.824.890-70

Colete a soma dos 9 primeiros dígitos do CPF

multiplicando cada um dos valores por uma

contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)

   10  9  8  7  6  5  4  3  2

*  7   4  6  8  2  4  8  9  0

   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 

70+36+48+56+12+20+32+27+0 = 301

Multiplicar o resultado anterior por 10

301 * 10 = 3010

Obter o resto da divisão da conta anterior por 11

3010 % 11 = 7

Se o resultado anterior for maior que 9:

    resultado é 0

contrário disso:

    resultado é o valor da conta

O primeiro dígito do CPF é 7

"""

# Valores de cpf para teste
# cpf = '746.824.890-70'
cpf = '516.644.220-21'



cpf_sem_traço = cpf.split('-')
nove_digitos, resto = cpf_sem_traço
sem_pontos_lista = nove_digitos.split('.')
sem_ponto_str = ''.join(sem_pontos_lista)
# print(sem_ponto_str)

indice_str=0
fator_multiplicação = 11
soma_numeros_multiplicados = 0
while indice_str <= 8:
    numero_cpf = int(sem_ponto_str[indice_str])
    # print(numero_cpf)
    fator_multiplicação -= 1
    # print(fator_multiplicação)
    multiplicacao_numeros = numero_cpf*fator_multiplicação
    soma_numeros_multiplicados += multiplicacao_numeros
    # print(soma_numeros_multiplicados)
    if indice_str == 8:
        multiplicacao_10 = soma_numeros_multiplicados*10
        resto_divisao = multiplicacao_10%11
        # print(resto_divisao)
        if resto_divisao>9:
            resultado = 0
            # print('Resultado é zero')
        else:
            resultado = resto_divisao
            # print(f'Resultado é {resto_divisao}')
        print(f'O seu primeiro dígito é {resultado}')
        break
    

    indice_str+=1
   



