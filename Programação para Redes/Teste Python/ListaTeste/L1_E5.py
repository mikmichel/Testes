# Solicite o preço de uma mercadoria e o percentual de desconto. exiba o valor do preço a pagar
##############################################################################

#recebendo o valor da mercadoria
preço = float(input("Digite o preço da mercadoria:"))

#recebendo o % de desconto
desconto = float(input("Digite o percentual de desconto:"))

#calculando o valor do desconto
valor_do_desconto = preço * desconto / 100

#calculando o valor do produco já com o desconto
a_pagar = preço - valor_do_desconto

print("Um desconto de %5.2f %% em uma mercadoria de R$ %7.2f" % (desconto, preço))
print("vale R$ %7.2f." % valor_do_desconto)
print("O valor a pagar é de R$ %7.2f" % a_pagar)