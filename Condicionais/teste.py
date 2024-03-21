# #Exercício 
# num = 9
# if num%2 == 0: #Usamos % por que ele irá dividir o número até achar 0 ou 1 
#     print(f"{num} é par pois {num}%{2} = {num%2}")
# else: 
#     print(f"{num} é impar pois {num}%{2} = {num%2}")


# Pedir 5 números e conferir se são pares ou ímpares
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))
num4 = int(input("Digite o quarto número: "))
num5 = int(input("Digite o quinto número: "))

par = 0 #Vai ser nosso contador 
impar = 5-par

if  num1%2 == 0: 
    par += 1
if num2%2 == 0: 
    par += 1
if num3%2 == 0: 
    par += 1
if num4%2 == 0: 
    par += 1
if num5%2 == 0: 
    par += 1
print(f"A quantidades de pares é de {par} | e de ímpares é de {impar}")
