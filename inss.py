import os
os.system("cls || clear")

def calcular_inss(salary):
    if salary <= 1412.00:
        inss = salary * 0.075
    elif 1412.01 <= salary <= 2666.68:
        inss = salary * 0.09
    elif 2666.69 <= salary <= 4000.03:
        inss = salary * 0.12
    elif 4000.04 <= salary <= 7386.02:
        inss = salary * 0.14
    else: 
        inss = 877.24 #teto do INSS
    
    return inss

def calcular_ir(salary):
    inss = calcular_inss(salary)
    base_ir = salary - inss

    if base_ir <= 1903.98:
        ir = 0
    elif base_ir <= 2826.65:
        ir = (base_ir - 1903.98) * 0.075 - 142.80
    elif base_ir <= 3751.05:
        ir = (base_ir - 2826.65) * 0.16  - 354.80
    elif base_ir <= 4664.68:
        ir = (base_ir - 3751.05) * 0.225 - 636.13
    else:
        ir = (base_ir - 4664.68) * 0.275 - 869.36

    return ir
def calcular_impostos(salary):
    inss = calcular_inss(salary)
    ir = calcular_ir(salary)
    return inss, ir


#Programa Principal
os.system("cls || clear")
salary = float(input("Insert your Salary: "))
inss, ir = calcular_impostos(salary)
print(f"Brute Salary: {salary:.2f}")
print(f"INSS: {inss:.2f}")
print(f"Imposto de Renda: {ir:.2f}")