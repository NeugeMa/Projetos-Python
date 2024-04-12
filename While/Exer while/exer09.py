'''
Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares 
e a quantidade de números impares.
'''

qtd = 1
pares = 0
impar = 0

while qtd < 10: 
    numero = int(input(f"Diga o {qtd} número: "))
    if numero%2 == 0: 
        pares += 1
        qtd += 1
    impar += 1
    qtd += 1

print(f"Quantidade par {pares} | Quantidade impares {impar}")


