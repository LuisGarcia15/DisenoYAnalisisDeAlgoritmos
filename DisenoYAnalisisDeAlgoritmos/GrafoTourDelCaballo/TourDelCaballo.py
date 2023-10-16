import numpy as np
from GrafoTourDelCaballo.Grafo import Grafo

def creacion_nodos(tablero, grafo):
    for fila in range(len(tablero)):
        for columna in range(len(tablero)):
            grafo.nuevo_nodo(fila, columna)

def creacion_aristas(tablero, grafo):
    fila_aux = 0
    columna_aux = 0
    for fila in range(len(tablero)):
        for columna in range(len(tablero)):
            nodo = grafo.obtener_nodo(fila, columna)
            if fila - 2 >= 0 and columna - 1 >= 0:
                grafo.nueva_arista(fila, columna, (fila-2), (columna-1))
                nodo.aumentar_num_casillas_adyacentes()
                ########## --
            if fila - 2 >= 0 and columna + 1 < len(tablero):
                grafo.nueva_arista(fila, columna, (fila-2), (columna+1))
                nodo.aumentar_num_casillas_adyacentes()
                ########## --
            if fila - 1 >= 0 and columna + 2 < len(tablero):
                grafo.nueva_arista(fila, columna, (fila-1), (columna+2))
                nodo.aumentar_num_casillas_adyacentes()
                ########## --
            if fila + 1 < len(tablero) and columna + 2 < len(tablero):
                grafo.nueva_arista(fila, columna, (fila+1), (columna+2))
                nodo.aumentar_num_casillas_adyacentes()
                ########## --
            if fila + 2 < len(tablero) and columna + 1 < len(tablero):
                grafo.nueva_arista(fila, columna, (fila+2), (columna+1))
                nodo.aumentar_num_casillas_adyacentes()
                ########## --
            if fila + 2 < len(tablero) and columna - 1 >= 0:
                grafo.nueva_arista(fila, columna, (fila+2), (columna-1))
                nodo.aumentar_num_casillas_adyacentes()
                ##########
            if fila + 1 < len(tablero) and columna - 2 >= 0:
                grafo.nueva_arista(fila, columna, (fila+1), (columna-2))
                nodo.aumentar_num_casillas_adyacentes()
                ##########
            if fila - 1 >= 0 and columna - 2 >= 0:
                grafo.nueva_arista(fila, columna, (fila-1), (columna-2))
                nodo.aumentar_num_casillas_adyacentes()
def movimento_caballo(tablero,x,y):
    coordenada_x = x
    coordenada_y = y
    coordenada_x_aux = -1
    coordenada_y_aux = -1
    movimiento_caballo = 1
    grafo = Grafo()
    creacion_nodos(tablero, grafo)
    creacion_aristas(tablero, grafo)
    costo_casilla = 0
    for item in range(64):
        nodo_actual = grafo.obtener_nodo(coordenada_x, coordenada_y)
        tablero[coordenada_x][coordenada_y] = movimiento_caballo
        movimiento_caballo += 1
        nodo_actual.set_fue_visitado(True)
        for arista in range(len(nodo_actual.get_aristas())):
            nodo_adyacente_actual = nodo_actual.get_aristas()[arista].obtener_destino()
            nodo_adyacente_actual.disminuir_num_casillas_adyacentes()
            if costo_casilla == 0 and nodo_adyacente_actual.get_fue_visitado() != True:
                costo_casilla = nodo_adyacente_actual.get_num_casillas_adyacentes()
                coordenada_x_aux = nodo_adyacente_actual.get_coordenada_x()
                coordenada_y_aux = nodo_adyacente_actual.get_coordenada_y()
            else:
                if nodo_adyacente_actual.get_num_casillas_adyacentes() <= costo_casilla\
                        and nodo_adyacente_actual.get_fue_visitado() != True:
                    costo_casilla = nodo_adyacente_actual.get_num_casillas_adyacentes()
                    coordenada_x_aux = nodo_adyacente_actual.get_coordenada_x()
                    coordenada_y_aux = nodo_adyacente_actual.get_coordenada_y()
        coordenada_x = coordenada_x_aux
        coordenada_y = coordenada_y_aux
        costo_casilla = 0
    return grafo, tablero

def main():
    tablero = np.array([[0]*(8)]*(8))
    grafo, tablero = movimento_caballo(tablero, 4, 4)
    print(tablero)
main()