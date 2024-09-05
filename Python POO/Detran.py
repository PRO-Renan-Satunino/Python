import random
import string

class Veiculo:
    def __init__(self, placa: str, modelo: str, ano: int) -> None:
        self.placa = placa
        self.modelo = modelo
        self.ano = ano

class SistemaEmplacamento:
    def __init__(self):
        self.veiculos = {}

    def gerar_placa(self) -> str:
        """
        Gera uma placa no formato ABC1D23.
        - ABC: Letras
        - 1D: Número e uma letra
        - 23: Dois números
        """
        letras = ''.join(random.choices(string.ascii_uppercase, k=3))
        numeros = ''.join(random.choices(string.digits, k=2))
        letra = random.choice(string.ascii_uppercase)
        placa = f"{letras}{random.choice(string.digits)}{letra}{numeros}"
        return placa

    def cadastrar_veiculo(self, modelo: str, ano: int) -> str:
        """
        Cadastra um veículo e retorna a placa gerada.
        """
        placa = self.gerar_placa()
        while placa in self.veiculos:
            placa = self.gerar_placa()  # Gera uma nova placa se a atual já estiver em uso
        veiculo = Veiculo(placa, modelo, ano)
        self.veiculos[placa] = veiculo
        return placa

    def consultar_veiculo(self, placa: str) -> str:
        """
        Consulta o veículo pelo número da placa.
        """
        veiculo = self.veiculos.get(placa)
        if veiculo:
            return f"Placa: {veiculo.placa}, Modelo: {veiculo.modelo}, Ano: {veiculo.ano}"
        else:
            return "Veículo não encontrado."

    def listar_veiculos(self) -> str:
        """
        Lista todos os veículos cadastrados.
        """
        if not self.veiculos:
            return "Nenhum veículo cadastrado."
        return '\n'.join(f"Placa: {v.placa}, Modelo: {v.modelo}, Ano: {v.ano}" for v in self.veiculos.values())

# Exemplo de uso:
sistema = SistemaEmplacamento()

# Cadastrar veículos
placa1 = sistema.cadastrar_veiculo("Fusca", 1974)
placa2 = sistema.cadastrar_veiculo("Civic", 2022)

print(f"Veículo cadastrado com placa: {placa1}")
print(f"Veículo cadastrado com placa: {placa2}")

# Consultar veículos
print(sistema.consultar_veiculo(placa1))
print(sistema.consultar_veiculo("XYZ1234"))  # Placa que não existe

# Listar todos os veículos
print("Todos os veículos cadastrados:")
print(sistema.listar_veiculos())
