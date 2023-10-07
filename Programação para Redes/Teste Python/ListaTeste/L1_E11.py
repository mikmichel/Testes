#"Sabendo que str( ) converte valores numéricos para string, calcule quantos dígitos há em 2 elevado a um milhão."

result=str(int(2**1000000))
print('A quantidade de digitos é: %s' %len(result))