import math
import random


class Persona:
    def __init__(self, numero_persona, lista_opiniones):
        self.__numero_persona = numero_persona
        self.__lista_opiniones = lista_opiniones

    @property
    def numero_persona(self):
        return self.__numero_persona

    @numero_persona.setter
    def numero_persona(self, numero_persona):
        self.__numero_persona = numero_persona

    @property
    def lista_opiniones(self):
        return self.__lista_opiniones

    @lista_opiniones.setter
    def lista_opiniones(self, lista_opiniones):
        self.__lista_opiniones = lista_opiniones

    def __str__(self):
        return f'{self.__numero_persona}'


def definicion_personas(numero_personas):
    num_personas_honestas = math.ceil(numero_personas * 0.51)
    lista_opiniones_honestos = []
    lista_opiniones_mentirosos = []
    lista_personas = []
    for item in range(numero_personas):
        if item >= num_personas_honestas:
            lista_opiniones_honestos.append(False)
            lista_opiniones_mentirosos.append(True)
        else:
            lista_opiniones_honestos.append(True)
            lista_opiniones_mentirosos.append(False)

    random.shuffle(lista_opiniones_honestos)
    random.shuffle(lista_opiniones_mentirosos)

    for item in range(numero_personas):
        if item >= num_personas_honestas:
            persona = Persona(item + 1, lista_opiniones_mentirosos)
            lista_personas.append(persona)
        else:
            persona = Persona(item + 1, lista_opiniones_honestos)
            lista_personas.append(persona)
    lista_aux = lista_personas.copy()
    random.shuffle(lista_personas)
    return lista_personas, lista_aux

def obtencion_honesto(lista):
    lista_persona = lista.copy()
    lista_final = []
    if len(lista_persona) == 1:
        return lista_persona[0]
    if len(lista_persona) == 0:
        return -1
    else:
        while(len(lista_persona) > 1):
            if lista_persona == 0:
                break
            persona_uno = lista_persona.pop(0)
            persona_dos = lista_persona.pop(0)
            indice_persona_uno = persona_uno.numero_persona-1
            indice_persona_dos = persona_dos.numero_persona - 1
            if persona_uno.lista_opiniones[indice_persona_uno] == \
                    persona_dos.lista_opiniones[indice_persona_uno]\
                    and persona_uno.lista_opiniones[indice_persona_dos] == \
                    persona_dos.lista_opiniones[indice_persona_uno]:
                lista_final.append(persona_uno)
        if len(lista_persona) == 1:
            lista_final.append(lista_persona.pop(0))
        return obtencion_honesto(lista_final)

def obtencion_mentirosos_honestos(honesto, lista_persona):
    mentirosos = set()
    honestos = set()
    for item in range(len(lista_persona)):
        if (honesto.numero_persona-1) == item:
            honestos.add(honesto)
            continue
        elif honesto.lista_opiniones[lista_persona[item].numero_persona -1]:
            honestos.add(lista_persona[item])
        else:
            mentirosos.add(lista_persona[item])
    return honestos, mentirosos
def los_mentirosos(num_personas):
    lista, lista_aux = definicion_personas(num_personas)
    honesto = obtencion_honesto(lista)
    while honesto == -1:
        random.shuffle(lista)
        honesto = obtencion_honesto(lista)
    return obtencion_mentirosos_honestos(honesto, lista)

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
