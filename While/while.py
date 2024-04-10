#Aprendendo While - 20/03 
# qtd | uma variável para quantidade 

#Pedir 5 números e conferir se são pares ou ímpares
par = 0 
qtd = 0
while qtd < 5: # enquanto a quantidade for menor que 5 , faça o laço
    num = int(input("Digite um número: "))
    if num%2 == 0:
        par += 1
        qtd += 1
print(f"Você digitou {par} pares e {5-par} ímpares.")
    
'''____'''

#Faça um código que peça uma senha para o usuário e só saia do laço quando a senha for correta
user = int(input("Digite sua senha: "))
senha = '1234'

while user != senha:    # enquanto a senha for diferente do usuário, faça a repetição 
    print("Senha errada!")
    user = input("Digite sua senha: ")
print("Senha correta!") # quando a senha for correta, o programa imprime a mensagem de senha correta

#Resolução Professor: 
senha = '1234'
user = input("Digite sua senha: ")
while user != senha:
    print("Você é hacker?")
    user = input("Digite sua senha: ")
print("Senha correta!")

#Faça um código que peça a senha mas tenha apenas três tentativas para acessar, e se errar mostre a mensagem "Sai daqui hacker"
senha = '1234'
user = int(input("Digite sua senha: "))
qtd = 1

while user != senha and qtd < 3:    # enquanto a senha for diferente do usuário, faça a repetição 
    print(f"Senha errada! Apenas mais {3 - qtd} tentativas")
    user = input("Digite sua senha: ")
    qtd += 1
if user == senha: 
    print("Senha correta!") # quando a senha for correta, o programa imprime a mensagem de senha correta
else: 
    print("Sai daqui hacker")

#Faça um código que some de 1 até 100 e imprima o resultado
soma = 0
num = 1
while num <= 100:
    soma += num
    num += 1
print(soma)

#Pedir um input para o usuário de sim ou não e só sair do laço quando o usuário digitar sim
user = input("Digite sim ou não: ")

while user != 'sim' or user != 'não':
    print("Digite sim ou não cacete")
    
    user = input("Digite sim ou não: ")
print(f"Aeeee, finalmente você digitou {sim}!")

#Caso o usuário seja idoso ele poderá acessar, se não o programa irá ficar repetindo até responder 'sim'
idoso = input("Você é idoso? S/N: ")
while idoso != 'sim' and idoso != 'não': 
    print("Resposta inválida")
    idoso = input("Você é idoso? S/N")

if idoso == "sim": 
    print("hahahhaha velho")
else: 
    print("ainda bem")

# Agora utilizando o OR
idoso = input("Você é idoso? S/N: ")
while not (idoso != 'sim' and idoso != 'não'): 
    print("Resposta inválida")
    idoso = input("Você é idoso? S/N")

if idoso == "sim": 
    print("hahahhaha velho")
else: 
    print("ainda bem")

#Exercício 
while True:
    idade = input("Digite sua idade: ")
    if idade.isnumeric(): 
        if int(idade) > 0 and int(idade) < 100: 
            idade = int(idade)
            break 
print(f"Você possui {idade} anos!!")

# Explicando while True: 
''' Sendo um loop infinito em Python. Ele continuará executando o bloco de código dentro dele até que uma 
instrução break seja encontrada.

Explicação prática:
''' 
while True: 
    nota = input("Digite sua nota: ")               #Insirir uma nota de 0 à 10 
    if nota.isnumeric():                            #Confere se a nota é um número
        if int(nota) >= 0 and int(nota) <= 10:      #E se a nota está entre 0 e 10, o programa imprime a nota e sai do loop (utilizando o break)
            nota = int(nota)
            print(f"Essa é sua nota {nota}")
            break 
    print("Resposta inválida")                      
    #Se a entrada do usuário não for numérica ou não estiver entre 0 e 10, o programa imprime "Resposta inválida" 
    # e o loop while True: começa novamente,