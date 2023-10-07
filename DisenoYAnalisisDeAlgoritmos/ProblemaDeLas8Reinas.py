import numpy as np
class Nodo:
    def __init__(self, contenido, hijos):
        self.__contenido = contenido
        self.__hijos = hijos

    @property
    def get_contenido(self):
        return self.__contenido

    @property
    def get_hijos(self):
        return self.__hijos

class Arbol:
    def __init__(self, contenido):
        self.__raiz = Nodo(contenido, [])

    @property
    def get_raiz(self):
        return self.__raiz
def reinas(tablero, num):
    copia_tablero = copiar_tablero(tablero)
    if num == len(tablero):
        return tablero
    else:
        for fila in range(len(tablero)):
            for columna in range(len(tablero)):
                if colocar_reina(tablero, fila, columna):
                    num = num + 1
                    backtracking = reinas(tablero, num)
                    if  backtracking == False:
                        tablero = copia_tablero
                        num = num - 1
                        continue
                    else:
                        return backtracking
        return False

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

def main():
    num = 9
    tablero = [
        [0]*num
    ]* num
    l = np.array(reinas(tablero,0))
    print(l)
main()
