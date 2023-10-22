import math
import random


class Persona:
    def __init__(self, numero_persona, lista_opiniones):
        '''Clase Persona, almacena el número de persona y una lista
        de opiniones acerca de N personas'''
        self.__numero_persona = numero_persona
        self.__lista_opiniones = lista_opiniones

    @property
    def numero_persona(self):
        '''get de numero_persona'''
        return self.__numero_persona

    @numero_persona.setter
    def numero_persona(self, numero_persona):
        '''setter de numero_persona'''
        self.__numero_persona = numero_persona

    @property
    def lista_opiniones(self):
        '''get de lista_opiniones'''
        return self.__lista_opiniones

    @lista_opiniones.setter
    def lista_opiniones(self, lista_opiniones):
        '''set de lista_opiniones'''
        self.__lista_opiniones = lista_opiniones

    def __str__(self):
        '''toString del objeto Persona. Representación del objeto'''
        return f'{self.__numero_persona}'


def definicion_personas(numero_personas):
    '''Define el 51% de personas honestos y 49% de personas
    mentirosas'''
    num_personas_honestas = math.ceil(numero_personas * 0.51)
    '''Calcula el número de personas honestos'''
    lista_opiniones_honestos = []
    '''Listas para almacenar las opiniones de las personas
    honestas'''
    lista_opiniones_mentirosos = []
    '''Lista para almacenar las opiniones de las personas
    mentirosas'''
    lista_personas = []
    '''Lista para almacenar las N personas'''
    for item in range(numero_personas):
        '''Recorre el rango del número de personas pasado
        como parámetro'''
        if item >= num_personas_honestas:
            '''Si el numéro actual es mayor al número de personas
            honestas, agrega False a la lista de personas honestas
            pues son aquellas personas que seran mentirosas, mientras
            que cuando el número actual es menor al número de personas
            coloca True a la lista personas honestas pues son aquellas
            personas que seran honestas'''
            lista_opiniones_honestos.append(False)
            lista_opiniones_mentirosos.append(True)
        else:
            lista_opiniones_honestos.append(True)
            lista_opiniones_mentirosos.append(False)

    random.shuffle(lista_opiniones_honestos)
    '''Mezcla los valores de la lista de honestos y mentirosos'''
    random.shuffle(lista_opiniones_mentirosos)

    for item in range(numero_personas):
        '''Recorre el rango de números del número de personas
        y si el número actual es mayor al número pasado como
        parámetro, crea un objeto persona, con el número de
        persona igual al número actual del rango y agrega
        la lista de opiniones de mentirosos al objeto persona
        pues es un mentiroso. Agrega esa persona a la lista
        de personas'''
        if item >= num_personas_honestas:
            persona = Persona(item + 1, lista_opiniones_mentirosos)
            lista_personas.append(persona)
        else:
            '''Si el número actual es menor al número pasado como
            parámetro crea un objeto persona, con el número de persona
            igual al número actual del rango y agrega la lista de opiniones
            de honestos al objeto persona pues es un honesto. Agrega esa
            persona a la lista de personas'''
            persona = Persona(item + 1, lista_opiniones_honestos)
            lista_personas.append(persona)
    lista_aux = lista_personas.copy()
    '''Copia la lista de personas a una lista original, pues 
    en este momento, el 51% de las primeras personas son honestos
    y el otro 49% restante son mentirosos. Por lo que sabriamos
    donde estan los mentirosos'''
    random.shuffle(lista_personas)
    '''Mezcla la lista de personas para quelos mentirosos y honestos
    se mezclen'''
    return lista_personas, lista_aux
'''Retorna la lista con mezclada y la lista ordenanda'''

def obtencion_honesto(lista):
    '''Obtiene una persona honesta de toda
    una lista de personas'''
    lista_persona = lista.copy()
    '''Copia la lista de personas original'''
    lista_final = []
    '''lista que almacenará las personas una vez evaluadas
    y que posiblemente de uno de ellos sea el honesto'''
    if len(lista_persona) == 1:
        '''Caso base: si solo hay un elemento en la lista,
        entonces se encontro a la persona honesta y retorna
        esa persona'''
        return lista_persona[0]
    if len(lista_persona) == 0:
        '''Caso base: si no hay un elemento en la lista,
        entonces no se encontro a la persona honesta y retorna
        -1'''
        return -1
    else:
        '''Caso base: cuando la lista de personas son de 2 elementos
        o más'''
        while(len(lista_persona) > 1):
            '''Recorre la lista mientra su tamaño
            sea mayor a 1'''
            if lista_persona == 0:
                '''Si el tamaño de la lista es cero, 
                rompe el ciclo'''
                break
            '''Obtiene las dos primeras personas de la lista
            y los elimina de la lista original'''
            persona_uno = lista_persona.pop(0)
            persona_dos = lista_persona.pop(0)
            indice_persona_uno = persona_uno.numero_persona-1
            '''Obtiene los numeros de las personas, que seran a su
            vez el indice que tendra su opinio en las listas de opiniones
            que se crearon anteriormente'''
            indice_persona_dos = persona_dos.numero_persona - 1
            if persona_uno.lista_opiniones[indice_persona_uno] == \
                    persona_dos.lista_opiniones[indice_persona_uno]\
                    and persona_uno.lista_opiniones[indice_persona_dos] == \
                    persona_dos.lista_opiniones[indice_persona_uno]:
                lista_final.append(persona_uno)
                '''Verifica si, a la persona 1, su opinion de el es igual
                a la opinion de la persona 2 sobre la persona 1 y si a la
                persona 2, su opinion de el es igual a la opinion de la 
                 persona 1 sobre la persona 2. Si esta propocisión es verdadera,
                 agrea la persona uno a la lista final, ya que tecnicamente, 
                 las dos personas tienen la misma lista de opiniones'''
        if len(lista_persona) == 1:
            '''Si la lista persona tiene un solo elemento, significa que por
            ser los honestos mmayor número a los mentirosos, y no haber entrado
            al while pues todos los demas personas eran mentirosos o combinaciones
            de mentirosos con honestos, este unico elemento es un honesto, por
            lo que se agrega a la lista final'''
            lista_final.append(lista_persona.pop(0))
        return obtencion_honesto(lista_final)
'''Retorna la lista final'''

def obtencion_mentirosos_honestos(honesto, lista_persona):
    '''Obtiene dos conjuntos, donde contendran, como representación
    a las personas, su número de persona. Cada número de persona
    pertenecienta a si es mentiroso u honesto'''
    mentirosos = set()
    '''Conjunto que almacenará los mentirosos y honestos'''
    honestos = set()
    for item in range(len(lista_persona)):
        '''Recorre el rango de la lista de personas, para
        comparar cada persona con la opinión del honesto'''
        if (honesto.numero_persona-1) == item:
            '''Si el indice actual corresponde al honesto, lo
            ingresamos al conjunto de honestos y '''
            honestos.add(honesto)
        elif honesto.lista_opiniones[lista_persona[item].numero_persona -1]:
            '''Si con el índice actual, obtenemos a la persona actual 
            y obtenemos su indice. apartir de ese nuevo indice comparamos
            en la lista de opiniones del honesto, si es True, significa
            que es una persona honesta y lo agregamos al conjunto de
            honestos'''
            honestos.add(lista_persona[item])
        else:
            '''Si con el índice actual, obtenemos a la persona actual 
            y obtenemos su indice. apartir de ese nuevo indice comparamos
            en la lista de opiniones del honesto, si es False, significa
            que es un persona mentirosa y lo agregamos al conjunto de
            mentiroso'''
            mentirosos.add(lista_persona[item])
    return honestos, mentirosos
'''Retornamos el conjutno de personas honestas y mentirosas'''
def los_mentirosos(num_personas):
    '''Obtiene el conjunto de mentirosos y honestos'''
    lista, lista_aux = definicion_personas(num_personas)
    '''Obtiene la lista de personas mezcladas entre honestos
    y mentirosos y la lista de personas ordenadas de honestos
    a mentirosos'''
    honesto = obtencion_honesto(lista)
    '''Obtiene al honesto de la lista mezclada entre honestos
    y mentirosos'''
    while honesto == -1:
        '''Si el honesto es igual a -1, entonces no encontro
        a la persona honesta, se itera un ciclo hasta que encuentre
        a una persona honesta, pero mezclando la lista que ya estaba
        mezclada anteriormente, sino obtendriamos el mismo resultado
        infinitamente'''
        random.shuffle(lista)
        honesto = obtencion_honesto(lista)
    return obtencion_mentirosos_honestos(honesto, lista)
'''Retorna el conjunto de mentirosos y honestos'''

def main():
    honestos, mentirosos = los_mentirosos(100)
    personas_honestas = ''
    personas_mentirosas = ''
    for item in honestos:
        personas_honestas += f'|{item.__str__() }|'
    print(f'Honestos: \n{personas_honestas}')

    for item in mentirosos:
        personas_mentirosas += f'|{item.__str__()}|'
    print(f'Mentirosos: \n{personas_mentirosas}')
main()
