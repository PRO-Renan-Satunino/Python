from abc import ABC, abstractclassmethod
import os

os.system("cls || clear")

class Endereco: 
    def __init__(self, logradouro:str, numero:str, complemento:str, cep:str, cidade:str) -> None:
        self.logradouro = logradouro
        self.numero = numero
        self.complemento = complemento
        self.cep = cep
        self.cidade = cidade

    def __str__(self) -> str:
        return (
            f"\nLogradouro: {self.logradouro}"
            f"\nNumero: {self.numero}"
            f"\nComplemento: {self.complemento}"
            f"\nCEP: {self.cep}"
            f"\nCidade: {self.cidade}"
            )
    
class Funcionario(ABC):
    def __init__(self, nome:str, salario:float, telefone:str, email:str) -> None:
        self.nome = nome
        self.salario = salario
        self.telefone = telefone
        self.email = email
        endereco = Endereco

    @abstractclassmethod
    def salario_final(self) -> float:
        pass

    def __str__(self) -> str:
        return (
            f"\nNome: {self.nome}"
            f"\nSalario: {self.salario}"
            f"\nTelefone: {self.telefone}"
            f"\nEmail: {self.email}"
            f"\nEndereco-- {Endereco}"
        )
    
class Engenheiro(Funcionario):
    BONIFICACAO = 1.5

    def salario_final(self) -> float:
        resultado = self.salario * self.BONIFICACAO
        return resultado

    def __init__(self, nome: str, salario: float, telefone: str, email: str) -> None:
        super().__init__(nome, salario, telefone, email)