import os
os.system("clear || cls")

numero = float (input("Digite um numero: "))
for i in range (1,11):
    print(f"{numero} x  {i} = {numero * i}")