import numpy as np

from GrafoTourDelCaballo.Nodo import Nodo
from  GrafoTourDelCaballo.Arista import Arista

class Grafo:

    num_max_vertices = 64
    '''Variable de clase que almacena el número
    máximo de vertices'''

    def __init__(self):
        '''Clase Grafo que sera la estructura
        de nodos conectados.'''
        self.num_vertices = 1
        '''Numero del vertice actual'''
        self.vertices = []
        '''Lista de los vertices que tiene actualmente el grafo'''
        self.matriz_adyacencia = np.array([[0]*(self.num_max_vertices)]*(self.num_max_vertices))
        '''Crea la matriz de adyacencia dado el numero máximo de
        vertices'''
    def nuevo_nodo(self, x, y):
        '''Método para crear un nuevo nodo al grafo'''
        nodo = Nodo(x, y)
        '''Crea un nodo con el valor pasado como parámetro'''
        if self.num_vertices <= self.num_max_vertices and nodo not in self.vertices:
            '''Verifica si el numero de vertice es menor o igual al numero
            maximo de vertices y en nodo creado con el valor actual no esta
            en la lista de vertices del grafo'''
            nodo.asignar_vertice(self.num_vertices)
            '''Añade el numero de vertice al vertice'''
            self.vertices.append(nodo)
            '''Añade el nodo a la lista de vertices del grafo'''
            self.num_vertices += 1
            '''aumenta el numero de vertices la unidad'''

    def indice_vertice(self, x, y):
        '''Obtiene el indice del nodo que tiene
        el valor pasado como parámetro'''
        for item in range(len(self.vertices)):
            '''Recorre cada indice de la lista vertices'''
            if x == self.vertices[item].get_coordenada_x() \
                    and y == self.vertices[item].get_coordenada_y():
                '''Si el valor es igual al nodo dado 
                el indice actual de la lista vertices, 
                retorna el indice'''
                return item
        '''Si no retorna -1, dado que no existe el nodo
        con el valor dado como parámetro'''
        return -1

    def nueva_arista(self, coordenada_x_uno, coordenada_y_uno,
                     coordenada_x_dos, coordenada_y_dos):
        '''Crea una nueva arista dado el valor de un nodo y el
        valor de otro nodo, además de incluir el peso que llevara
        la arista'''
        indice_nodo_uno = self.indice_vertice(coordenada_x_uno, coordenada_y_uno)
        '''Busca el indice del nodo dado el primer valor pasado 
        como parámetro y lo almacena en una variable'''
        indice_nodo_dos = self.indice_vertice(coordenada_x_dos, coordenada_y_dos)
        '''Busca el indice del nodo dado el segundo valor pasado 
        como parámetro y lo almacena en una variable'''
        if indice_nodo_uno < 0 or indice_nodo_dos < 0:
            '''Verifica que los indices sean validos (mayor a cero),
            de lo contrario, retorna un error informando que no
            existe algun vértice'''
            raise ValueError(f"No existe algún vertice. "
                             f"indiceUno: {indice_nodo_uno} - "
                             f"indiceDos: {indice_nodo_dos}")
        else:
            nodo_uno = self.obtener_nodo(coordenada_x_uno, coordenada_y_uno)
            '''Obtenemos el nodo dado el primer valor pasado
            como parámetro y lo almacenamos en una variable'''
            nodo_dos = self.obtener_nodo(coordenada_x_dos, coordenada_y_dos)
            '''Obtenemos el nodo dado el segundo valor pasado
            como parámetro y lo almacenamos en una variable'''
            nodo_uno.get_aristas().append(Arista(nodo_dos))
            '''Añadimos la arista al primer nodo, añadiendo la
            arista a su lista de aristas, pasando como nodo de
            destino el segundo nodo y pasamos el peso gracias a
            la variable pasado como parámetro "peso"'''
            self.matriz_adyacencia[indice_nodo_uno][indice_nodo_dos] = 1
            #self.matriz_adyacencia[indice_nodo_uno][indice_nodo_dos] = nodo_uno
            '''Colocamos en la matriz de adyacencia dado la coordenada
            (indice_nodo_uno, indice_nodo_dos), el peso de la arista
            creada anteriormente'''



    def son_adyacentes(self, coordenada_x_uno, coordenada_y_uno,
                     coordenada_x_dos, coordenada_y_dos):
        '''Verifica si dos nodos son adyacentes dado el valor de
        dos nodos pasado como parámetro'''
        indice_nodo_uno = self.indice_vertice(coordenada_x_uno, coordenada_y_uno)
        '''Busca el indice del nodo dado el primer valor pasado 
        como parámetro y lo almacena en una variable'''
        indice_nodo_dos = self.indice_vertice(coordenada_x_dos, coordenada_y_dos)
        '''Busca el indice del nodo dado el segundo valor pasado 
        como parámetro y lo almacena en una variable'''
        if indice_nodo_uno < 0 or indice_nodo_dos < 0:
            '''Verifica que los indices sean validos (mayor a cero),
            de lo contrario, retorna un error informando que no
            existe algun vértice'''
            raise ValueError(f"No existe algún vertice. "
                             f"indiceUno: {indice_nodo_uno} - "
                             f"indiceDos: {indice_nodo_dos}")

        '''Retorna la evaluacion de casilla dado la coordenada
        (indice_nodo_uno, indice_nodo_dos). Si esa coordenada
        es diferente de 0, entonces los dos nodos son adyacente'''
        return self.matriz_adyacencia[indice_nodo_uno][indice_nodo_dos] != 0

    def obtener_primer_nodo(self):
        '''Obtiene el primer vertice del grafo'''
        if len(self.vertices) != 0:
            '''Si la longitud de la lista vertices
            es diferente de cero, entonces existe
            por lo menos un vertice. retorna el
            primer elemento de la lista vertices'''
            return self.vertices[0]
        '''Si la longitud de la lista vertices
        es igual a cero, entonces no existen 
        vertices aun creados y retorna -1'''
        return -1

    def obtener_ultimo_nodo(self):
        '''Obtiene el primer vertice del grafo'''
        if  len(self.vertices) != 0:
            '''Si la longitud de la lista vertices
            es diferente de cero, entonces existe
            por lo menos un vertice. retorna la longitud de
             la lista vertices - 1 para obtener el último
             vertice creado'''
            return self.vertices[len(self.vertices)-1]
        '''Si la longitud de la lista vertices
        es igual a cero, entonces no existen 
        vertices aun creados y retorna -1'''
        return -1

    def obtener_nodo(self, x, y):
        '''Obtiene el vertice del grafo dado
        el valor pasado como parámetro'''
        if len(self.vertices) != 0:
            '''Si la longitud de la lista vertices
            es diferente de cero, entonces existe 
            al menor un vertice'''
            for item in range(len(self.vertices)):
                '''Recorre cada indice de la lista vertices'''
                if x == self.vertices[item].get_coordenada_x() \
                    and y == self.vertices[item].get_coordenada_y():
                    '''Del nodo en el indice actual en la lista
                    verices obtenemos el valor y si ese valor
                    es igual al valor pasado como parámetro,
                    retornamos el nodo actual'''
                    return self.vertices[item]
            '''Si termina toda la iteración y no encuentra un nodo
            con valor igual al valor pasado como parámetro, retorna
            -1'''
            return -1
        '''Si la longitud de la lista vertices
        es igual a cero, entonces no existen 
        vertices aun creados y retorna -1'''
        return -1

    def get_vertices(self):
        '''get de la variable vertices'''
        return self.vertices


    def __str__(self):
        '''to string del grafp: representación del grafo dad
        la matriz de adyacencia'''
        return self.matriz_adyacencia