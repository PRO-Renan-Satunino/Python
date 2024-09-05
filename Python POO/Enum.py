from enum import Enum #importador do Enum
import os

os.system("clear")

class Sexo(Enum):
    MASCULINO = "Masculino"
    FEMININO = "Feminino"
    
#Aplicação
print(f"Sexo: {Sexo.FEMININO}") #Mostra o Enum puro
print(f"Sexo: {Sexo.FEMININO.name}") #Mostra a identificação do Enum
print(f"Sexo: {Sexo.FEMININO.value}") #Mostra o texto do Enum
