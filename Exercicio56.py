#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
soma=0
maiorhomem=0
nomevelho=''
totmulher=0
for c in range (1,5):
    nome=str(input("Digite seu nome: "))
    idade=int(input("Informe sua idade: "))
    sexo= str(input("Qual o seu sexo ? [ M / F ]: ")).strip().upper()
    soma= soma+idade
    if c==1 and sexo in 'Mm':
        maiorhomem=idade
        nomevelho=nome
    if sexo in 'Mm' and idade>maiorhomem:
        maiorhomem=idade
        nomevelho=nome
    if sexo in 'Ff' and idade <20:
        totmulher+=1


media=soma/4
print("A media das idades é {} anos" .format(media))
print("O nome mais velho tem {} anos e se chama {}" .format(maiorhomem,nomevelho))
print("Um total de {}  tem menos de 20 anos".format(totmulher))