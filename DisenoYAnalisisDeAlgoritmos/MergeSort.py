'''Algoritmo de ordenamiento MergeSort, capaz de ordenar de menor
a mayor una lista, dividiendo una lista dada en dos, y la cual se
ira dividiendo de manera recurisva, hasta donde llege el momento
en que se comparará los indices [0] de cada lista y de menor en
menor, se iran agregando a una nueva lista para acomodar estos
elementos de menor a mayor.
Su costo computaciones es de O(t*log2[t])
'''

def splitList(lista):
    pivot = int(len(lista)/2)
    '''La división del pivote redondea hacia el entero más cercano
     hacia abajo'''
    return lista[0:pivot], lista[pivot:len(lista)]

def merge(l1, l2):
    lr = []
    while len(l1) > 0 and len(l2) > 0:
        if l1[0] < l2[0]:
            lr.append(l1[0])
            l1.remove(l1[0])
        else:
            lr.append(l2[0])
            l2.remove(l2[0])
    return lr+l1+l2

def mergeSort(lista):
    if len(lista) > 1:
        l1, l2 = splitList(lista)
        l1 = mergeSort(l1)
        l2 = mergeSort(l2)
        return merge(l1,l2)
    else:
        return lista

def main():
    lista = [9,5,6,5,7,7,3]
    print(f'Lista normar: {lista}')
    print(f'Lista | MergeSort: {mergeSort(lista)}')

main()