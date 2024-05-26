import os

# Função sem retorno
def logoSenai():
    os.system("cls || clear")
    print("=== SENAI ===")

# Definindo listas vazias para armazenar dados dos usuários
nome = []
idade = []
altura = []
peso = []
usuarios = []

def calcular_imc(peso, altura):
    return peso / (altura ** 2)

def resultado_imc(imc):
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
        return "Obesidade Grau III (Mórbida)"

#programa principal
#Solicitando os dados em loop
while True:
    logoSenai()
    nome = input("Digite o nome completo do usuário (escreva 'sair' para cancelar)")
    if nome.lower() == 'sair':
        break
        
    idade = int (input("Digite a Idade do Usuário: "))
    altura = float(input("Digite a altura do usuário (metros): "))
    peso = float(input("Digite o peso do usuário (metros): "))

    usuarios.append((nome, altura, peso, idade))
        
#exibindo dados
logoSenai()
print("\nDados dos Usuarios:")
for nome, altura, peso, idade in usuarios:
    imc = calcular_imc(peso, altura)
    classificacao = resultado_imc(imc)
    print(f"{nome} de {idade} anos, seu IMC é: {imc:.2f}. \nClassificação: {classificacao}")
    print(f"Seu Peso: {peso}")
    print(f"Sua Altura: {altura}")