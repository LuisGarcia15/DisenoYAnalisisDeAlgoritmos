'''Algoritmo de ordenamiento BucketSort, capaz de ordenar de menor
a mayor una lista, dada una lista de n elementos, partimos de la idea
de crear una lista que se rellenará con ceros, en esa lista de ceros
se operará para establecer cuandos elementos existen por lo que a cada
elemento de la lista a ordenar le corresponde un indice de la
lista de casilleros [Lista de ceros]. A partir de esa lista de
ceros o lista de casilleros se irán creando los elementos en el orden
correcto en otra lista diferente a la lista de casilleros y a la
lista que se esta ordenando, denominada LR. Retornaremos esa lista
[LR] con los elementos ordenados. Su costo computacional es de O(t) aunque
si existen varios elementos repetidos, puede ser O(t´2)'''
def bucketSort(lista):
    min, max = foundMinMax(lista) #Reciben el elemento mínimo y máximo de la lista
    bucket = prepareBucket(min, max) #Crea la lista de casilleros, que tendra elementos cero
    bucket = fillBucket(bucket, lista, min)
    '''Rellena la lista de casilleros con el valor máximo de elementos que existen'''
    LR = reviewBucket(bucket,min)
    '''Guarda la lista orenada en la variable LR'''
    return LR

def foundMinMax(lista):
    '''Encuentra el valor mínimo y el valor máximo de la lista'''
    return min(lista), max(lista)

def prepareBucket(min,max): #Crea una lista de ceros, de la longitud de la lista - 1
    bucket = []
    for i in range((max-min)+1):
        '''Crea la lista de casilleros que llevará el conteo de elementos a ordenar,
        esta lista se rellena con ceros. la londitud de la lista sera la diferencia
        del valor máximo de la lista a ordenar menos el valor mínimo de la lista 
        a ordenar, posteriormente se le suma la unidad'''
        bucket.append(0)
    return bucket

def fillBucket(bucket, lista, min):
    '''Rellena la lista de casilleros, la cual solo contiene unicamente elemntos
    con el número cero. La rellena con el número de elementos que tendran en esos indices,
    esto quiere decir que si la lista a ordenar tiene dos elementos del número 1,
    en el indice donde ira el número 1 habra un número dos, expresando que existen
    dos numeros que tienen el mismo indice.

    Si existen elementos repetidos, esto puede hacer que la lista de casilleros no
    tenga la misma logintud que la lista origina que se esta ordenando'''
    for e in lista:
        bucket[e-min] += 1
    return bucket

def reviewBucket(bucket, min):
    LR = []
    for i in range(len(bucket)):
        '''Recorre toda la lista de elementos que eran ceros y que
        en este momento tienen el numero de elementos que deberan
        existir'''
        for j in range(bucket[i]):
            '''Recorre cada elemento de la lista de casilleros, como
            tiene el numero de elementos que deberan existir, puede recorrer
            desde 0 hasta n-1, donde n es el valor máximo en ese casillero'''
            LR.append(i+min)
            '''Suma el valor de i del for exterior con el valor minimo de la lista
            que se debe ordenar y lo agrega a la lista LR que será la lista ordenada'''
    return LR

def main():
    lista = [3,2,4,1,2,2,2]
    print(f'Lista normal: {lista}')
    print(f'Lista ordenado por BucketSort: {bucketSort(lista)}')

main()