#Faça a tabuada de todos os números de 1 à 10: 
while True:
    num = input("Digite um número entre 1 e 10 para ver a tabuada: ")
    
    if num.isnumeric() and 1 <= int(num) <= 10:
        num = int(num)
        break
    else:
        print("Erro! Digite entre 1 e 10.")

print(f"Tabuada do {num}:") 
for i in range(1, 11):                      
    print(f"{num} x {i} = {num * i}")