# Exercícios para trabalhar com classes e herança.

from carro import Carro
from moto import Moto

carro1 = Carro("Volkswagen", "Gol", 4)
carro2 = Carro("Fiat", "Uno", 2)
carro3 = Carro("Honda", "Civic", 4)

moto1 = Moto("Honda", "CBR", "Esportiva")
moto2 = Moto("Honda", "Betoneira", "Esportiva")
moto3 = Moto("Yamaha", "ZX", "Casual")

def main():
    Carro.listar_carros()
    Moto.listar_motos()

if __name__ == "__main__": 
    main()