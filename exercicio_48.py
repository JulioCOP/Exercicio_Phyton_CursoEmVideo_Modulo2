#Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram
#no intervalo de 1 até 500

n=0
soma=0
cont=0
for n in range(1,501,2):
    if n%3 ==0:
        cont= cont+1  #cont+=1
        soma=soma+n    #soma+=n
print("O resultado da soma dos {} multiplos é {}" .format(cont,soma))