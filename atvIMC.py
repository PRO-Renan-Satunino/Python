import os
os.system ("cls || clear")

def calcular_imc(peso, altura):
    return peso / (altura ** 2)

def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do Peso"
    elif 18.5 <= imc < 24.9:
        return "Peso Ideal"
    elif 25.0 <= imc < 29.9:
        return "Sobrepeso"
    elif 30.0 <= imc < 34.9:
        return "Obesidade Grau I"
    elif 35.0 <= imc < 39.9:
        return "Obesidade Grau II"
    else:
        return "Obesidade Grau III (Morbida)"
usuarios = []
nome = []

while True:
    os.system ("cls || clear")
    nome = input("Digite seu nome (ou 'sair' para encerrar): ")
    if nome.lower() == "sair":
        break

    altura = float(input("Digite sua altura em metros (ex: 1.75): "))
    peso = float(input("Digite seu peso em quilogramas (ex: 70.5): "))
    usuarios.append((nome, altura, peso))

    if altura == 0 or peso == 0:
        print("Por favor, digite um valor valido")

    #exibindo dados
print("\nResultados")
for nome, altura, peso in usuarios: 
    imc = calcular_imc(peso, altura)
    classificacao = classificar_imc(imc)
    print(f"{nome}, seu IMC é {imc:.2f}. Classificação: {classificacao}")     
    print(f"Sua Altura: {altura}")
    print(f"Seu Peso: {peso}")
    print(f"Seu IMC: {imc}")
    print(f"Sua Situação é: {classificacao}")
