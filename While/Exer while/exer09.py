'''
Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares 
e a quantidade de números impares.
'''

qtd = 0 
while qtd < 10: 
    numero = input(f"Diga o {qtd+1} número: ")
    while not numero.isnumeric():
        print("Erro! Digite um número")
        numero = input(f"Diga o {qtd+1} número:")
    numero = int(numero)