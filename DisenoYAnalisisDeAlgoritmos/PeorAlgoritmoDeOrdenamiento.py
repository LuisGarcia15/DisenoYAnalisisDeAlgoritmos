import random
'''El costo computacional del algoritmo es 2 elevado a 2 elevado a n ya que
parte de la idea de, dada una probabilidad de 1/2 se decide si se ordena el
elemento actual. Porteriormente dada una probabilidad de 1/2 se decide
si se verifica si la lista esta o no ordenada. Es como si se dieran
todas las posibilidades que existieran al realizar su tabla de verdad.
Es muy similar a BubbleSort'''
def peor_algoritmo_de_ordenamiento(lista):
    '''Algoritmos que se le pasa una lista desordenada'''
    se_ordena = [True, False]
    '''Lista que almacena dos valores, True o False que, dado
    el valor que se elija, permitira verificar si la lista se 
    ah ordenado o si se ordena un elemento'''
    bandera = True
    '''Bandera para terminar el ciclo principal cuando se ah
    verificado que la lista está ordenado'''
    número_iteraciones = 1
    num = 1
    while bandera:
        '''Mientras la bandera sea True, entonces no se ah verificado
        que la lista este ordenada o simplemente no esta ordenada'''
        número_iteraciones += 1
        for item in range(len(lista)):
            num += 1
            '''Recorre todos los indices de la lista
            pasada como parámetro'''
            orden = se_ordena[random.randint(0,1)]
            '''Si, apartir de la lista se_ordena se obtiene
            el valor True, entonces verifica si el elemento
            actual se ordena con respecto a su siguiente elemento.
            Pero si se obtiene False, continua a evaluar el
            siguiente elemento'''
            if orden:
                '''Si orden obtuvo el valor de True, procede
                a evluar si necesita ordenar el elemento actual
                con respecto a su siguiente elemento'''
                if item != (len(lista)-1):
                    '''Si el indice actual es diferente al 
                    ultimo indice lde la lista'''
                    if lista[item] > lista[item+1]:
                        '''Verifica si el elemento actual es
                        mayor al elemento siguiente, si lo es
                        intercambia los elementos de posición'''
                        aux = lista[item+1]
                        lista[item+1] = lista[item]
                        lista[item] = aux
                else:
                    '''Si el indice actual es igual al 
                    ultimo indice lde la lista'''
                    if lista[item] < lista[item-1]:
                        '''Verifica si el elemento actual es
                        menos al elemento anteior pus estas
                        comparando si el último elemento esta
                        en la posición correcta, si lo es
                        intercambia los elementos de posición'''
                        aux = lista[item-1]
                        lista[item-1] = lista[item]
                        lista[item] = aux
        orden = se_ordena[random.randint(0, 1)]
        '''Si orden obtuvo el valor de True, procede
        a evluar si la lista esta o no ordenada. Si orden
        obtiene False, entonces no verifica si la lista
        está o no ordenada y el ciclo no termina aún si la 
        lista ya esta ordenada'''
        if orden:
            '''Si orden obtiene el valor de True verifica
            si la lista está o no ordenada'''
            for item in range(len(lista)):
                '''Recorre todos los indices de la lista
                pasada como parámetro'''
                if item != (len(lista) - 1):
                    '''Si el indice actual es diferente al 
                    ultimo indice lde la lista'''
                    if lista[item] > lista[item+1]:
                        '''Si el elemento actual es mayor al
                        elemento siguiente, entonces la lista
                        no esta ordenada. Mantiene la bandera
                        en True y rompe el ciclo For'''
                        bandera = True
                        break
                    else:
                        '''Si el elemento actual es menor al
                        elemento siguiente, por ahora, la lista
                        esta ordenada hasta el elemento actual.
                        Por lo que la variable bandera cambia su
                        valor a False y continua a evaluar el siguiente
                        elemento'''
                        bandera = False
                else:
                    '''Si el indice actual es igual al 
                    ultimo indice de la lista'''
                    if lista[item] < lista[item-1]:
                        '''Si el elemento actual es menor al
                        elemento anterior, entonces la lista
                        no esta ordenada. Mantiene la bandera
                        en True y rompe el ciclo For'''
                        bandera = True
                        break
                    else:
                        '''Si el elemento actual es mayor al
                        elemento anterior la lista esta ordenada.
                       Por lo que la variable bandera cambia su
                        valor a False y rompera la evaluación de 
                        la cadena'''
                        bandera = False
    print(num)
    print(número_iteraciones)
    return lista
'''Retorna la lista ordenada'''

def main():
    lista = [item for item in range(100000)]
    random.shuffle(lista)
    print(peor_algoritmo_de_ordenamiento(lista))
main()