import os
os.system ("cls || clear")

idade = int (input("Digite sua idade: "))

if idade < 18 or idade > 65:
    print("Você não é obrigado a votar!")

else :
    print("Você é obrigado a votar!")