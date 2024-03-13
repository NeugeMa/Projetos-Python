'''Escreva um programa para ler um número de lados de um polígono regular e a medida do lado (em cm).
Calcular e imprimir o seguinte: 
- Se o número de lados for igual a 3 escreva TRIÂNGULO e o valor da área'
- Se o número de lados for igual a 4 escreva QUADRADO e o valor da área'
- Se o número de lados for igual a 5 escreva PENTÁGONO. 
'''
#Exer07 
nm_lado = int(input("Digite o número de lados do polígono: "))
medida_lado = float(input("Digite a medida do lado (em cm, por favor): "))

if nm_lado == 3:
    area = (medida_lado ** 2) * (3 ** 0.5) / 4
    print("TRIÂNGULO")
    print("Área:", area)
elif nm_lado == 4:
    area = medida_lado ** 2
    print("QUADRADO")
    print("Área:", area)
elif nm_lado == 5:
    print("PENTÁGONO")
else:
    print("Digito errado, refaça por favor!")