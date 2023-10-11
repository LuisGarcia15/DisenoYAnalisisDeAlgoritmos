class Nodo:

    def __init__(self, valor):
        self.valor = valor
        self.num_vertice = -1
        self.aristas = []

    @property
    def get_valor(self):
        return self.valor

    @property
    def get_aristas(self):
        return self.aristas

    def grado_nodo(self):
        return len(self.aristas)

    def es_igual(self, nodo):
        return self.valor == nodo.get_valor()

    def asignar_vertice(self, num_vertice):
        self.num_vertice = num_vertice

    def __str__(self):
        return f'Valor: {self.valor} - Número De Vertice: {self.num_vertice}'