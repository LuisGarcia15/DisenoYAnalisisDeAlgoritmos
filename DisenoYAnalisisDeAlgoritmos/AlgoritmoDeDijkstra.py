import numpy as np
class Arista:

    def __init__(self, nodo_destino, peso):
        '''Clase Arista que sera la arista de
        un nodo. Recibe como parámetro
        el peso de la arista y el nodo destino'''
        self.nodo_destino = nodo_destino
        self.peso = peso

    def get_peso(self):
        '''get de la variable peso'''
        return self.peso

    def obtener_destino(self):
        '''Obtiene el destino de la arista'''
        return self.nodo_destino.get_valor()

    def __str__(self):
        '''to string de la arista: representación de la arista'''
        return f'Destino: [{self.nodo_destino}] | Peso: {self.peso}'

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

class Grafo:

    num_max_vertices = 6
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
    def nuevo_nodo(self, valor):
        '''Método para crear un nuevo nodo al grafo'''
        nodo = Nodo(valor)
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

    def indice_vertice(self, valor):
        '''Obtiene el indice del nodo que tiene
        el valor pasado como parámetro'''
        for item in range(len(self.vertices)):
            '''Recorre cada indice de la lista vertices'''
            if valor == self.vertices[item].get_valor():
                '''Si el valor es igual al nodo dado 
                el indice actual de la lista vertices, 
                retorna el indice'''
                return item
        '''Si no retorna -1, dado que no existe el nodo
        con el valor dado como parámetro'''
        return -1

    def nueva_arista(self, valor_nodo_uno, valor_nodo_dos, peso):
        '''Crea una nueva arista dado el valor de un nodo y el
        valor de otro nodo, además de incluir el peso que llevara
        la arista'''
        indice_nodo_uno = self.indice_vertice(valor_nodo_uno)
        '''Busca el indice del nodo dado el primer valor pasado 
        como parámetro y lo almacena en una variable'''
        indice_nodo_dos = self.indice_vertice(valor_nodo_dos)
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
            nodo_uno = self.obtener_nodo(valor_nodo_uno)
            '''Obtenemos el nodo dado el primer valor pasado
            como parámetro y lo almacenamos en una variable'''
            nodo_dos = self.obtener_nodo(valor_nodo_dos)
            '''Obtenemos el nodo dado el segundo valor pasado
            como parámetro y lo almacenamos en una variable'''
            nodo_uno.get_aristas().append(Arista(nodo_dos, peso))
            '''Añadimos la arista al primer nodo, añadiendo la
            arista a su lista de aristas, pasando como nodo de
            destino el segundo nodo y pasamos el peso gracias a
            la variable pasado como parámetro "peso"'''
            self.matriz_adyacencia[indice_nodo_uno][indice_nodo_dos] = peso
            '''Colocamos en la matriz de adyacencia dado la coordenada
            (indice_nodo_uno, indice_nodo_dos), el peso de la arista
            creada anteriormente'''



    def son_adyacentes(self, valor_nodo_uno, valor_nodo_dos):
        '''Verifica si dos nodos son adyacentes dado el valor de
        dos nodos pasado como parámetro'''
        indice_nodo_uno = self.indice_vertice(valor_nodo_uno)
        '''Busca el indice del nodo dado el primer valor pasado 
        como parámetro y lo almacena en una variable'''
        indice_nodo_dos = self.indice_vertice(valor_nodo_dos)
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

    def obtener_nodo(self, valor):
        '''Obtiene el vertice del grafo dado
        el valor pasado como parámetro'''
        if len(self.vertices) != 0:
            '''Si la longitud de la lista vertices
            es diferente de cero, entonces existe 
            al menor un vertice'''
            for item in range(len(self.vertices)):
                '''Recorre cada indice de la lista vertices'''
                if self.vertices[item].get_valor() == valor:
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

def algoritmo_de_dijkstra(grafo):
    '''Algoritmo que encuentra el menor camino a cada nodo
    de un grafo'''
    representaciones = [0]*len(grafo.get_vertices())
    '''Crea una lista dado el número de vertices que tiene el grafo'''
    representaciones = list(map(lambda item: {'costo': 0, 'camino': ""}, representaciones))
    '''Transdorma cada elemento de la lista representaciones a un diccionario. El diccionario
    almacena el costo de llegar a cierto vertice dado el indice que ocupa en la lista y el camino 
    más corto que se sigue'''
    for nodo in range(1,len(grafo.get_vertices())):
        '''Recorre cada inidce de la lista vertices del grafo'''
        nodo_actual = grafo.obtener_nodo(nodo)
        '''Obtiene el nodo actual dado el indice actualmente evaluado'''
        for arista in range(len(nodo_actual.get_aristas())):
            '''Recorre cada indice de la lista aristas del nodo actual y
            evalua cada vertice adyacente del nodo actual'''
            nodo_adyacente = grafo.obtener_nodo(nodo_actual.get_aristas()[arista].obtener_destino())
            '''Obtiene el nodo adyacente dado el indice de la arista actualmente
            evaluado'''
            costo_nodo_actual = representaciones[nodo_actual.get_valor()-1]['costo']
            '''Obtiene el costo del nodo actual, obteniendo el valor del nodo, asi se
            obtiene su lugar el la lista representaciones y obtenemos el valor de la
            key "costo"'''
            costo_nodo_adyacente = nodo_actual.get_aristas()[arista].get_peso()
            '''Obtiene el costo llegar al nodo actual adyacente, obteniendo el nodo de
            la lista arista dado el indice actual de la lista arista para obtener
            el costo de la arista de llegar al nodo adyacente'''
            suma = costo_nodo_actual + costo_nodo_adyacente
            '''Suma el costo del nodo actual y el costo de llegar al nodo actual
            adyacente'''
            if (representaciones[nodo_adyacente.get_valor()-1]['costo'] == 0):
                '''Obtenemos el valor del nodo actual adyacente, para obtener su lugar 
                en la lista representaciones y obtener el costo dado la key "costo". 
                Si el costo es igual a cero, entonces colocamos el valor de la 
                variable suma a la key "costo"'''
                representaciones[nodo_adyacente.get_valor()-1]['costo'] += suma
                '''colocamos el valor de la variable suma a la key "costo"'''
                representaciones[nodo_adyacente.get_valor() - 1]['camino'] += str(f'|{nodo_actual.get_valor()}|')
                '''Obtenemos el valor del nodo actual adyacente, para obtener su lugar 
                en la lista representaciones y obtener el camino menor de llegar a el 
                dado la key "camino".nAñadimos la repersentación del nodo actual y la 
                representación del nodo actual adyacente al camino del nodo actual 
                adyacente'''
                representaciones[nodo_adyacente.get_valor() - 1]['camino'] += str(f'|{nodo_adyacente.get_valor()}|')

            elif(suma <= representaciones[nodo_adyacente.get_valor()-1]['costo']):
                '''Obtenemos el valor del nodo actual adyacente, para obtener su lugar 
                en la lista representaciones y obtener el costo dado la key "costo". 
                Si el costo es mayor al costo obtenido por la variable cuma, entonces 
                colocamos el valor de la variable suma a la key costo"'''
                representaciones[nodo_adyacente.get_valor()-1]['costo'] += suma
                '''colocamos el valor de la variable suma a la key "costo"'''
                representaciones[nodo_adyacente.get_valor() - 1]['camino'] = str(f'|{nodo_actual.get_valor()}|')
                '''Obtenemos el valor del nodo actual adyacente, para obtener su lugar 
                en la lista representaciones y obtener el camino menor de llegar a el 
                dado la key "camino".nAñadimos la repersentación del nodo actual y la 
                representación del nodo actual adyacente al camino del nodo actual 
                adyacente'''
                representaciones[nodo_adyacente.get_valor() - 1]['camino'] += str(f'|{nodo_adyacente.get_valor()}|')
    '''Retorna la lista representaciones, cada indice tendra un diccionario donde tendra el menor
    costo de llegar a ese vertice (cada indice de la lista puede interpretarse como un vertice)
    y el camino más corto para llegar a ese vertice'''
    return representaciones

def main():
    grafo = Grafo()
    grafo.nuevo_nodo(1)
    grafo.nuevo_nodo(2)
    grafo.nuevo_nodo(3)
    grafo.nuevo_nodo(4)
    grafo.nuevo_nodo(5)
    grafo.nuevo_nodo(6)
    grafo.nueva_arista(1, 2, 2)
    grafo.nueva_arista(1, 3, 3)
    grafo.nueva_arista(2, 4, 5)
    grafo.nueva_arista(3, 4, 5)
    grafo.nueva_arista(3, 5, 4)
    grafo.nueva_arista(4, 5, 1)
    grafo.nueva_arista(5,6,8)
    print(algoritmo_de_dijkstra(grafo))
main()