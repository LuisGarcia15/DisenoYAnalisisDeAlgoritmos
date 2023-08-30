'''Algoritmo de busqueda BinarySearch, capaz de buscar un elemento
en una lista, dada una lista de n elementos la cual debe estar ordenada
de menor a mayor, La idea del algoritmo es dada la lista ordenada dada, encontrar
el elemento a la mitad de esta lista, posteriormente se verificará si el
número a buscar es menos, mayor o igual al elemento seleccionado, si es correcto
puede volverse una recursión hasta encontrar el número, si no encuentra
el número y el tamaño de esa lista es uno, regresa false. Su costo computacional
es de O(log2[n])'''
def binary_search(lista, item):
    if(len(lista) > 1):
        middle = int(len(lista)/2)
        value_in_middle = lista[middle]
        if (item > value_in_middle):
            return binary_search(lista[middle:len(lista)], item)
        elif (item < value_in_middle):
            return binary_search(lista[0:middle], item)
        elif (item == value_in_middle):
            return True
    else:
        if item == lista[0]:
            return True
        else:
            return False

def main():
    lista = [item for item in range(1,100000)]
    item = 1000
    print(f'Lista original: {lista}')
    print(f'Busqueda Binaria | Encontrar el número {item}: {binary_search(lista,item)}')

main()