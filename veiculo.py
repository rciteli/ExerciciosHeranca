class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self._ligado = False

    def __str__(self):
        return f"Marca: {self.marca}\nModelo: {self.modelo}\nLigado: {self._ligado}"
    
    
            