# Versão do Professor :)

print("Seja bem-vindo a Vinharia Agnelo!")
ano = int(input("Digite seu ano de nascimento: "))
nome = input("Digite seu nome: ")
idade = 2024 - ano

#Resolvendo questões de idade
if idade < 18: 
    print("Sai daqui, você não tem 18 anos")

else: 
    end = input("Diga seu endereço: ")
    # Variáveis que iramos usar para todos os vinhos
    v1 = 'Vinho Maluf'
    v2 = 'Vinha Negrobauer'
    v3 = 'Vinho Corotinho'
    preco1 = 100
    preco2 = 50
    preco3 = 10
    fretado = 10            

    opcao =  input("Olá " + nome + " nós possuimos os seguintes vinhos: \n Vinho Maluf (v1) | 100R$ \n Vinho Negrobauer (v2) | 50R$ \n Vinho Corotinho (v3) | 10R$ \n Qual você quer?")
    if opcao == v1: 
        preco == preco1
    elif opcao == v2: 
        preco == preco2
    else: 
        preco = preco3
    qtd = int(input(f"Diga à quantidade de garrafas {opcao}: "))
    valor = qtd*preco
    if valor > 100: 
        print("Parabéns, você ganhou frete grátis")
    else: 
        valor += fretado 
    print(f"{nome} muito obrigada por comprar em nossa vinharia! Sua compra foi: \n Você levou {qtd} de garrafas de {opcao} ")