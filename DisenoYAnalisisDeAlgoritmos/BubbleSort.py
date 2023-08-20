'''Algoritmo de ordenamiento burbuja, capaz de ordenar de menor
a mayor una lista, alejando en cada iteración los números mayores
al final de la lista. Su costo computaciones es de O(t'2)'''
def bubblesort(list):
    for length in range(0,len(list)): #Encargado de recorrer toda la lista
        for item in range(0, len(list)-1):
            '''Encargado de recorrer desde el indice
            cero hasta el indice (longitud-1)'''
            if list[item + 1] < list[item]:
                aux = list[item + 1]
                list[item + 1] = list[item]
                list[item] = aux
    return list


def main():
    list = [9, 4, 7, 66, 54, 23, 87, 23, 12]
    print(f'Lista Original: {list}')
    print(f'Lista ordenada por BubbleSort: {bubblesort(list)}')
    try_list = [3,2,1]
    print(try_list)
    print(bubblesort(try_list))
main()
