from veiculo import Veiculo

class Carro(Veiculo):
    lista_carros = []
    def __init__(self, marca, modelo, portas):
        super().__init__(marca, modelo)
        self._portas = portas
        Carro.lista_carros.append(self)

    def __str__(self):
        return f"Marca: {self.marca}\nModelo: {self.modelo}\nPortas: {self._portas}\nLigado: {self._ligado}"
    
    @classmethod   
    def listar_carros(cls):
        print(f'{"Marca".ljust(25)} | {"Modelo".ljust(25)} | {"Portas".ljust(10)} | {"Ligado".ljust(10)}')
        for carro in cls.lista_carros:
            print(f'{carro.marca.ljust(25)} | {carro.modelo.ljust(25)} | {str(carro._portas).ljust(10)} | {str(carro._ligado).ljust(10)}')
