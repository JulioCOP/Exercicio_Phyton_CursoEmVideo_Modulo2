#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa,
# o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário
# ou então o empréstimo será negado.

valor_casa= float(input("Qual o valor da casa ? "))
salario= float(input("Qual o salario do comprador ? "))
anos= int(input("Quantos anos o usuario deseja financiar a casa ? "))
valor_prestacao= (valor_casa/ (anos*12))
print("Essa casa será paga em {} anos, com valor de prestação de R$ {:.2f} " .format(anos, valor_prestacao))
limite= salario*0.3
print("O limitido permitido para o comprador pagar é até {:.2f}".format(limite))
if valor_prestacao<=limite:
    print("Emprestimo PERMITIDO")
else:
    print("Emprestimo NEGADO, o salario do funcionário excede o limite permitido")
