from GrafoADT.Grafo import Grafo
def main():
    grafo = Grafo()
    grafo.nuevo_nodo(1)
    n = grafo.obtener_primer_nodo()
    print(f'OK: {n}')
    grafo.nuevo_nodo(2)
    print(f'Indice de Grafo con valor 2: {grafo.indice_vertice(2)}')
    grafo.nueva_arista(1,2,3)
    grafo.nuevo_nodo(3)
    print(f'Son adyacentes el grafo de valor 1 y el grafo de valor 2: {grafo.son_adyacentes(1,2)}')
    primero = grafo.obtener_primer_nodo()
    print(f'Primer Nodo: {primero.__str__()}')
    ultimo = grafo.obtener_ultimo_nodo()
    print(f'Ultimo Nodo: {ultimo.__str__()}')
    alguno = grafo.obtener_nodo(2)
    print(f'Segundo Nodo: {alguno.__str__()}')
    print(f'Adyacencia de primer nodo: {primero.get_aristas()[0]}')
    print(grafo.__str__())
main()