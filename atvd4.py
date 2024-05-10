import os
os.system("cls || clear")

nome = str(input("Digite seu nome: "))
sexo = str(input("Informe seu sexo (M/F): "))
estadoCivil = str(input("Estado Civil:"))

if sexo == "F" or sexo == "f" and estadoCivil == "Casada" or estadoCivil == "casada":
    tempoDeCasada = float(input("Informe seu tempo de casada em anos:  "))
if tempoDeCasada > 14 :
    print("Ja dá pra divorciar")