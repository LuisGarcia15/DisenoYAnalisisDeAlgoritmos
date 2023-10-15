import numpy as np
from GrafoADT.Grafo import Grafo
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