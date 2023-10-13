'''
La piramide del sol en Teotihuacan pesa 57899 toneladas y tiene
una altura de 120 m, una ancho de 106 m y un largo de 94 m. Si
quisiera hacer una pirámide con exactamente una escala de 1/3,
¿Cuánto pesaría y cuáles serían sus dimensiones=
'''
import math
def piramide(ancho, altura, largo, peso, escala):
    '''Para resolver el problema debems entender que el volumen de
    la piramide es proporcional al peso de la piramide, por lo que,
    para reducir sus medidas debemos encontrar un factor de
    escala'''
    peso_uno_a_n= peso / escala
    '''Para encontrar el nuevo peso de la piramide que queremos
    obtener a escala, dividimos el peso original de la piramide
    entre la escala que queremos obtener [suponiendo que la escala
    que queremos obtener siempre es 1 a n]'''
    factor_de_proporcion = peso_uno_a_n / peso
    '''Encontramos el factor de proporcion para las medidad de la
    nueva piramide a escala dividiendo el peso de la piramide 
    a escala entre el peso de la piramide original'''
    factor_de_escala = pow(factor_de_proporcion, 1/escala)
    '''Para encontrar el factor de escala para que las medidas
    de la piramide original se reproduzcan a la escala deseada,
    encontramos la raiz n-esima (dependiendo la escala), del
    factor de proporcion'''
    ancho = ancho * factor_de_escala
    '''Multiplicamos todas las medidas por el factor de escala
    para obtener las medidas dada una escala n'''
    altura = altura * factor_de_escala
    largo = largo * factor_de_escala
    return f'[Piramide a Escala: {round(escala,2)} \nAncho: {round(ancho,2)} | Largo:' \
           f' {round(largo,2)} | Altura: {round(altura,2)} | Peso: {round(peso_uno_a_n,2)}]'

def main():
    print(piramide(106, 120, 94, 57899, 3))

main()