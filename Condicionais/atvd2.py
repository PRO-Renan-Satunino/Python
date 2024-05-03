import os
os.system ("cls || clear")

def calcular_media(notas):
    return sum(notas) / len(notas)

def main():
    nome = input("Digite o nome do aluno: ")
    idade = int(input("Digite a idade do aluno: "))

    notas = []
    for i in range(3):
        nota = float(input(f"Digite a nota {i+1}: "))
        notas.append(nota)

    media = calcular_media(notas)
    
    print(f"O Aluno {nome} tem {idade} anos, e a média das notas e: {media:.2f}")
    
    if media < 7:
        print("Aluno Reprovado")
    else: 
        print("Aluno Aprovado")

if __name__ == "__main__":
    main()
