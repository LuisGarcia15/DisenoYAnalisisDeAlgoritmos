import numpy as np
class Nodo:

    def __init__(self, x, y):
        '''Clase Nodo que sera el vertice de
        un grafo. Recibe como parámetro
        la coordenada que almacena el grafo'''
        self.__coordenada_x = x
        '''Variable que almacena la coordenada x'''
        self.__coordenada_y = y
        '''Variable que almacena la coordenada x'''
        self.__fue_visitado = False
        '''Variable que indica si el nodo ya fue
        visitado'''
        self.__grado_nodo = 0
        '''variable que almacena el grado del nodo,
        osea, el número de conecciones entre este 
        y otros n nodos'''
        self.__num_vertice = -1
        '''Tendra una variable num:vertice que sera
        el número de vertice del nodo'''
        self.__aristas = []
        '''Tendra una lista con las aristas asi donde
        se conecta el nodo'''

    def get_coordenada_x(self):
        '''get de la coordenada x'''
        return self.__coordenada_x

    def get_coordenada_y(self):
        '''get de la coordenada y'''
        return self.__coordenada_y

    def get_fue_visitado(self):
        '''get de la variable valor'''
        return self.__fue_visitado

    def get_aristas(self):
        '''get de la variable aristas'''
        return self.__aristas

    def get_grado_nodo(self):
        '''get de la get_nodo'''
        return self.__grado_nodo

    def set_coordenada_x(self, x):
        '''set de la coordenada x'''
        self.__coordenada_x = x

    def set_coordenada_y(self, y):
        '''set de la coordenada y'''
        self.__coordenada_y = y

    def set_fue_visitado(self, valor):
        '''set de la variable fue_visitado'''
        self.__fue_visitado = valor

    def aumentar_grado_nodo(self):
        '''método para aumentar el grado
        del nodo'''
        self.__grado_nodo += 1

    def disminuir_grado_nodo(self):
        '''método para disminuir el grado
        del nodo'''
        self.__grado_nodo -= 1

    def asignar_vertice(self, num_vertice):
        '''añade el numero de vertice al vertice'''
        self.num_vertice = num_vertice

    def __str__(self):
        '''to string del nodo: representación del nodo'''
        return f'Valor: {self.__valor} - Número De Vertice: {self.num_vertice}'

class Arista:

    def __init__(self, nodo_destino):
        '''Clase Arista que sera la arista de
        un nodo. Recibe como parámetro
        el nodo destino'''
        self.nodo_destino = nodo_destino

    def obtener_destino(self):
        '''Obtiene el destino de la arista'''
        return self.nodo_destino

    def __str__(self):
        '''to string de la arista: representación de la arista'''
        return f'Destino: [{self.nodo_destino}]'

class Grafo:

    num_max_vertices = 0
    '''Variable de clase que almacena el número
    máximo de vertices'''

    def __init__(self, num_vertices):
        '''Clase Grafo que sera la estructura
        de nodos conectados.'''
        self.num_max_vertices = num_vertices
        '''Variable para crear el número de vertices
        pasado como parámetro'''
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
        '''Crea un nodo con laas coordenadas pasadas como parámetro'''
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
        la coordenada pasado como parámetro'''
        for item in range(len(self.vertices)):
            '''Recorre cada indice de la lista vertices'''
            if x == self.vertices[item].get_coordenada_x() \
                    and y == self.vertices[item].get_coordenada_y():
                '''Si la coordenada es igual al nodo dado 
                el indice actual de la lista vertices, 
                retorna el indice'''
                return item
        '''Si no retorna -1, dado que no existe el nodo
        con el valor dado como parámetro'''
        return -1

    def nueva_arista(self, coordenada_x_uno, coordenada_y_uno,
                     coordenada_x_dos, coordenada_y_dos):
        '''Crea una nueva arista dado la coordenada de un nodo y la
        coordenada de otro nodo'''
        indice_nodo_uno = self.indice_vertice(coordenada_x_uno, coordenada_y_uno)
        '''Busca el indice del nodo dado los primeros valores x,y pasados 
        como parámetros y lo almacena en una variable'''
        indice_nodo_dos = self.indice_vertice(coordenada_x_dos, coordenada_y_dos)
        '''Busca el indice del nodo dado los segundos valores x, y  pasado 
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
            '''Obtenemos el nodo dado los primeros valores x,y pasados
            como parámetro y lo almacenamos en una variable'''
            nodo_dos = self.obtener_nodo(coordenada_x_dos, coordenada_y_dos)
            '''Obtenemos el nodo dado los segundos valores x,y pasados
            como parámetro y lo almacenamos en una variable'''
            nodo_uno.get_aristas().append(Arista(nodo_dos))
            '''Añadimos la arista al primer nodo, añadiendo la
            coneccion entre vertices a su lista de aristas, pasando 
            como nodo de destino el segundo nodo'''
            self.matriz_adyacencia[indice_nodo_uno][indice_nodo_dos] = 1
            '''Colocamos en la matriz de adyacencia dado la coordenada
            (indice_nodo_uno, indice_nodo_dos), el peso de la arista
            creada anteriormente'''



    def son_adyacentes(self, coordenada_x_uno, coordenada_y_uno,
                     coordenada_x_dos, coordenada_y_dos):
        '''Verifica si dos nodos son adyacentes dado las coordenadas de
        dos nodos pasado como parámetro'''
        indice_nodo_uno = self.indice_vertice(coordenada_x_uno, coordenada_y_uno)
        '''Busca el indice del nodo dado los primeros valores x,y pasados 
        como parámetro y lo almacena en una variable'''
        indice_nodo_dos = self.indice_vertice(coordenada_x_dos, coordenada_y_dos)
        '''Busca el indice del nodo dado los segundos valores x,y pasados  
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
        es diferente de 0, entonces los dos nodos son adyacentes'''
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
        la coordenada pasada como parámetro'''
        if len(self.vertices) != 0:
            '''Si la longitud de la lista vertices
            es diferente de cero, entonces existe 
            al menor un vertice'''
            for item in range(len(self.vertices)):
                '''Recorre cada indice de la lista vertices'''
                if x == self.vertices[item].get_coordenada_x() \
                    and y == self.vertices[item].get_coordenada_y():
                    '''Del nodo en el indice actual en la lista
                    verices obtenemos su coordenada x,y y si ese valor
                    es igual al valor de la coordenada x,y pasadas como 
                    parámetro,retornamos el nodo actual'''
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
        '''to string del grafo: representación del grafo dad
        la matriz de adyacencia'''
        return self.matriz_adyacencia

def creacion_nodos(tablero, grafo):
    '''Método para crear la misma cantidad de nodos
    que de casillas en el tablero'''
    for fila in range(len(tablero)):
        for columna in range(len(tablero)):
            '''Cada iteración, crea un nuevo nodo con
            las coordenadas de la casilla actual'''
            grafo.nuevo_nodo(fila, columna)

def creacion_aristas(tablero, grafo):
    '''Método para crear las conecciones (aristas)
    entre nodos dependiendo de los moviminetos
    de una pieza de caballo del ajedrez ajedrez'''
    fila_aux = 0
    '''Variables para almacenar las filas y columnas
    dependiendo de los 8 posibles movimientos de un
    caballo en el ajedrez'''
    columna_aux = 0
    for fila in range(len(tablero)):
        for columna in range(len(tablero)):
            '''Recorre cada casilla del ajedrez'''
            nodo = grafo.obtener_nodo(fila, columna)
            '''Obtiene el vertice dado las coordenadas pasadas
            como parámetro'''
            if fila - 2 >= 0 and columna - 1 >= 0:
                '''Evalua el movimiento (x-2,y-1)'''
                grafo.nueva_arista(fila, columna, (fila-2), (columna-1))
                '''Si la coordenada (x-2,y-1) es alcanzable dentro del
                vertice actual, crea la arista del nodo actual al nodo
                con coordenada (x-2,y-1)'''
                nodo.aumentar_grado_nodo()
                '''Aumenta en la unidad el grado del nodo'''
                ########## --
            if fila - 2 >= 0 and columna + 1 < len(tablero):
                '''Evalua el movimiento (x-2,y+1)'''
                grafo.nueva_arista(fila, columna, (fila-2), (columna+1))
                '''Si la coordenada (x-2,y+1) es alcanzable dentro del
                vertice actual, crea la arista del nodo actual al nodo
                con coordenada (x-2,y+1)'''
                nodo.aumentar_grado_nodo()
                '''Aumenta en la unidad el grado del nodo'''
                ########## --
            if fila - 1 >= 0 and columna + 2 < len(tablero):
                '''Evalua el movimiento (x-1,y+2)'''
                grafo.nueva_arista(fila, columna, (fila-1), (columna+2))
                '''Si la coordenada (x-1,y+2) es alcanzable dentro del
                vertice actual, crea la arista del nodo actual al nodo
                con coordenada (x-1,y+2)'''
                nodo.aumentar_grado_nodo()
                '''Aumenta en la unidad el grado del nodo'''
                ########## --
            if fila + 1 < len(tablero) and columna + 2 < len(tablero):
                '''Evalua el movimiento (x+1,y+2)'''
                grafo.nueva_arista(fila, columna, (fila+1), (columna+2))
                '''Si la coordenada (x+1,y+2) es alcanzable dentro del
                vertice actual, crea la arista del nodo actual al nodo
                con coordenada (x+1,y+2)'''
                nodo.aumentar_grado_nodo()
                '''Aumenta en la unidad el grado del nodo'''
                ########## --
            if fila + 2 < len(tablero) and columna + 1 < len(tablero):
                '''Evalua el movimiento (x+2,y+1)'''
                grafo.nueva_arista(fila, columna, (fila+2), (columna+1))
                '''Si la coordenada (x+2,y+1) es alcanzable dentro del
                vertice actual, crea la arista del nodo actual al nodo
                con coordenada (x+2,y+1)'''
                nodo.aumentar_grado_nodo()
                '''Aumenta en la unidad el grado del nodo'''
                ########## --
            if fila + 2 < len(tablero) and columna - 1 >= 0:
                '''Evalua el movimiento (x+2,y-1)'''
                grafo.nueva_arista(fila, columna, (fila+2), (columna-1))
                '''Si la coordenada (x+2,y-1) es alcanzable dentro del
                vertice actual, crea la arista del nodo actual al nodo
                con coordenada (x+2,y-1)'''
                nodo.aumentar_grado_nodo()
                '''Aumenta en la unidad el grado del nodo'''
                ##########
            if fila + 1 < len(tablero) and columna - 2 >= 0:
                '''Evalua el movimiento (x+1,y-2)'''
                grafo.nueva_arista(fila, columna, (fila+1), (columna-2))
                '''Si la coordenada (x+1,y-2) es alcanzable dentro del
                vertice actual, crea la arista del nodo actual al nodo
                con coordenada (x+1,y-2)'''
                nodo.aumentar_grado_nodo()
                '''Aumenta en la unidad el grado del nodo'''
                ##########
            if fila - 1 >= 0 and columna - 2 >= 0:
                '''Evalua el movimiento (x-1,y-2)'''
                grafo.nueva_arista(fila, columna, (fila-1), (columna-2))
                '''Si la coordenada (x-1,y-2) es alcanzable dentro del
                vertice actual, crea la arista del nodo actual al nodo
                con coordenada (x-1,y-2)'''
                nodo.aumentar_grado_nodo()
                '''Aumenta en la unidad el grado del nodo'''
def movimento_caballo(tablero,x,y):
    '''Método que se encarga de moverse entre el tablero
    como lo haria una pieza de caballo del ajedrex'''
    coordenada_x = x
    '''Variables que almacenan las coordenadas x,y pasadas
    como parámetro'''
    coordenada_y = y
    coordenada_x_aux = -1
    '''Variables que almacenaran coordenadas x,y auxiliares
    a lo largo del problema'''
    coordenada_y_aux = -1
    movimiento_caballo = 1
    '''Variable que lleva el contedo de movimientos del caballo'''
    grafo = Grafo(len(tablero)*len(tablero))
    '''Estructura de datos para movernos a lo largo del tablero. crear el
    número de vertices que se le pasa como parámetro, en este caso, la
    misma cantidad de casillas que hay en el tablero'''
    creacion_nodos(tablero, grafo)
    '''Crea el número de vertices dependiendo del número de casillas'''
    creacion_aristas(tablero, grafo)
    '''crea el grado de cada vertice, dependiendo las casillas
    adyacentes que tenga cada nodo respecto a sus coordenadas
    que almacena'''
    costo_casilla = 0
    '''Variable que nos servirá para comparar el grado de cada nodo
    adyacente al nodo que se este evaluando'''
    for item in range(len(tablero)*len(tablero)):
        '''Ciclo para recorrer cada casilla del tablero'''
        nodo_actual = grafo.obtener_nodo(coordenada_x, coordenada_y)
        '''Obtiene el nodo actual dado la coordenada pasada como parámetro'''
        tablero[coordenada_x][coordenada_y] = movimiento_caballo
        '''Al tablero, en la coordenada actual, se pinta con
        el número de movimiento del caballo'''
        movimiento_caballo += 1
        '''Aumenta el número del movimiento del caballo'''
        nodo_actual.set_fue_visitado(True)
        '''Marca como visitado el noco actual'''
        for arista in range(len(nodo_actual.get_aristas())):
            '''Recorre cada nodo adyacente del nodo actual'''
            nodo_adyacente_actual = nodo_actual.get_aristas()[arista].obtener_destino()
            '''Guarda el nodo adycente evaluado actualmente'''
            nodo_adyacente_actual.disminuir_grado_nodo()
            '''Diminuye el grado del nodo adyacente actual'''
            if costo_casilla == 0 and nodo_adyacente_actual.get_fue_visitado() != True:
                '''si la variable costo_casilla es cero y el nodo adyacente actual no
                ha sido visitado'''
                costo_casilla = nodo_adyacente_actual.get_grado_nodo()
                '''Almacena el grado actual del nodo adyacente, para comparar
                si existe otro nodo con grado menor'''
                coordenada_x_aux = nodo_adyacente_actual.get_coordenada_x()
                '''Almacena la coordenada x,y del nodo adyacente actual en
                las variables de coordenada auxiliares'''
                coordenada_y_aux = nodo_adyacente_actual.get_coordenada_y()
            else:
                if nodo_adyacente_actual.get_grado_nodo() <= costo_casilla\
                        and nodo_adyacente_actual.get_fue_visitado() != True:
                    '''Sino, si el grado del nodo adyacente actual es menor al
                    costo_casilla almacenado actualmente y el nodo adyacente
                    actual no ha sido visitado'''
                    costo_casilla = nodo_adyacente_actual.get_grado_nodo()
                    '''Almacena el grado actual del nodo adyacente, para comparar
                    si existe otro nodo con grado menor'''
                    coordenada_x_aux = nodo_adyacente_actual.get_coordenada_x()
                    '''Almacena la coordenada x,y del nodo adyacente actual en
                    las variables de coordenada auxiliares'''
                    coordenada_y_aux = nodo_adyacente_actual.get_coordenada_y()
        coordenada_x = coordenada_x_aux
        '''Guarda las coordenadas de las variables auxiliares a las variables
        de coordenada para encontrar el proximo nodo y pueda desplzarse a otra
        casilla el caballo'''
        coordenada_y = coordenada_y_aux
        costo_casilla = 0
        '''cambiamos el valor de costo casilla a cero para, una vez se necesite
        comparar de nuevo los nodos adyacentes, inicie desde cero'''
    return grafo, tablero
'''retorna el grafo y el tablero con la solución'''

def main():
    num = 5
    tablero = np.array([[0]*(num)]*(num))
    grafo, tablero = movimento_caballo(tablero, 0, 0)
    print(tablero)
main()