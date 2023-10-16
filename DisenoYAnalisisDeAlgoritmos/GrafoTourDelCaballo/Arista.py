class Arista:

    def __init__(self, nodo_destino):
        '''Clase Arista que sera la arista de
        un nodo. Recibe como parámetro
        el peso de la arista y el nodo destino'''
        self.nodo_destino = nodo_destino

    def obtener_destino(self):
        '''Obtiene el destino de la arista'''
        return self.nodo_destino

    def __str__(self):
        '''to string de la arista: representación de la arista'''
        return f'Destino: [{self.nodo_destino}]'