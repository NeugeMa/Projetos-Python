while True:
    idade = input("Digite sua idade: ")
    if idade.isnumeric(): 
        if int(idade) > 0 and int(idade) < 100: 
            idade = int(idade)
            break 
print(f"Você possui {idade} anos!!")