import numpy as np
class Nodo:
    def __init__(self, cont, hijos):
        self.__contenido = cont
        self.__hijos = hijos

    @property
    def contenido(self):
        return self.__contenido

    @property
    def get_hijos(self):
        return self.__hijos

    @contenido.setter
    def contenido(self, cont):
        self.__contenido = cont

class Arbol:
    def __init__(self, contenido):
        self.__raiz = Nodo(contenido, [])

    @property
    def get_raiz(self):
        return self.__raiz

def colocar_reina(tablero, fila, columna):
    if verificar_columna(tablero, columna) and verificar_fila(tablero, fila) and verificar_diagonal(tablero, fila, columna):
        tablero[fila][columna] = 1
        return True
    else:
        return False

def verificar_fila(tablero, fila):
    for col in range(len(tablero)):
        if tablero[fila][col] != 0:
            return False
    return True

def verificar_columna(tablero, columna):
    for fil in range(len(tablero)):
        if tablero[fil][columna] != 0:
            return False
    return True

def verificar_diagonal(tablero, fila, columna):
    fil_original = fila
    col_original = columna

    fila = fila -1
    columna = columna - 1
    if fila >= 0 and columna >= 0:
        while fila >= 0 and columna >= 0:
            if tablero[fila][columna] != 0:
                return False
            fila = fila - 1
            columna = columna - 1

    fila = fil_original
    columna = col_original
    fila = fila + 1
    columna = columna + 1
    if fila < len(tablero) and columna < len(tablero):
        while fila != len(tablero) and columna != len(tablero):
            if tablero[fila][columna] != 0:
                return False
            fila = fila + 1
            columna = columna + 1

    fila = fil_original
    columna = col_original
    fila = fila + 1
    columna = columna - 1
    if fila < len(tablero) and columna >= 0:
        while fila != len(tablero) and columna >= 0:
            if tablero[fila][columna] != 0:
                return False
            fila = fila + 1
            columna = columna - 1

    fila = fil_original
    columna = col_original
    fila = fila - 1
    columna = columna + 1
    if fila >= 0 and columna < len(tablero):
        while fila >= 0 and columna != len(tablero):
            if tablero[fila][columna] != 0:
                return False
            fila = fila - 1
            columna = columna + 1

    return True

def copiar_tablero(tablero):
    copia_tablero = ([[] * len(tablero)] * len(tablero))
    for copia in range(len(tablero)):
        copia_tablero[copia] = tablero[copia].copy()
    return copia_tablero

def reinas(nodo, num = 0):
    copia_tablero = copiar_tablero(nodo.contenido)
    if num == len(nodo.contenido):
        return nodo.contenido
    else:
        for fila in range(len(nodo.contenido)):
            for columna in range(len(nodo.contenido)):
                nodo.get_hijos.append(Nodo(nodo.contenido, []))
                if colocar_reina(nodo.get_hijos[len(nodo.get_hijos)-1].contenido, fila, columna):
                    num = num + 1
                    backtracking = reinas(nodo.get_hijos[len(nodo.get_hijos)-1], num)
                    if  backtracking == False:
                        nodo.contenido = copia_tablero
                        num = num - 1
                        continue
                    else:
                        return backtracking
        return False

def problema_reinas(longitud_tablero):
    tablero = [[0] * longitud_tablero] * longitud_tablero
    arbol = Arbol(tablero)
    resultado = np.array(reinas(arbol.get_raiz))
    return resultado

def main():
    print(problema_reinas(4))
main()