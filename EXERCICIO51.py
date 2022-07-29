#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos
#dessa progressão
#termo progressão aritimética an=a1+(n-1)*r

t=int(input("Informe o primeiro termo da PA: "))
r= int(input("Informe a razão dessa PA: "))
for c in range (1,11):
    pa=(t+((c-1)*r))
    print("{}".format(pa), end='->')
print("FIM DO PROGRAMA")
