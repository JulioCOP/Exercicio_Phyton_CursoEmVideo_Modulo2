#Exercício Python 52: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

#Os números primos são os números naturais que podem ser divididos por apenas dois fatores: o número um e ele mesmo.

n=int(input("Informe um número: "))
cont=0
for c in range (1,n+1):
    if n%c==0:
        print('\033[31m', end=' ')
        cont+=1
    else:
        print('\033[33m', end=' ')
    print("{}" .format(c), end=' ')
print("\nO número {} foi possível dividir {}x" .format(n,cont))
if cont==2:
    print("Por isso ele é um número PRIMO")
else:
    print("POR ISSO ELE NÃO É PRIMO")