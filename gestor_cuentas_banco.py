from random import *
import os

# Banco de funciones y clases

# Clases:

class Persona:

    # Atributos de intancia - 

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
    
class Cliente(Persona):

    # Atributos de instancia - Caracteristicas del Cliente

    def __init__(self, nombre, apellido, nro_cuenta, saldo):
        super().__init__(nombre, apellido)
        self.nro_cuenta = nro_cuenta
        self.saldo = saldo

    # Metodos de instancia - Acciones que podra hacer el Cliente.

    def depositar(self, i_dinero):  # i_dinero: Input dinero.
        self.saldo += i_dinero

    def retirar(self, o_dinero):    # o_dinero: Output dinero.
        self.saldo -= o_dinero

    # Metodos especiales - Estado de la cuenta bancaria del cliente.

    def __str__(self):
        return f"Cuenta Bancaria\n   - Usuario: {self.nombre} {self.apellido}\n   - Nro. de Cuenta: {self.nro_cuenta}\n   - Saldo Disponible: {self.saldo}"

# Funciones:

def crear_nro_cuenta(lista_clientes):

    """Genera y retorna un numero de 10 digitos numericos que representara el numero de cuenta de un cliente."""

    nro_no_generado = True
    while (nro_no_generado):

        # Se genera el numero de cuenta de maximo 10 numeros.

        nro_cuenta = ""
        for i in range(11):
            nro_cuenta += str(randint(0,9))
        
        if (len(lista_clientes) != 0):  # Se cumplira este "if" si existen clientes en "lista_clientes".
        
            # Se buscara si existe un cliente con el mismo numero de cuenta.

            for cliente in lista_clientes:
                if (nro_cuenta == cliente.nro_cuenta):
                    break
        nro_no_generado = False     # Si llega aqui, entonces el numero de cuenta generado no lo tiene ningun otro cliente.

    return nro_cuenta

def crear_cliente(nombre, apellido, dinero, lista_clientes):

    """Retorna un objeto cliente que cuenta con los atributos: nombre, apellido, nro_cuenta, dinero"""

    nro_cuenta = crear_nro_cuenta(lista_clientes)
    costumer = Cliente(nombre, apellido, nro_cuenta, dinero)
    return costumer

def rango_opciones(cantidad):
    os.system("cls")
    print(f"Opción seleccionada fuera de rango. Elige una entre 1-{cantidad}.\n")

def pausa_menu():

    """Muestra un mensaje previo para no mostrar el menu inmediatamente."""

    input("\nPreciona Enter para volver al menú.")
    os.system("cls")

def mostrar_menu_principal():

    print("--"*2, "Menu Principal","--"*2)
    print()
    print("[1] - Crear cuenta bancaria.")
    print("[2] - Ingresar a mi cuenta bancaria.")
    print("[3] - Salir.")
    print()

def mostrar_menu_cliente():

    print("--"*6, "Menu", "--"*6)
    print()
    print("[1] - Mostrar estado de cuenta.")
    print("[2] - Depositar dinero.")
    print("[3] - Retirar dinero.")
    print("[4] - Salir al menu principal.")
    print()

def existe_cliente(nro_cuenta, lista_clientes):

    """Retorna True si el cliente tiene una cuenta bancaria segun su numero de cuenta. En caso contrario, retorna False"""

    for cliente in lista_clientes:
        if (cliente.nro_cuenta == nro_cuenta):
            return True
    return False

def buscar_cliente(nro_cuenta, lista_clientes):

    """Retorna el objeto cliente segun el numero de cuenta."""

    for cliente in lista_clientes:
        if (cliente.nro_cuenta == nro_cuenta):
            return cliente

def salir():

    os.system("cls")

    no_finish = True
    while (no_finish):

        salida = input("\n¿Seguro quieres salir? (Y/N)\n  - ").upper()
        if (salida == "Y"):
            no_finish = False
            os.system('cls')
            return False

        elif (salida == "N"):
            no_finish = False
            os.system('cls')
            return True
            
        else:
            os.system("cls")
            print("Debes elegir entre Y/N.")

# -----------------------------------------------------------------------------------------------------------------

# Codigo principal:

lista_clientes = []

estado = True
while (estado):

    mostrar_menu_principal()
    opcion_principal = int(input("Ingresa una opción: "))

    if (opcion_principal not in range(1,4)):
        rango_opciones(3)

    elif (opcion_principal == 1):

        os.system("cls")
        print("Creación de Cuenta Bancaria")
        nombre = input("Ingresa tu nombre: ")
        os.system("cls")

        print("Creación de Cuenta Bancaria")
        apellido = input("Ingresa tu apellido: ")
        os.system("cls")
        dinero = 0

        costumer = crear_cliente(nombre, apellido, dinero, lista_clientes)
        lista_clientes.append(costumer)

        print(f"Se a creado exitosamente su cuenta bancaria:\n\n {costumer}")
        pausa_menu()

    elif (opcion_principal == 2):
        
        if (len(lista_clientes) == 0):
            os.system("cls")
            print("Debes crear una cuenta bancaria anteriormente. Digita la opcion [1]\n")
        
        else:

            os.system("cls")

            nro_cuenta_incorrecto = True
            while (nro_cuenta_incorrecto):

                nro_cuenta = input("Ingrese su numero de cuenta bancaria: ")

                if (existe_cliente(nro_cuenta, lista_clientes)):
                    os.system("cls")
                    costumer_user = buscar_cliente(nro_cuenta, lista_clientes)
                    nro_cuenta_incorrecto = False
                else:
                    os.system("cls")
                    print("Cuenta bancaria no encontrada. Verifique haber ingresado correctamente su numero de cuenta.")

            estado_2 = True
            while (estado_2):

                print(f"Welcome Back, {costumer_user.nombre}!\n")

                mostrar_menu_cliente()
                opcion = int(input("Ingresa una opción: "))

                if (opcion not in range(1,5)):
                    rango_opciones(4)

                elif (opcion == 1):
                    os.system("cls")
                    print(costumer_user)
                    pausa_menu()

                elif (opcion == 2):
                    
                    os.system("cls")

                    print("¿Cuanto quieres depositar en tu cuenta?")
                    deposito = int(input("Ingresa la cantidad: "))

                    os.system("cls")
                    costumer_user.depositar(deposito)
                    print(f"Se han enviado {deposito} unidades monetarias exitosamente a su cuenta.\nAqui esta el estado actual:\n\n{costumer_user}")
                    pausa_menu()

                elif (opcion == 3):

                    os.system("cls")

                    if (costumer_user.saldo == 0):
                        print("No puedes retirar dinero ya que no cuentas con saldo en tu cuenta bancaria.\n")
                        continue

                    retiro_incorrecto = True
                    while (retiro_incorrecto):

                        print("¿Cuanto quieres retirar de tu cuenta?")
                        retiro = int(input("Ingresa la cantidad: "))

                        if (retiro > costumer_user.saldo):
                            os.system("cls")
                            print(f"Retiro denegado. No puede retirar mas de lo que tiene en su cuenta.\nSaldo actual: {costumer.saldo}\n")

                        else:
                            costumer_user.retirar(retiro)
                            
                            os.system("cls")
                            print(f"Se han retirado {retiro} unidades monetarias exitosamente a su cuenta.\nAqui esta el estado actual:\n\n{costumer}")
                            retiro_incorrecto = False
                            pausa_menu()

                elif (opcion == 4):
                    estado_2 = salir()

    elif (opcion_principal == 3):
        estado = salir()
