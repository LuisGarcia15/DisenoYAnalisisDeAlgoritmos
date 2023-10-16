class Nodo:

    def __init__(self, x, y):
        '''Clase Nodo que sera el vertice de
        un grafo. Recibe como parámetro
        el valor que almacena el grafo'''
        self.__coordenada_x = x
        '''Tendra una variable num:vertice que sera
        el número de vertice del nodo'''
        self.__coordenada_y = y
        self.__fue_visitado = False
        self.__num_casillas_adycentes = 0
        self.__num_vertice = -1
        '''Tendra una lista con las aristas asi donde
        se conecta el nodo'''
        self.__aristas = []

    def get_coordenada_x(self):
        '''get de la variable valor'''
        return self.__coordenada_x

    def get_coordenada_y(self):
        '''get de la variable valor'''
        return self.__coordenada_y

    def get_fue_visitado(self):
        '''get de la variable valor'''
        return self.__fue_visitado

    def get_aristas(self):
        '''get de la variable aristas'''
        return self.__aristas

    def get_num_casillas_adyacentes(self):
        '''get de la variable aristas'''
        return self.__num_casillas_adycentes

    def set_coordenada_x(self, x):
        '''set de la variable valor'''
        self.__coordenada_x = x

    def set_coordenada_y(self, y):
        '''set de la variable valor'''
        self.__coordenada_y = y

    def set_fue_visitado(self, valor):
        '''set de la variable valor'''
        self.__fue_visitado = valor

    def aumentar_num_casillas_adyacentes(self):
        '''set de la variable valor'''
        self.__num_casillas_adycentes += 1

    def disminuir_num_casillas_adyacentes(self):
        '''set de la variable valor'''
        self.__num_casillas_adycentes -= 1

    def grado_nodo(self):
        '''obtiene el grado del nodo'''
        return len(self.__aristas)

    def asignar_vertice(self, num_vertice):
        '''añade el numero de vertice al vertice'''
        self.num_vertice = num_vertice

    def __str__(self):
        '''to string del nodo: representación del nodo'''
        return f'(Coordenada X: {self.__coordenada_x}, ' \
               f'Coordenada Y: {self.__coordenada_y}) - ' \
               f'Número de caillas adyacentes: {self.__num_casillas_adycentes}' \
               f'- Número De Vertice: {self.num_vertice}'