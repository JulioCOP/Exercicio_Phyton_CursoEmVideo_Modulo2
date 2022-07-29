#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e
# condição de pagamento:

#– à vista dinheiro/cheque: 10% de desconto

#– à vista no cartão: 5% de desconto

#– em até 2x no cartão: preço formal

#– 3x ou mais no cartão: 20% de juros

from time import sleep
import emoji

valor_produto=float(input("Informe o valor do produto: R$ "))
print('''Digite sua forma de pagamento
[ 1 ]   a vista dinheiro/cheque
[ 2 ]   a vista no cartão
[ 3 ]   em até 2x no cartão
[ 4 ]   3x ou mais no cartão''')
opcao=int(input("Digite a opção desejada pelo cliente: "))
if opcao==1:
    print("O cliente ganhou 10% de desconto!")
    print(emoji.emojize("PROCESSANDO...:running:\nAGUARDE :wink: ", use_aliases=True))
    sleep(2)
    valor_pagar= (valor_produto - (valor_produto*0.1))
    print("O valor total do produto a ser pago com desconto é {} R$ {:.2f} {}".format('\033[1;31;40m',valor_pagar, '\033[m'))
elif opcao==2:
    print("O cliente ganhou 5% de deconto!")
    print(emoji.emojize("PROCESSANDO...:running:\nAGUARDE :wink:", use_aliases=True))
    sleep(2)
    valor_pagar= (valor_produto-(valor_produto*0.05))
    print("O valor total a ser pago pelo cliente com o desconto é {} R${:.2f} {}".format('\033[1;31;40m',valor_pagar,'\033[m'))
elif opcao==3:
    print("O cliente NÃO TEM direito a desconto!")
    print(emoji.emojize("PROCESSANDO...:running:\nAGUARDE :wink: ", use_aliases=True))
    sleep(2)
    valor_pagar=valor_produto/2
    print("O valor a ser pago pelo cliente é {} 2xR$ {:.2f} {}".format('\033[1;31;40m',valor_pagar, '\033[m'))
else:
    print("O cliente realizará o pagamento com juros de 20%!")
    print(emoji.emojize("PROCESSANDO...:running: AGUARDE :wink:", use_aliases=True))
    sleep(2)
    valor_pagar= ((valor_produto+(valor_produto*0.2))/3)
    print("O valor a ser pelo cliente é {} 3xR$ {:.2f} {}".format('\033[1;31;40m',valor_pagar,'\033[m'))



