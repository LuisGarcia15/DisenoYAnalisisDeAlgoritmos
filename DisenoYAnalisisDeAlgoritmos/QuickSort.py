'''Algoritmo de ordenamiento QuickSort, capaz de ordenar de menor
a mayor una lista, partiendo de que en una lista, se encuentra un
pivote, apartir de ese pivote se van agregando valores mayores al
pivote en na lista y menores a ese pivote a otra lista, esto de
manera recursiva. Su costo computaciones es de O(t*log2[t])'''
def foundPivot(list):
    return sum(list)/len(list)

def divideMinorsAndMajors(list, pivot):
    minors = []
    majors = []
    for item in range(0, len(list)):
        if list[item] < pivot:
            minors.append(list[item])
    for item in range(0, len(list)):
        if list[item] >= pivot:
            majors.append(list[item])
    return minors,majors

def repeatingElements(list):
    for item in range(1, len(list)):
        '''For recorre todos los elementos de la lista'''
        if not (list[item-1] == list[item]):
            '''
            1-. Verifica si los elementos sucesores {Lista[1] = Lista[2],
            Lista[2] = Lista[3], Lista[3] = Lista[4], ..., Lista[n] = Lista[n+1]}
            son iguales.
            
            2-. Si los elementos sucesores son iguales, esto quiere decir que la
            propocisión es {True}, pero gracias al NOT, su valor de verdad sera
            {False}, por lo que NO entrará al cuerpo de IF.
            
            3-. Si los elementos sucesores NO son iguales, esto quiere decir que la
            propocisión es {False}, pero gracias al NOT, su valor de verdad sera
            {TRUE}, por lo que entrará al cuerpo de IF.
            
            4-. Dentro del cuerpo del IF, regresará FALSE.
            '''
            return False
    return True
    '''Si todos los elementos de la lista son iguales, quiere decir que no entró
    en el cuerpo del bloque if y NO regreso {FALSE}, por lo que regresá {TRUE}. El
    que regrese {TRUE} quiere decir que evaluó que todos los elementos son repetidos,
    contrario, si regresó {FALSE} quiere decir que evaluo que algunos elementos de la
    lista NO son repetidos'''

def quickSort(list):
    if len(list) > 1 and not repeatingElements(list):
        '''
        1-. Si la lista tiene tamaño mayor a uno y el método repeatingElements() regresa
        {FALSE}, gracias al NOT esa proporcisión es {TRUE} y entrá al código del bloque
        IF. Esto quiere decir que en esa lista evaluada hay elementos diferentes entre si.
        
        2-. Si la lista tiene tamaño mayor a uno y el método repeatingElements() regresa
        {TRUE}, gracias al NOT esa proporcisión es {FALSE} y NO entrá al código del bloque
        IF. Esto quiere decir que en esa lista evaluada TODOS los elementos son iguales entre si.'''
        pivot = foundPivot(list)
        minors, majors = divideMinorsAndMajors(list, pivot)
        minors = quickSort(minors)
        majors = quickSort(majors)
        return minors + majors
    else:
        return list
        '''Retorna la lista evaluada si la longitud de la lista es uno (tambien se puede decir que 
        esa lista solo tiene un elemento) o retorna una lista donde todos sus elementos son iguales
        y por lo tanto no ejecuto recursivamente el método Quicksort()'''
def main():
    list = [9,4,7,66,77,8,0,40,9,4,7,66,89,100,4,4,4,5,6,77,8,9,100,55,64,6,5,4,7,8,9]
    print(f'Lista Original: {list}')
    print(f'Lista ordenada por QuickSort: {quickSort(list)}')

main()