import numpy as np
def mochila(pesos, beneficios, peso_maximo):
    table = np.array([[0]*(peso_maximo+1)]*(len(pesos)+1))#primero van filas luego columnas
    for peso_actual in range(1,len(pesos)+1):
        for mochila_actual in range(1, peso_maximo+1):

            if pesos[peso_actual-1] <= mochila_actual:
                '''Verifica si el peso actual es menor o igual al peso de a mochila actual'''
                if pesos[peso_actual-1] < mochila_actual:
                    '''Si el peso actua es menor al peso de la mochila actual'''
                    resta = mochila_actual - pesos[peso_actual-1]
                    '''restamos el peso de la mochila actual menos el peso del objeto actual, eso
                    nos dará el indice de la columna con el objeto de peso mayor que aun cabe en 
                la casilla actual'''
                    if table[peso_actual-1][resta] + beneficios[peso_actual-1] > table[peso_actual-1][mochila_actual]:
                        '''Si el beneficio del elemento con el peso mayor que aun cabe en la casilla actual más
                        el beneficio del elemento actual es mayor al beneficio del elemento anterior que entro en
                        la mochila con el peso actual'''
                        table[peso_actual][mochila_actual] = table[peso_actual - 1][resta] + beneficios[peso_actual - 1]
                        '''Colocamos en la casilla actual la suma del beneficio del elemento con el peso mayor que 
                        aun cabe en la casilla actual más el beneficio del elemento actual'''
                    else:
                        '''Si el beneficio del elemento con el peso mayor que aun cabe en la casilla actual más
                        el beneficio del elemento actual es menor al beneficio del elemento anterior que entro en
                        la mochila con el peso actual'''
                        table[peso_actual][mochila_actual] = table[peso_actual-1][mochila_actual]
                        '''Colocamos en la casilla actual el benedicio del elemento anterior que entro en la mochila
                        con el peso actual, pues es el beneficio mayor que ha entrado hasta el momento en esa
                        mochila con capacidad n'''
                elif pesos[peso_actual-1] == mochila_actual:
                    '''Si el peso actual no es menor al peso de la mochila actual y por el contrario,
                    es igual, entonces colocamos en la casilla actual el beneficio del objeto actual'''
                    table[peso_actual][mochila_actual] = beneficios[peso_actual-1]
            else:
                '''Si el peso actual no es menor o igual al peso de la mochila actual,
                entonces tomamos el beneficio del peso anterior en el peso de la mochila
                actual y colocamos ese beneficio en la casilla actual, ya que el anterior
                debe haber entrado'''
                table[peso_actual][mochila_actual] = table[peso_actual-1][mochila_actual]
    return table[peso_actual][mochila_actual]


def main():
    listaPesos = [1,1,8,7,7,11,10]
    listaBeneficios = [3,3,4,2,2,8,7]
    peso = 20
    print(mochila(listaPesos, listaBeneficios, peso))
main()