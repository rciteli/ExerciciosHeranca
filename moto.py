from veiculo import Veiculo

class Moto(Veiculo):
    lista_motos = []
    def __init__(self, marca, modelo, tipo):
        super().__init__(marca, modelo)
        self._tipo = tipo
        Moto.lista_motos.append(self)

    def __str__(self):
        return f"Marca: {self.marca}\nModelo: {self.modelo}\nTipo: {self._tipo}"
    
    @classmethod
    def listar_motos(cls):
        print(f'{"Marca".ljust(25)} | {"Modelo".ljust(25)} | {"Tipo".ljust(10)}')
        for moto in cls.lista_motos:
            print(f'{moto.marca.ljust(25)} | {moto.modelo.ljust(25)} | {moto._tipo.ljust(10)}')
