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
print(f"{soma}")


