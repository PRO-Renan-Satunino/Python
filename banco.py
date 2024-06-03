import os
import time
os.system ("cls||clear")

def TED():
    global conta
    destinatario = int(input("Digite o codigo do destinatario: "))
    valor = float(input("Insira o Valor: "))
    os.system("clear||cls")
    print("Processando...")
    time.sleep(5)
    os.system("cls||clear")
    print("Trasnferência Concluída!")
    conta -= valor
    print(f"Você possui: {conta}")

def PIX():
    global conta
    chavePIX = int(input("Digite a chave PIX: "))
    valor = float(input("Insira o valor: "))
    os.system("clear||cls")
    print("Processando...")
    time.sleep(5)
    os.system("clear||cls")
    print("Trasnferência Concluida!")
    conta -= valor
    print(f"Você possui: {conta}")

def poupanca():
    global conta
    poupar = float(input("Quanto você deseja depositar: "))
    conta -= poupar
    print(f"Você depositou: {poupar}")
    print(f"Você possui: {conta}")

def saque():
    global conta
    saque = float(input("Digite o valor do saque: "))
    conta -= saque
    print(f"Você possui: {conta}")

def deposito():
    global conta
    adicao = float(input("Quanto você deseja depositar: "))
    conta += adicao
    print(f"Saldo: {conta}")

def switchcase(option):
    switch = {
        1: TED,
        2: PIX,
        3: poupanca,
        4: saque,
        5: deposito,
    }
    func = switch.get(option)
    if func:
        func()
    else:
        print("Opção inválida.")

#Programa Principal
conta = 5000
option = []

print("====Bem vindo ao Oprah Banking!====")

while True: 
    print("Escolha uma ação: ")
    print("1    | TED")
    print("2    | PIX")
    print("3    | Poupança")
    print("4    | Saque")
    print("5    | Deposito")
    print("0    | Sair")

    option = int(input("Digite o Código: "))
    if option == 0: 
        print("Obrigado por utilizar o Oprah Banking!")
        break

    switchcase(option)

