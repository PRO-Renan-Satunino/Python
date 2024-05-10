import os
os.system ("cls || clear")

media = 0
soma = 0

for i in range (1, 5) :
    nota = float(input(f"Digite a {i} nota: "))
    soma += nota

media = soma / 4

print(f"Sua Media e: {media}")