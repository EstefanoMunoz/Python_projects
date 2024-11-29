# Modulo de definicion de funciones y clases:

from os import system
from to_project.detalles_funciones import *

# -----------------------------------------------------------------------------------------------------------------

# Clases:

class Cliente:

    # Atributos de Instancia (Cliente)

    def __init__(self, rut, ticket, area):
        self.rut = rut          # Tipo str.
        self.ticket = ticket    # Tipo str.
        self.area = area        # Tipo str.
    
    # Metodos de Instancia (Cliente)

    @Decoracion_turno
    def mostrar_turno(self):
        return self.ticket

# Funciones:

def pausa_menu():

    """Detiene el codigo para no pasar directamente a mostrar el menu hasta que el usuario precione 'Enter'"""
    input("Presiona 'Enter' para continuar...")

def menu_1():

    """Muestra, el menu principal de ingreso de datos del usuario: 'rut'."""

    print("--"*4, "Generador de turnos", "--"*4,"\n")
    print("   [1] - Ingresar el Rut")
    print("   [2] - Salir\n")

def menu_2():

    """Muestra, el menú de areas a donde el usuario puede ir 'Perfumeria, Farmacia, Cosmetica'."""

    system("cls")

    print("--"*4, "Menu Farmacia" ,"--"*4)
    print()
    print("Areas disponibles:")
    print()
    print("   [1] - Perfumeria")
    print("   [2] - Farmacia")
    print("   [3] - Cosmetica")
    print("   [4] - Anular Turno")
    print()

def verificar_opcion(mensaje, tipo, *args):

    """Informacion 1: La función evita que, en casos de posible ingreso erroneo del usuaio en el input, el codigo no se detenga y arroje un mensaje que no pueda entender.

    Parametros:
        - 'mensaje': Para especificar el mensaje que el desarrollador quiera decir en el input.
        - 'tipo': Para que la funcion retorne si quiere un valor de tipo 'str' o 'int'.
        - *args: Solo para ingresar la cantidad de opciones numericas y verificar que el valor 'int' del usuario no salga de ese rango/numeros."""

    def funcion(lista):

        while (True):

            try:
                opcion = input(f"{mensaje} ")

                if (tipo == "alnum" and not opcion.isalnum()):
                    system("cls")
                    print("Incorrecto. Tienes que ingresar un valor numerico o alfa-numerico.")

                elif (tipo == "str" and not opcion.isalpha()):
                    system("cls")
                    print("Incorrecto. Tienes que ingresar una letra.")
                
                elif (tipo == "int" and not opcion.isnumeric()):
                    system("cls")
                    print("Incorrecto. Tienes que ingresar un numero.")

                elif (tipo == "int" and int(opcion) not in lista and len(args) != 0):   # len(args) != 0 , es para identificar si esta vacio o no "*args".
                    system("cls")
                    print(f"Incorrecto. El número seleccionado esta fuera del rango.\nElige alguna: {lista}\n")

                else:
                    return opcion

            except KeyboardInterrupt:
                system("cls")
                print("Incorrecto. Realizaste una combinación del teclado incorrecto.")

                pausa_menu()
                system("cls")

    lista = [i for i in args]
    if (tipo == "str" or tipo == "alnum"):
        return str(funcion(lista))
    
    elif (tipo == "int"):
        return int(funcion(lista))

def anular_turno():
    
    """Retorna True si el usuario ingresa 'Y', y False si ingresa 'N'. Para ambos casos, la funcion se encarga que ingrese o 'Y' o 'N'"""

    system("cls")

    state = True
    while (state):

        opcion = verificar_opcion("¿Seguro quieres anular el turno? (Y/N)", "str")
        if (opcion.upper() == "Y"):
            return False
        elif (opcion.upper() == "N"):
            return True
        else:
            system("cls")
            print("Incorrecto. Tienes que ingresar 'Y' o 'N'.")

def asignar_turno(costumer, opcion, turn):

    if (opcion == 1):
        costumer.area = "Perfumeria"
        costumer.ticket = turn
    
    elif (opcion == 2):
        costumer.area = "Farmacia"
        costumer.ticket = turn

    elif (opcion == 3):
        costumer.area = "Cosmetica"
        costumer.ticket = turn