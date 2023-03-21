# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

# vamos definir a função

def mult(*args): # args para usar argumentos não nomeados ilimitados
    produto = 1 # importante: um número multiplicado por zero é zero
    for numero in args:
        produto *= numero
    print(produto)

print(1*2*3*4*5*6*7)
mult(1, 2, 3, 4, 5, 6, 7)

# Crie uma função fala se um número é par ou ímpar
# Retorne se o número é par ou ímpar

# definir a função

def paridade(x):
    if x % 2 == 0:
        print(f'{x=} é um número par.')
    else:
        print(f'{x=} é um número ímpar.')

# Não iremos entrar no mérito de 0 ser ou não um número par aqui.
paridade(3)