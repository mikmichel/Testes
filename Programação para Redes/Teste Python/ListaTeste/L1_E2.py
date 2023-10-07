#Escreva um programa que leia um valor em metros e o exiba convertido em milímetros
###################################################################################
print("\tConversão de Metros para Milímetros\n")

#Inserindo valor
metros = float(input("Metros: "))

#Calculando conversão
milimetros = (metros * 1000)

#Imprimindo resultado na tela
print("")
print("Conversão em milímetros: %6.2f" %milimetros)