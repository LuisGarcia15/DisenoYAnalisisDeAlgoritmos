class Nodo:

    def __init__(self, valor):
        '''Clase Nodo que sera el vertice de
        un grafo. Recibe como parámetro
        el valor que almacena el grafo'''
        self.__valor = valor
        '''Tendra una variable num:vertice que sera
        el número de vertice del nodo'''
        self.__num_vertice = -1
        '''Tendra una lista con las aristas asi donde
        se conecta el nodo'''
        self.__aristas = []

    def get_valor(self):
        '''get de la variable valor'''
        return self.__valor

    def set_valor(self, valor):
        '''set de la variable valor'''
        self._valor = valor

    def get_aristas(self):
        '''get de la variable aristas'''
        return self.__aristas

    def grado_nodo(self):
        '''obtiene el grado del nodo'''
        return len(self.__aristas)

    def es_igual(self, nodo):
        '''verifica si un nodo es igual a otro'''
        return self.__valor == nodo.get_valor()

    def asignar_vertice(self, num_vertice):
        '''añade el numero de vertice al vertice'''
        self.num_vertice = num_vertice

    def __str__(self):
        '''to string del nodo: representación del nodo'''
        return f'Valor: {self.__valor} - Número De Vertice: {self.num_vertice}'