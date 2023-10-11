class Arista:

    def __init__(self, nodo_destino, peso):
        self.nodo_destino = nodo_destino
        self.peso = peso

    def __str__(self):
        return f'Destino: [{self.nodo_destino}] | Peso: {self.peso}'