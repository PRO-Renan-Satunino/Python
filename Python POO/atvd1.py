class ContaBancaria:
    def __init__ (self, banco:str, agencia:str, numeroConta:str, tipoConta:str, saldo:str, limite:str) -> None:
        self.banco = banco
        self.agencia = agencia
        self.numeroConta = numeroConta
        self.tipoConta = tipoConta
        self.saldo = saldo
        self.limite = limite

        def __str__ (self):
            return f"Banco: {self.banco} \nAgencia: {self.agencia} \nNumero da Conta: {self.numeroConta} \nTipo da Conta: {self.tipoConta} \nSaldo: {self.saldo} \nLimite: {self.limite}"

        
class Funcionario:
    def __init__(self, codigoFuncionario:str, nome:str, telefone:str, email:str, ContaBancaria) -> None:
        self.codigoFuncionario = codigoFuncionario
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.ContaBancaria = ContaBancaria
    
    def __str__(self):
        return f"Cod. Funcionario: {self.codigoFuncionario} \nNome: {self.nome} \nTelefone: {self.telefone} \nEmail: {self.email} \n--Conta Bancaria-- {ContaBancaria}"

        