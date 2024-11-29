# Paquetes Importados

from to_project.other import *
from to_project.detalles_funciones import *

# -----------------------------------------------------------------------------------------------------------------

# Codigo Principal.

clientes = []   # Esto simularia como si la empresa estuviera llevando un registro de los clientes: "Rut, turno, area."

turn_perfumeria = nro_espera_P()
turn_farmacia = nro_espera_F()
turn_cosmetica = nro_espera_C()

estado_1 = True
while (estado_1):

    system("cls")
    menu_1()

    choose = verificar_opcion("Ingresa una opcion:", "int", 1,2)
    if (choose == 1):

        system("cls")

        while (True):

            rut = verificar_opcion("Por favor, Ingrese su Rut.\nImportante! Omita puntos y guiones:", "alnum")
            
            if (len(rut) != 9):
                 system("cls")
                 print("Rut invalido. El rut ingresado no cuenta con la cantidad de 9 digitos.\n")
            else:
                 break

        costumer = Cliente(rut, "", "")      # Por ahora, los atributos: "turno y area" estaran vacios.
        clientes.append(costumer)

        estado_2 = True
        while (estado_2):

            menu_2()
            opcion = verificar_opcion("Ingresa el número de la opción:", "int", 1,2,3,4)

            if (opcion == 1):
                system("cls")

                asignar_turno(costumer, opcion, next(turn_perfumeria))
                costumer.mostrar_turno()

                pausa_menu()
                estado_2 = False

            elif (opcion == 2):
                system("cls")

                asignar_turno(costumer, opcion, next(turn_farmacia))
                costumer.mostrar_turno()

                pausa_menu()
                estado_2 = False

            elif (opcion == 3):
                system("cls")

                asignar_turno(costumer, opcion, next(turn_cosmetica))
                costumer.mostrar_turno()

                pausa_menu()
                estado_2 = False

            elif (opcion == 4):

                estado_2 = anular_turno()
    
    elif (choose == 2):

        estado_1 = anular_turno()
        system("cls")
