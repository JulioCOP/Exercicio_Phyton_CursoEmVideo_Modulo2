#Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
#Se o valor digitado for ímpar, desconsidere-o.
soma=0
cont=0
for n in range(1,7):
    x=int(input("Digite um número inteiro: "))
    if x%2==0:
        soma=soma + x
        cont+=1
print("O usuário informou {} nº pares e sua soma foi {}".format(cont,soma))