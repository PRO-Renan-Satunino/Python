from abc import ABC, abstractclassmethod #importador do Abstract
import os

os.system("cls || clear")

class Funcionario(ABC):
    def __init__(self, nome:str, salario:float) -> None:
        self.nome = nome
        self.salario = salario    

    @abstractclassmethod #transforma em uma classe abstrata
    def salario_final(self) -> float:
        pass 
        
    def __str__(self) -> str:
        return (
            f"\nNome: {self.nome}"
            f"\nSalario: {self.salario}"
            f"\nSalario Final: {self.salario_final()}"
        )
    
    
class Motoboy(Funcionario): #chama funcionario para dentro de Motoboy, como o Extend do Java
    #acrecimo de 10%
    BONIFICACAO = 1.1

    def salario_final(self) -> float:
        resultado = self.salario * self.BONIFICACAO
        return resultado
    
class Engenheiro(Funcionario):
    BONIFICACAO = 1.2

    def __str__(self, crea:str) -> str:
        return (
            f"\nCREA: {self.crea}"
        )

    def salario_final(self) -> float:
        resultado = self.salario * self.BONIFICACAO
        return resultado


#instanciando classes
motoboy1 = Motoboy("Joao", 2000)
eng1 = Engenheiro("Maicon", 9000)

print(motoboy1)
print(eng1)