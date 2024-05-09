# Funções: 

# Google Drive | https://docs.google.com/document/d/1MkTDNSKe85-RVgow_Kwpk00ybxyR4eRnEXvZvZGsGOU/edit

# Exercício - Pode votar ou não?
def podeVotar(nome, idade):
    if idade >= 16:
        print(f"Sim, a pessoa {nome} pode votar")
        return True
    else:
        print(f"Não, a pessoa {nome} ainda não pode votar")
        return False
        


a = podeVotar("Lucas",38)
print(f"a primeira resposta foi {a}")
b = podeVotar("Maira",13)
print(f"a segunda resposta foi {b}")
c = podeVotar("Pedro",18)

#Adicionando Input
nome2 = input("Digite um nome")
idade2 = int(input("Digite uma idade"))
podeVotar(nome2,idade2)

'''
- Quando eu rodo a linha a = podeVotar("Lucas",38) , eu faço duas atribuições.
nome="Lucas”, idade=38

        - Quando a função termina, ela executou o comando return True
        - Isso faz o seguinte: a = podeVotar(“Lucas”,38)  True

- Quando eu rodo a linha b = podeVotar("Maira",13) , eu faço duas atribuições.
nome=”Maira”, idade=13

        - Quando a função termina, ela executou o comando return False
        - Isso faz o seguinte: b = podeVotar(“Maira”,13)  False

'''

# Exercício - Calcular Idade
# Escreva uma função que recebe o ano de nascimento da pessoa e retorna a idade da pessoa
ano_atual = 2024

def calcularIdade(nome,ano_nascimento):
	print(f"A pessoa {nome} tem a idade {2024-ano_nascimento}")
	return  ano_atual-ano_nascimento
	
a = calcularIdade("Lucas",2004)
b = calcularIdade("Mari",1994)
c = calcularIdade("Helo",2014) 

# Exercício - Pode votar ou não? | Outra forma
def podeVotar(nome, ano_nascimento):
    idade = calculaIdade(nome, ano_nascimento)
    if idade >= 16:
        print(f"Sim, a pessoa {nome} pode votar")
        return True
    else:
        print(f"Não, a pessoa {nome} ainda não pode votar")
        return False
        
def calculaIdade(nome,ano_nascimento):
    print(f"A pessoa {nome} tem a idade {2024-ano_nascimento}")
    return 2024-ano_nascimento
    
        
a = podeVotar("Lucas",2004)
b = podeVotar("Rafael",1996)
c = podeVotar("Gabriela",2014)


# Exercício - Calcular Idade usando DateTime
from datetime import datetime

agora = datetime.now()
ano_atual = agora.year

def calculaIdade(nome,ano_nascimento):
    idade  = ano_atual-ano_nascimento
    print(f"A pessoa {nome} tem a idade {idade}")
    return idade
    
a = calculaIdade("Lucas",2004)
b = calculaIdade("Rafael",1996)
c = calculaIdade("Gabriela",2014)

# Exercício - Faça uma função que mostre o maior número
def maior(numeros):
    maior = 0 # A variável maior é acumulativa
    for elemento in numeros:
        if elemento >  maior:
            maior = elemento
    return maior
    

n = maior([10,20,2,30,7]) #maior retorna o 30, o n vai valer 30
n2 = maior([100,200,2,30,7]) #maior retorna o 200, o n vai valer 200
n3 = maior([-2,-3,-1]) #BUG! era pra ser -1, mas vai ser 0