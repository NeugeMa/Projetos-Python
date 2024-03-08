# Iniciando Python - 01/03
print("Olá mundo!") # Imprimindo nosso primeiro 'Olá mundo!'

# Variáveis 
frase = "Olá mundo!"        #string - Escrita
primeiro_numero = 1         #int - Números 
segundo_numero = 1.5        #float - Números quebrados
booleana = False            #boolean - Utilizamos para condicionais
''' Exemplo: Se você tiver 17 anos e for entrar num site de bebidas,você não irá pode acessar por ser FALSE (não ter 18 anos) 
 e caso você tivesse seria TRUE'''

print(type(frase))         # type - utilizado para descobrir o tipo de variável 
print(primeiro_numero)
print(type(primeiro_numero))
print(segundo_numero)
print(type(segundo_numero))
print(booleana)
print(type(booleana))

''' ---- '''

#Operações Aritiméticas |  + - * /
num1 = 2
num2 = 2
adição = num1 + num2
sutracao = num1 - num2
multiplicacao = num1 * num2
divisao = num1 / num2
print(f"A soma entre {primeiro_numero} e {segundo_numero} tem o resultado de {soma}")
print(f"A subtração entre {num1} e {num2} é de {sutracao}")
print(f"A multiplicação entre {num1} e {num2} é de {multiplicacao}")
print(f"A divisão entre {num1} e {num2} é de {divisao}")

''' Imprimindo contas com strings  '''
num1 = int(input("Digite um número:"))
num2 = int(input ("Agora digite outro número:"))

# soma de strings faz com que eles juntem os números em vez de realmente somar/sub/etc.. | EX: 4 + 4 ele entende que será 44 em vez de 8
soma = num1 + num2
print(soma)

nome = input("Qual o seu nome?:")
print(f"Seja Bem-Vindo {nome}")

num1 = int(input("Agora digite um número: "))
num2 = int(input("Agora digite outro número: "))
soma = num1 + num2
print(soma)

''' ---- '''

#Estruturas de repetição sem while/ for
frase = "Eu"
frase = frase + " me"
frase = frase + " chamo"
frase = frase + input(" Digite seu nome: ")
frase = frase + " :)"
print(frase)

''' ---- '''

#Booleanos | True & False | 
''' 
> maior      | < menor
== igual     | != diferente 
>= maior que | <= menor que 
and | or | in | is | not ''' 

a = 2==3
b = 2!=3
c = not 5 == 6
d = 'd' not in 'Mariana'
e = 2>3 or 5!=6               # or - retorna verdadeiro caso uma das coisas sejam verdadeiras/ mesma coisa funciona para falso 
f = 2 == 3 and 2<3            # and - só retorna verdadeiro/falso se ambos os casos sejam verdadeiro/falso
print(a)
print(b)
print(c)
print(d)
print(e)
print(f) 

#Aprendendo a comparar com verificador booleano 
num1 = 5 
num2 = 9
a = num1 > num2 
print(f"A comparacao  {num1}>{num2} dá {a}")

a = num1 == num2 
print(a)
a = num1 >= num2 
print(a)
a = num1 <= num2
print(a)
a = num1 != num2 
print(a)

#Utilizando o OR 
a = 2
b = 4
c = 6 
d = 8
print(f"A comparação {a} > {b} or {c} > {d}, ou seja, {a>b} or {c>d}")       #false 
print(f"A comparação {d} < {c} or {a} > {b}, ou seja, {d>c} or {a>b}")       #verdadeiro, falso 
print(f"A comparação {a} == {b} or {c} != {d}, ou seja, {a==b} or {c!=d}")   #falso, verdadeiro
print(f"A comparação {b} > {a} or {d} < {c}, ou seja, {b>a} or {d>c}")       #verdadeiro

#Utilizando o AND 
a = 2
b = 4
c = 6 
d = 8
print(f"A comparação {a} > {b} and {c} > {d}, ou seja, {a>b} and {c>d} resultando em: {a>b and c>d}")         #false      
print(f"A comparação {d} < {c} and {a} > {b}, ou seja, {d>c} and {a>b} resultando em: {d<c and a>b}")         #false
print(f"A comparação {a} == {b} and {c} != {d}, ou seja, {a==b} and {c!=d} resultando em: {a==b and c!=d}")   #false
print(f"A comparação {b} > {a} and {d} < {c}, ou seja, {b>a} and {d>c} resultando em: {b>a and c<d}")         #true

''' ---- '''

#Condicionais
idade = int(input("Para entrar no site, digite sua idade: "))
if idade < 18:
    print("Você é menor de idade e não pode acessar o site.")
else: 
    print("Bem vindo a Zé Delivery")

#Condição utilizando - OR 
idoso = input("Você é idoso? ")
gestante = input("Você está grávida?")
if idoso == 'sim' or gestante == 'sim': 
    print("Pode estacionar!!")

#Condição utilizando - AND | só irá ser terminada quando ambas condições sejam verdadeiras 
idoso = input("Você é idoso? ")
cartao = input("Você tem o cartão? ")
if idoso == 'sim': 
    if cartao == 'sim':
        print("Estacionar")

#Exercício: Faça um código que mostre as vogais utilizando tudo que aprendemos 
vogal = input("Digite uma letra: ")
if vogal == "a" or vogal == "e" or vogal == "i" or vogal == "o" or vogal == "u": #utilizando o or 
    print("Isso aí, você acertou a letra 😎")
else: 
    print("Seu burro!! Você errou")

#Declarando se um aluno está reprovado/aprovado/exame
nota = int(input("Digite sua nota: "))
if nota >= 6:
    print(f"Parabéns você está aprovado, atingindo a média final {nota}")
elif nota < 6 and nota>=4:
    print ("Exame")
else:
    print("Reprovado!")

#Declarando o imposto de renda 
salario = float(input("Digite seu sálario atual: "))
if salario<1903.98: 
    agiota = 0 #Porcentagem agiot    
elif salario <= 2826.65: 
    agiota = 0.075 #Porcentagem agiota
elif salario <= 3751.05:
    agiota = 0.15 #Porcentagem agiota
elif salario <= 4664.68:
    agiota = 0.225 #Porcentagem agiota
  
else: 
    agiota = 0.275 #Porcentagem agiota
    desconto = salario*agiota
    salario = salario - desconto
    print(f" O seu salário com desconto é de {desconto} será {salario}!!")

# 