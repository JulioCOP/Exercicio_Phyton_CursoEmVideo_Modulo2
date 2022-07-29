#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços

f=str(input("Digite uma frase: ").strip() .upper())
palavras= f.split()
palavras_juntas = ''.join(palavras)
inverso= ""
for letra in range(len(palavras_juntas)-1,-1,-1):
    inverso += palavras_juntas[letra]
print("O inverso de {} é: {} ".format(palavras_juntas,inverso))
if inverso==palavras_juntas:
    print("TEMOS UM PALÍNDROMO")
else:
    print("NÃO É UM PALINDROMO")

