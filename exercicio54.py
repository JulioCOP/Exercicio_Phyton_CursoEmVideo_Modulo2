# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda
# não atingiram a maioridade e quantas já são maiores.

from datetime import date
ano= date.today().year
cont_menor=0
cont_maior=0
for nome in range (1,8):
    n=int(input("Informe o ano de nascimento do usuário: "))
    maioridade = ano - n
    if maioridade>=18:
        cont_maior+=1
    else:
        cont_menor+=1
print("{} pessoas ainda não atingiram a maioridade." .format(cont_menor))
print("{} pessoas já atingiram a maioridade." .format(cont_maior))
print("FIM DO PROGRAMA")
