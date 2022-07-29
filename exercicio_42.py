#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não
# formar um triângulo. Além disso, mostre que tipo de triangulo foi formado.
#– EQUILÁTERO: todos os lados iguais

#– ISÓSCELES: dois lados iguais, um diferente

#– ESCALENO: todos os lados diferentes

#Para formar um triãngulo é necessário que: a soma dos dois lados menores, seja maior que o terceiro lado.

s1= float(input("Informe o valor do primeiro segmento do triângulo: "))
s2= float(input("Informe o valor do segundo segmento do triângulo: "))
s3= float(input("Informe o valor do terceiro segmento do triângulo: "))
soma_lados= s1+s2
if soma_lados>s3:
    print("A partir dos valores informados é possível formar um triângulo.")
    if s1!=s2 or s2!=s3 or s3!=s1:
        print("TRIANGULO ESCALENO")
    elif s1==s2==s3:
        print("TRIÂNGULO EQUILÁTERO")
    else:
        print("TRIANGULO ISOSCELES")
else:
    print("NÃO FOI POSSIVEL FORMAR UM TRIANGULO")