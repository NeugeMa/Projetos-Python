# Aprendendo For - 20/04

# O que é o For?
# é utilizado para percorrer/ ou repetir uma sequência de dados, executando um conjunto de instruções 

#Exemplo
lista = [1, 2, 3, 4, 5]

for item in lista: 
    print(item)

# 0.1 - Na primeira repetição, item vai receber o valor do primeiro elemento da lista lista, que é 1. 
# Portanto print(item) vai mostrar o valor 1.

# 0.2 - Na segunda repetição, item vai receber o valor do segundo elemento da lista lista, que é 2. Portanto print(item) 
# vai mostrar o valor 2.
    
# Utilizando For com Else:
# Adicionar o else ao final do for nos possibilita executar um bloco de código após a repetição ter sido completamente percorrido.

'''
for item in sequencia:
    print(item)
else:
    print('Todos os items foram exibidos com sucesso') '''

# Função range:
# Sua ideia é retornar a lista de números inteiros. A forma de usar é range(n):
# aonde n é um número. E ele vai fornecer uma lista com elementos (e sempre iniciará com 0)

#Exer: Crie um script em Python que imprima os números de 1 até 5 na tela, usando a função range.

for num in range(5): #Irá imprimir apenas [1, 2, 3, 4]
    print(num+1)     #Irá somar para mostrar o número 5 

#Outra forma:
for num in range (1,6): 
    print(num)



# Exemplos com for + range
for i in range(10):
    print(i)

for i in range(10):
    i = 1
    print(i)