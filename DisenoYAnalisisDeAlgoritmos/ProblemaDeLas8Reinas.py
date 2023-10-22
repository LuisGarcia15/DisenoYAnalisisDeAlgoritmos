import numpy as np
class Nodo:
    def __init__(self, cont, hijos):
        '''Constructor del objeto nodo, acepta el contenido que
        tendra el nodo y una lista. esa lista son los nodos que
        se bifurcan a apartir del nodo principal'''
        self.__contenido = cont
        self.__hijos = hijos

    @property
    def contenido(self):
        '''Get de la variable contenido'''
        return self.__contenido

    @property
    def get_hijos(self):
        '''get la lista de nodos'''
        return self.__hijos

    @contenido.setter
    def contenido(self, cont):
        '''set del contenido del nodo'''
        self.__contenido = cont

class Arbol:
    def __init__(self, contenido):
        '''Constructor de la estructura de datos árbol, recibe
        como parámetro el contenido que tendrá el nodo raíz
        del arbol'''
        self.__raiz = Nodo(contenido, [])

    @property
    def get_raiz(self):
        '''Get del nodo raiz'''
        return self.__raiz

def colocar_reina(tablero, fila, columna):
    '''Método para verificar la fila, columnas y diagonales de una reina
    y saber si es posible colocarla en una casilla dada'''
    if verificar_columna(tablero, columna) and verificar_fila(tablero, fila) and verificar_diagonal(tablero, fila, columna):
        '''Si todas las evaluaciones retorna true, entonces es posible
        colocar una reina. por lo que colocar un 1 en la casilla actual y retornas True'''
        tablero[fila][columna] = 1
        return True
    else:
        '''Si alguna de la evaluaciones retorna False, entonces existe en 
        alguna casilla una reina que afecta a la actual, por lo que no coloca
        una reina y retorna False'''
        return False

def verificar_fila(tablero, fila):
    '''Método para verificar la fila de una reina
    y saber si es posible colocarla en una casilla dada'''
    for col in range(len(tablero)):
        '''Verifica la fila donde se encuentra la
        reina y si encuentra una casilla donde su
        elemento es diferente de cero, entonces no
        es posible colocar una reina'''
        if tablero[fila][col] != 0:
            return False
    '''Si termina la evaluacion sin retornar false, significa
    que no hay reinas que afecten a la actual casilla y retorna true'''
    return True

def verificar_columna(tablero, columna):
    '''Método para verificar la columna de una reina
    y saber si es posible colocarla en una casilla dada'''
    for fil in range(len(tablero)):
        '''Verifica la columna donde se encuentra la
        reina y si encuentra una casilla donde su
        elemento es diferente de cero, entonces no
        es posible colocar una reina'''
        if tablero[fil][columna] != 0:
            return False
    '''Si termina la evaluacion sin retornar false, significa
    que no hay reinas que afecten a la actual casilla y retorna true'''
    return True

def verificar_diagonal(tablero, fila, columna):
    '''Método para verificar las diagonales de una reina
    y saber si es posible colocarla en una casilla dada'''
    fil_original = fila
    '''Variables para guardar las coordenadas de la casilla
    actual evaluada'''
    col_original = columna

    '''Evaluamos cuando (x-1, x-1)'''
    fila = fila -1
    columna = columna - 1
    '''Si la fila y la columna es mayor o igual a cero, significa
    que esta dentro de las coordenadas de la matriz'''
    if fila >= 0 and columna >= 0:
        while fila >= 0 and columna >= 0:
            if tablero[fila][columna] != 0:
                '''For para verificar la diagonal cuando 
                (x-1, x-1) y si es diferente de cero
                entonces no es posible colocar la reina 
                en la casilla evaluada'''
                return False
            fila = fila - 1
            '''Resta la unidad a las filas y columnas para seguir
            evaluando la diagonal'''
            columna = columna - 1

    '''Restauramos las coordenadas originales'''
    fila = fil_original
    columna = col_original
    '''Evaluamos cuando (x+1, y+1)'''
    fila = fila + 1
    columna = columna + 1
    '''Si la fila es menor a la longitud del tablero 
    y la columna es menor a la longitud del tablero, significa
    que esta dentro de las coordenadas de la matriz'''
    if fila < len(tablero) and columna < len(tablero):
        while fila != len(tablero) and columna != len(tablero):
            if tablero[fila][columna] != 0:
                '''For para verificar la diagonal cuando 
                (x+1, y+1) y si es diferente de cero
                entonces no es posible colocar la reina 
                en la casilla evaluada'''
                return False
            fila = fila + 1
            '''Suma la unidad a las filas y columnas para seguir
            evaluando la diagonal'''
            columna = columna + 1

    '''Restauramos las coordenadas originales'''
    fila = fil_original
    columna = col_original
    '''Evaluamos cuando (x+1, y-1)'''
    fila = fila + 1
    columna = columna - 1
    '''Si la fila es menor a la longitud del tablero 
    y la columna es mayor o igual a cero, significa
    que esta dentro de las coordenadas de la matriz'''
    if fila < len(tablero) and columna >= 0:
        while fila != len(tablero) and columna >= 0:
            if tablero[fila][columna] != 0:
                '''For para verificar la diagonal cuando 
                (x+1, y-1) y si es diferente de cero
                entonces no es posible colocar la reina 
                en la casilla evaluada'''
                return False
            fila = fila + 1
            '''Suma la unidad a las filas resta la unidad a 
            la columnas para seguir evaluando la diagonal'''
            columna = columna - 1

    '''Restauramos las coordenadas originales'''
    fila = fil_original
    columna = col_original
    '''Evaluamos cuando (x-1, y+1)'''
    fila = fila - 1
    columna = columna + 1
    '''Si la fila es mayot o igual a cero  y la columna 
    es menor a la longitud del tablero, significa que 
    esta dentro de las coordenadas de la matriz'''
    if fila >= 0 and columna < len(tablero):
        while fila >= 0 and columna != len(tablero):
            if tablero[fila][columna] != 0:
                '''For para verificar la diagonal cuando 
                (x+1, y-1) y si es diferente de cero
                entonces no es posible colocar la reina 
                en la casilla evaluada'''
                return False
            fila = fila - 1
            '''Suma la unidad a las filas resta la unidad a 
            la columnas para seguir evaluando la diagonal'''
            columna = columna + 1
    '''Si termina todas la evaluaciones sin retornar false, significa
    que no hay reinas que afecten a la actual casilla y retorna true'''
    return True

def copiar_tablero(tablero):
    '''Método para copiar el tablero'''
    copia_tablero = ([[] * len(tablero)] * len(tablero))
    '''Crea una matriz del mismo tamaño que el tablero
    pasado como parámetro'''
    for copia in range(len(tablero)):
        '''For para copiar cada fila de la variable
        tablero a la variable copia_tablero'''
        copia_tablero[copia] = tablero[copia].copy()
        '''Retorna la copia de tablero'''
    return copia_tablero

def reinas(nodo, num = 0):
    '''Método recursivo para colocar las reinas y retornar
    el tablero con las fichas en la posición correcta'''
    copia_tablero = copiar_tablero(nodo.contenido)
    '''Copia el tablero a una variable auxiliar llamada
    copia_tablero'''
    if num == len(nodo.contenido):
        '''Caso base: si la variable num es igual al número
        de filas del tablero, retorna el tablero correcto'''
        return nodo.contenido
    else:
        '''Caso recursivo'''
        for fila in range(len(nodo.contenido)):
            for columna in range(len(nodo.contenido)):
                '''For para recorrer cada casilla del tablero'''
                nodo.get_hijos.append(Nodo(nodo.contenido, []))
                '''Agrega un nodo hijo al nodo actual'''
                if colocar_reina(nodo.get_hijos[len(nodo.get_hijos)-1].contenido, fila, columna):
                    '''Si es posible colocar una reina en la actual casilla del tablero
                    evaluada por los for'''
                    num = num + 1
                    '''Se aumenta el valor de num en la unidad, pues se coloco de manera exitosa
                    una reina'''
                    backtracking = reinas(nodo.get_hijos[len(nodo.get_hijos)-1], num)
                    '''Recursión para saber si, de la bifurcación actual, fue posible
                    obtener la disposición correcta de reinas'''
                    if  backtracking == False:
                        '''si la variable backtracking es False, entonces significa
                        que se revisaron todos las casillas y no se encontro la
                        disposición correcta'''
                        nodo.contenido = copia_tablero
                        '''copiamos al nodo del nivel anterior, el tablero antes de
                        colocar una reina'''
                        num = num - 1
                        '''restamos la variable num ya que no fue posible colocar
                        una reina'''
                        continue
                        '''continuamos con una iteración'''
                    else:
                        '''Si la variable backtracking es diferente de false, quiere decir que 
                        encontro la configuración correcta de reinas en el tablero, por lo
                        que retorna el tablero correcto'''
                        return backtracking
        return False
    '''Si recorre todas las casillas y no encuentra la disposición correcta de reinas, retorna
    False'''

def problema_reinas(longitud_tablero):
    '''Método que resuelve el problema de las reinas, recibe como
    parámetro la longitud del tablero para construir un tablero nxn'''
    tablero = [[0] * longitud_tablero] * longitud_tablero
    '''Construye un tablero n x n apartir de la logitud del tablero'''
    arbol = Arbol(tablero)
    '''Crea la estructura arbol y se le pasa el tablero como contenido'''
    resultado = np.array(reinas(arbol.get_raiz))
    '''Llama al método reinas y retorna el resultado y se convierte en
    una matriz por numpy'''
    return resultado
'''Retorna el tablero con la solución'''

def main():
    '''El algoritmo funciona para un tablero 4x4, 5x5, 6x6
    7x7 y 9x9. Sin embargo, no funciona para un tablero 8x8'''
    print(problema_reinas(9))
main()