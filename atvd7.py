import os
os.system("cls || clear")

soma = 0 #declarando que soma e 0

for i in range (1, 6) :
    numero = int(input(f"Digite o {i} numero:  "))

    soma += numero #adicionando um valor a soma toda vez que e inserido
print(f"\nSoma total dos numeros: {soma}")