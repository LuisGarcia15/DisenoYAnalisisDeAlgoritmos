def problema_de_las_bolsas(lista_pesos, peso_de_bolsas):
    bolsas = [[]]
    '''Lista que tendra la mejor configuración y donde se
    agregaran los elementos'''
    bolsa = 0
    '''Indice que permitira apuntar a las bolsas'''
    while True:
        '''Ciclo que solo puede cerrarse por un break'''
        if (sum(bolsas[bolsa]) + lista_pesos[0]) <= peso_de_bolsas:
            '''Evalua si la suma de los pesos de la bolsa más el peso a verificar
            es menor al peso de las bolsas'''
            bolsas[bolsa].append(lista_pesos[0])
            '''Agrega el peso a la bolsa correspondiente y donde se puede almacenar'''
            lista_pesos.remove(lista_pesos[0])
            '''Elimina el peso que se ingreso a la bolsa de la lista de pesos'''
            bolsa = 0
            '''Permite volver a verificar el ingreso de pesos desde la primer bolsa'''
            if len(lista_pesos) == 0:
                '''Verifica si la lista de pesos es vacia, si lo es, rompe el ciclo'''
                break
        elif bolsas[len(bolsas)-1] == bolsas[bolsa]:
            '''Verifica si la bolsa a la que se apunta es la última'''
            bolsas.append([])
            '''Si es la última, agrega una bolsa nueva y vacia'''
            bolsas[len(bolsas)-1].append(lista_pesos[0])
            '''Agrega el peso correspondiente a la ultima bolsa, pues ya se verifico que 
            no se pudo agregar a una anterior y este if peermite ingresar un elemento a una
            nueva bolsa, siendo esa bolsa la última'''
            lista_pesos.remove(lista_pesos[0])
            '''Elimina el peso que se ingreso a la bolsa de la lista de pesos'''
            bolsa = 0
            '''Permite volver a verificar el ingreso de pesos desde la primer bolsa'''
            if len(lista_pesos) == 0:
                '''Verifica si la lista de pesos es vacia, si lo es, rompe el ciclo'''
                break
        else:
            '''Si ninguna de las anteriores verificaciones se cumple, simplemente se aumenta
            el apuntador de las bolsas para verificar si en la siguiente bolsa es posible
            almacenar un articulo'''
            bolsa += 1
    return bolsas
    '''Retorna la mejor configuración dada una lista de pesos y un peso limite para cada bolsa'''

def main():
        listaPesos = [6,5,5,4,3,3,3,3,3,2,2,1,1,1,1]
        peso_de_bolsa = 7
        print(problema_de_las_bolsas(listaPesos, peso_de_bolsa))

main()