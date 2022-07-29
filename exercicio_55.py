#Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
maior=0
menor=0
for u in range (1,6):
    p=float(input("Informe o peso da {}º pessoa em Kg: ".format(u)))
    if u==1:
        maior= p
        menor=p
    else:
        if p>maior:
            maior=p
        if p<menor:
            menor=p
print("{} É O MAIOR PESO".format(maior))
print("{} É O MENOR PESO".format(menor))