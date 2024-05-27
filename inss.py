#Uma parte do codigo ta em ingles pq eu tava digitando com a linguagem ingles do teclado e tava com preguica de mudar o idioma toda hora so pra colocar acento.

import os
os.system("cls || clear")

def calcular_inss(salary):
    if salary <= 1100.00:
        inss = salary * 0.075
    elif 1100.01 <= salary <= 2203.48:
        inss = salary * 0.09
    elif 2203.49 <= salary <= 3305.22:
        inss = salary * 0.12
    elif 3305.23 <= salary <= 6433.57:
        inss = salary * 0.14
    else:
        inss = 854.36
    return inss
    
def calcular_ir(salary):
    inss = calcular_inss(salary)
    base_ir = salary - inss
    
    if base_ir <= 2259.20:
        ir = 0
    elif 2259.21 <= base_ir <= 2826.65:
        ir = (salary * 0.075) 
    elif 2826.66 <= base_ir <= 3751.05:
        ir = (salary * 0.15) 
    elif 3751.06 <= base_ir <= 4664.68:
        ir = (salary * 0.225) 
    elif base_ir >= 4664.69:
        ir = (salary * 0.275) 
        
    return ir
    
def calcular_impostos(salary):
    inss = calcular_inss(salary)
    ir = calcular_ir(salary)
    valor_dependente = dependente * 189.59
    valeRef = valorRef * 0.2
    planSaude = 150
    salaryLiq = salary - (ir + planSaude + valeRef + valeTrans + inss + valor_dependente)
    
    
    return inss, ir, valor_dependente, salaryLiq
    
dependente = []
#Programa Principal
os.system("cls || clear")
matricula = int(input("Insira seu numero de matricula: "))
senha = int(input("Insira sua senha: "))
salary = float(input("Insira seu salário: "))
valorRef = float(input("Qual o valor do seu Vale Refeicao: "))
dependente = int(input("Quantidade de dependentes: "))
transporte = input("Voce deseja receber o vale transporte? (s/n): ")
if transporte == 's':
    valeTrans = salary * 0.06
else:
    valeTrans = 0

inss, ir, valor_dependente, salaryLiq = calcular_impostos(salary)
    
#Mostrando Dados para o Usuario
print(f"Salario Bruto: {salary:.2f}")
print(f"INSS: {inss:.2f}")
print(f"Imposto de Renda: {ir:.2f}")
print(f"Dependentes: {dependente} \nValor a ser pago: {valor_dependente}")
print(f"Salario Liquido: {salaryLiq:.2f}")
