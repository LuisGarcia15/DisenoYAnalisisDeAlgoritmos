'''Algoritmo de ordenamiento BogoSort, capaz de ordenar de menor
a mayor una lista, todo esto de manera aleatoria, esto ya que
de manera aleatoria coloca los elementos en indices aleatorios
y cuando esta ordenada el algoritmo temina. Su costo computaciones
es de O(n!)'''
import random as rnd

def bogoSort(lista):
    counter = 0
    while (not sort_list(lista)):
        rnd.shuffle(lista)
        counter += 1
    print(f'Número de iteraciones: {counter}')
    return lista

def sort_list(lista):
    for i in range(len(lista)-1):
        if(lista[i] > lista[i+1]):
            return False
    return True

def main():
    lista = [4,2,3,1]
    print(f'Lista normal: {lista}')
    print(f'Lista ordenado por BogoSort: {bogoSort(lista)}')

main()
