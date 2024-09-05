import os

os.system("clear || cls")

# Definindo a exceção personalizada
class SaldoInsuficiente(Exception):
    pass

class Conta:
    def __init__(self, numero_conta: int, agencia: int) -> None:
        self.numero_conta = numero_conta
        self.agencia = agencia
        self._saldo = 0  # atributo protegido

    def saldo(self) -> float:
        return self._saldo
    
    def sacar(self, valor: float) -> str:
        try:
            self.__verificar_sacar(valor)
        except SaldoInsuficiente as erro:
            return f"Erro: {erro}"
        return f"Saque realizado com sucesso. Saldo atual: {self._saldo}"
    
    def __verificar_sacar(self, valor: float) -> None:  # Método Privado
        if valor > self._saldo:
            raise SaldoInsuficiente("Saldo Insuficiente")
        self._saldo -= valor

    def depositar(self, valor: float) -> str:
        if valor <= 0:
            return "Valor para depósito deve ser positivo."
        self._saldo += valor
        return f"Depósito realizado com sucesso. Saldo atual: {self._saldo}"

class ContaCorrente(Conta):
    def __init__(self, numero_conta: int, agencia: int, limite: float = 0) -> None:
        super().__init__(numero_conta, agencia)
        self.limite = limite  # Limite especial para a conta corrente

    def sacar(self, valor: float) -> str:
        try:
            if valor > (self._saldo + self.limite):
                raise SaldoInsuficiente("Saldo e limite insuficientes")
            if valor > self._saldo:
                self._saldo -= valor
            else:
                self._saldo -= valor
        except SaldoInsuficiente as erro:
            return f"Erro: {erro}"
        return f"Saque realizado com sucesso. Saldo atual: {self._saldo}"

class ContaPoupanca(Conta):
    def __init__(self, numero_conta: int, agencia: int, rendimento: float) -> None:
        super().__init__(numero_conta, agencia)
        self.rendimento = rendimento  # Taxa de rendimento da conta poupança

    def aplicar_rendimento(self) -> None:
        self._saldo += self._saldo * (self.rendimento / 100)

# Exemplo de uso:
conta_corrente = ContaCorrente(222, 334, limite=500)
conta_poupanca = ContaPoupanca(333, 555, rendimento=1.5)

# Depositando e sacando valores
print(conta_corrente.depositar(1000))
print(conta_corrente.sacar(1200))  # Deve usar o limite
print(conta_corrente.sacar(500))   # Deve falhar se o limite não for suficiente

print(conta_poupanca.depositar(2000))
conta_poupanca.aplicar_rendimento()
print(f"Saldo da Poupança após rendimento: {conta_poupanca.saldo()}")

# Informações de saldo
print(f"Saldo da Conta Corrente: {conta_corrente.saldo()}")
print(f"Saldo da Conta Poupança: {conta_poupanca.saldo()}")
