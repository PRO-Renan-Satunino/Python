import os
os.system ("clear || cls")

par = 0 #declarando par com valor 0
impar = 0

for i in range (5) :
    numero = int(input(f"Digite o {1 + i} valor: "))

    if numero % 2 == 0:
        par += 1
    else :
        impar += 1
    
print(f"Quantidade de numeros pares: {par}")
print(f"Quantidade de numeros impares: {impar}")