#Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher
#qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
import decimal
import math
n=int(input("Digite um número inteiro: "))
print('''Usuário escolha sua base de conversão:
 [ 1 ]      Converter para binário
 [ 2 ]      Converter para octal 
 [ 3 ]      Converter para hexadecimal''')
opcao= int(input("Sua opção: "))

if opcao==1:
    print("O número{} convertido em binário é: {} ".format(n,bin(n)))
elif opcao==2:
        print("O número {} convertido para decimal: {} ".format(n, oct(n)))
else:
    print("O número {} convertido para hexadecimal: {} ".format(n, hex(n)))
