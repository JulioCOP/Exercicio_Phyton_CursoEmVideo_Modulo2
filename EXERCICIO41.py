#A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta
#e mostre  sua categoria, de acordo com a idade
# Até 9 anos: MIRIM

#Até 14 anos: INFANTIL

#Até 19 anos: JÚNIOR

# Até 25 anos: SÊNIOR

# Acima de 25 anos: MASTER

from datetime import date

nome_atleta= str(input("Informe o nome do atleta: "))
ano_nasc= int(input("Informe o ano de nascimento do atleta: "))
ano= date.today().year
idade= ano - ano_nasc

if idade<=9:
    print("A categoria do atleta {} é MIRIM".format(nome_atleta))
elif idade<=14:
    print("A categoria do atleta {} é JUNIOR" .format(nome_atleta))
elif idade<=19:
    print("A categoria do atleta {} é JUNIOR" .format(nome_atleta))
elif idade<=25:
    print("A categoria do atleta {} é SÊNIOR" .format(nome_atleta))
else:
    print("A categoria do atleta {} é MASTER" .format(nome_atleta))