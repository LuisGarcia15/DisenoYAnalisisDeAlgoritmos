import random

def mastermind():
    print('+'*10 + '| MASTERMIND |' + '+'*10)
    numero_pc = str(random.randrange(1000,9999,1))
    #numero_pc = '7066'
    numero_persona = ''
    lista_num_correcto = []
    lista_pos_incorrecta = []
    num_correctos = 0
    poscision_incorrecta = 0
    intentos = 8
    bandera = True
    while intentos >= 0 or bandera:
        print('#' * 60)
        print(f'Número aleatorio: {numero_pc}')
        numero_persona = input('Introduce un número de 4 cífras: ')
        if len(numero_persona) != 4:
            intentos -= 1
            print('X' * 60)
            print(f'Número equivocado: {numero_persona}')
            print(f'Cantidad de números correctos: {num_correctos}')
            print(f'Cantidad de poscisiones incorrectas: {poscision_incorrecta}')
            print(f'QUEDAN {intentos} INTENTOS')
            print('X' * 60)
            lista_num_correcto.clear()
            lista_pos_incorrecta.clear()
            num_correctos = 0
            poscision_incorrecta = 0
            continue
        for caracter in range(len(numero_pc)):
            if numero_persona[caracter] == numero_pc[caracter]:
                num_correctos += 1
                lista_num_correcto.append(caracter)
        if num_correctos == 4:
                print('$' * 60)
                print('FELICIDADES, ENCONTRASTE EL NÚMERO')
                print(f'Número ingresado: {numero_persona}')
                print(f'Número aleatorio: {numero_pc}')
                print(f'Número de intentos restantes: {intentos} intentos')
                print('$' * 60)
                bandera = False
                break
        else:
            for caracter_persona in range(len(numero_persona)):
                for caracter_pc in range(len(numero_pc)):
                    if caracter_pc in lista_num_correcto and \
                            numero_pc[caracter_pc] == numero_persona[caracter_persona] and\
                            caracter_pc == caracter_persona:
                        break
                    elif caracter_pc in lista_num_correcto and \
                            numero_pc[caracter_pc] == numero_persona[caracter_persona]:
                        continue
                    elif caracter_pc not in lista_num_correcto and \
                            caracter_pc not in lista_pos_incorrecta and \
                            numero_pc[caracter_pc] == numero_persona[caracter_persona]:
                        if numero_persona[caracter_persona] == numero_pc[caracter_persona]:
                            continue
                        else:
                            poscision_incorrecta += 1
                            lista_pos_incorrecta.append(caracter_pc)
                            break
        intentos -= 1
        if intentos < 1:
            print('*' * 60)
            print('FIN DEL JUEGO')
            print(f'Número equivocado: {numero_persona}')
            print(f'Número aleatorio: {numero_pc}')
            print(f'Cantidad de números correctos: {num_correctos}')
            print(f'Cantidad de poscisiones incorrectas: {poscision_incorrecta}')
            print(f'Quedan {intentos} intentos')
            print('*' * 60)
            lista_num_correcto.clear()
            lista_pos_incorrecta.clear()
            num_correctos = 0
            poscision_incorrecta = 0
            break
        else:
            print('*' * 60)
            print(f'Número equivocado: {numero_persona}')
            print(f'Cantidad de números correctos: {num_correctos}')
            print(f'Cantidad de poscisiones incorrectas: {poscision_incorrecta}')
            print(f'QUEDAN {intentos} INTENTOS')
            print('*' * 60)
            lista_num_correcto.clear()
            lista_pos_incorrecta.clear()
            num_correctos = 0
            poscision_incorrecta = 0


def main():
    mastermind()

main()
