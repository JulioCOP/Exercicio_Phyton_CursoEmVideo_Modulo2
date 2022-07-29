#Programa deve informar ler o ano de nascimento do usuário e informar de acordo com sua idade
# se o mesmo tem idade exata para se alistar ou se o mesmo ja passou do prazo de alistamento.
# e se não passou quanto ainda falta para se alistar. Para as situações do programa, mostar o tempo que
# falta ou que quanto que já passou

from datetime import date

nome=str(input("Qual o nome do usuário ? "))
ano_nasc= int(input("{}, qual o ano de seu nascimennto: " .format(nome)))
ano= date.today().year
idade= ano-ano_nasc
if idade > 18:
    a = idade - 18
    print("{} ja passou {} anos. VOCÊ TEM DE FAZER SEU ALISTAMENTO MILITAR ".format(nome, a))
elif idade < 18:
    a2 = 18 - idade
    print("{} não pode se alistar, ainda faltam {} anos".format(nome,a2))
else:
    print("USUÁRIO PODE SE ALISTAR")


