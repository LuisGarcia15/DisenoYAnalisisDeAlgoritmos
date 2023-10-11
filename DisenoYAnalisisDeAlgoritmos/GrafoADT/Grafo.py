import numpy as np

from GrafoADT.Nodo import Nodo
from  GrafoADT.Arista import Arista

class Grafo:

    num_max_vertices = 10

    def __init__(self):
        self.num_vertices = 1
        self.vertices = []
        self.matriz_adyacencia = np.array([[0]*(self.num_max_vertices)]*(self.num_max_vertices))

    def nuevo_nodo(self, valor):
        nodo = Nodo(valor)
        if self.num_vertices <= 10 and nodo not in self.vertices:
            nodo.asignar_vertice(self.num_vertices)
            self.vertices.append(nodo)
            self.num_vertices += 1

    def indice_vertice(self, valor):
        for item in range(len(self.vertices)):
            if valor == self.vertices[item].get_valor:
                return item
        return -1

    def nueva_arista(self, valor_nodo_uno, valor_nodo_dos, peso):
        indice_nodo_uno = self.indice_vertice(valor_nodo_uno)
        indice_nodo_dos = self.indice_vertice(valor_nodo_dos)
        if indice_nodo_uno < 0 or indice_nodo_dos < 0:
            raise ValueError("No existe algún vertice")
        nodo_uno = self.obtener_nodo(valor_nodo_uno)
        nodo_dos = self.obtener_nodo(valor_nodo_dos)
        nodo_uno.get_aristas.append(Arista(nodo_dos, peso))
        nodo_dos.get_aristas.append(Arista(nodo_uno, peso))
        self.matriz_adyacencia[indice_nodo_uno][indice_nodo_dos] = peso
        self.matriz_adyacencia[indice_nodo_dos][indice_nodo_uno] = peso

    def son_adyacentes(self, valor_nodo_uno, valor_nodo_dos):
        indice_nodo_uno = self.indice_vertice(valor_nodo_uno)
        indice_nodo_dos = self.indice_vertice(valor_nodo_dos)
        if indice_nodo_uno < 0 or indice_nodo_dos < 0:
            raise ValueError("No existe algún vertice")
        return self.matriz_adyacencia[indice_nodo_uno][indice_nodo_dos] == 1

    def obtener_primer_nodo(self):
        if  len(self.vertices) != 0:
            return self.vertices[0]
        return -1

    def obtener_ultimo_nodo(self):
        if  len(self.vertices) != 0:
            return self.vertices[len(self.vertices)-1]
        return -1

    def obtener_nodo(self, valor):
        if len(self.vertices) != 0:
            for item in range(len(self.vertices)):
                if self.vertices[item].get_valor == valor:
                    return self.vertices[item]
        return -1

    def __str__(self):
        return self.matriz_adyacencia