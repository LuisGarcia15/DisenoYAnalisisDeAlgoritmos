import numpy as np
from GrafoADT.Grafo import Grafo
def algoritmo_de_dijkstra(grafo):
    representaciones = [0]*len(grafo.get_vertices())
    representaciones = list(map(lambda item: {'costo': 0, 'camino': ""}, representaciones))
    for nodo in range(1,len(grafo.get_vertices())):
        nodo_actual = grafo.obtener_nodo(nodo)
        for arista in range(len(nodo_actual.get_aristas())):
            nodo_adyacente = grafo.obtener_nodo(nodo_actual.get_aristas()[arista].obtener_destino())
            costo_nodo_actual = representaciones[nodo_actual.get_valor()-1]['costo']
            costo_nodo_adyacente = nodo_actual.get_aristas()[arista].get_peso()
            suma = costo_nodo_actual + costo_nodo_adyacente
            if (representaciones[nodo_adyacente.get_valor()-1]['costo'] == 0):
                representaciones[nodo_adyacente.get_valor()-1]['costo'] += suma
                representaciones[nodo_adyacente.get_valor() - 1]['camino'] += str(f'|{nodo_actual.get_valor()}|')
                representaciones[nodo_adyacente.get_valor() - 1]['camino'] += str(f'|{nodo_adyacente.get_valor()}|')

            elif(suma <= representaciones[nodo_adyacente.get_valor()-1]['costo']):
                representaciones[nodo_adyacente.get_valor()-1]['costo'] += suma
                representaciones[nodo_adyacente.get_valor() - 1]['camino'] += str(f'|{nodo_actual.get_valor()}|')
                representaciones[nodo_adyacente.get_valor() - 1]['camino'] += str(f'|{nodo_adyacente.get_valor()}|')
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