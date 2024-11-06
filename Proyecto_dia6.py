from pathlib import Path
import os

# Banco de funciones:

def recorrer_carpetas(ruta_inicial):

    # Imprime todas las carpetas o archivos contenidos en la ruta de un directorio (carpeta).

    if ruta_inicial.is_dir() == True:   # Para verificar que la ruta termina en una carpeta.
        print(ruta_inicial)
        try:
            for ruta in ruta_inicial.iterdir():     # Para iterar por cada subcarpeta de una carpeta.
                print(ruta)
            print()

        except PermissionError:
            pass

def buscar_carpeta(file_inicial):

    # Recorre recursivamente por cada subcarpeta de una carpeta anterior hasta encontrar una carpeta especifica. En este caso, "Recestas"

    if (file_inicial.is_dir()):
        #print(file_inicial)  # Imprime la ruta de la carpeta.
        try:
            for sub_file in file_inicial.iterdir():     # Para iterar por cada subcarpeta de una carpeta.
                #print(sub_file)
                if (sub_file.name == 'Recetas'):        # Si encontramos la carpeta 'Recetas'
                    #print(f"Lo encontre: {sub_file}")
                    return sub_file                     # Retornamos la ruta y salimos del loop for.
                else:
                    resultado = buscar_carpeta(sub_file)      # Llamada recursiva
                    if resultado:                             # Si encontramos 'Recetas' en la recursión. La ruta en "resultado" en el "if" se entendera como True si se encuentra.
                        return resultado                      # Salimos de la función
            print()
        except PermissionError:
            pass

"""
Gracias a ChatGPT:
    - Detener la recursión: Se agrega una verificación después de la llamada recursiva. Si resultado no es None (lo
    que significa que se encontró "Recetas"), se retorna esa ruta y se sale de la función.
    - Que complejo es darle seguimiento a la recursividad, y mas aun, ver una manera de finalizarlo antes de tiempo y
    que arroje lo necesitado.
"""

def menu_opciones():
    
    print("Gestor de Recetas Local:")
    print()
    print("--"*5 ,"Menu", "--"*5)
    print()
    print("[1] - Leer receta.")
    print("[2] - Crear Receta.")
    print("[3] - Crear Categoria.")
    print("[4] - Eliminar Receta.")
    print("[5] - Eliminar Categoria.")
    print("[6] - Finalizar Programa.")
    print()

def pausa_menu():

    # Muestra un mensaje previo para no mostrar el menu inmediatamente.

    input("\nPreciona Enter para volver al menú.")
    os.system("cls")

def verifiacion_palabra(lista, palabra):

    # Analiza si la palabra recibida esta correctamente escrita segun la lista entregada.

    for word in lista:
        if (palabra == word):
            return True
    return False

def palabra_bien_escrita(eleccion, lista):

    # Retorna una palabra, ingresada por el usuario, hasta que este bien escrita segun como lo este en una lista. 

    wrong_word = True       # La palabra esta mal escrita o aun
    while (wrong_word):     # no se ha ingresado.

        word = input(f"\nElige una {eleccion}: ({", ".join(palabra for palabra in lista)})\nImportante: ¡Escribirlos tal cual!\n- ")
        if (verifiacion_palabra(lista, word)):   # Si esta bien escrita la categoria...
            wrong_word = False
            return word
        else:
            os.system('cls')
            print(f"{eleccion.capitalize()} no encontrada. Escribelo nuevamente.")

def elegir_categoria(path_categorias):

    # Busca las categorias disponibles y da a elegir alguna de esas.

    lista_categorias = []
    for sub_carpeta in path_categorias.iterdir():      # Para iterar por cada subcarpeta/categoria de la carpeta/Recetas.
        lista_categorias.append(sub_carpeta.name)      # Para enlistar solo los nombres de las subcarpetas/categorias.

    return palabra_bien_escrita("categoria", lista_categorias)

def elegir_receta(path_recetas):

    lista_recetas = []
    for archivo in path_recetas.glob("*.txt"):       # Para ubicar e iterar por cada archivo ".txt" de la carpeta.
        lista_recetas.append(archivo.stem)           # Para enlistar solo los nombres de los archivos sin su extención.

    return palabra_bien_escrita("receta", lista_recetas)

# -----------------------------------------------------------------------------------------------------------------

# Ruta de las recetas:

ruta = r"C:\Users\Estefano\Documents\Proyectos"
home = Path(ruta)                       # Ruta base del sistema de archivos de nuestro PC.

ruta_recetario = buscar_carpeta(home)     # Ruta donde se encuentran las recetas por categoria.

print("Bienvenido, Usuario!\n")
print(f"Ruta de acceso a las recetas:\n    - {ruta_recetario}\n")

# Contar cantidad de recetas dentro de la carpeta:

path_recetario = Path(ruta_recetario)

count = 0
for archivo in path_recetario.rglob("*.txt"): 
    count += 1

print(f"Hay {count} recetas en la carpeta.")

pausa_menu()
os.system('cls')

estado = True
while (estado):

    # Menú de opciones.

    menu_opciones()
    opcion = input("Ingresa una opción: ")

    if (int(opcion) not in range(1,7)):
        os.system("cls")
        print("Opción seleccionada fuera de rango. Elige una de 1-6.\n")

    # Opción 1
    
    elif (opcion == "1"):

        os.system("cls")

        # Mostrar y dar a elegir una Categoria:

        print("¿En que categoria quieres entrar?")
        categoria = elegir_categoria(path_recetario)

        os.system("cls")

        # Elegir, leer y mostrar receta segun la categoria elegida.

        print("¿Que receta quieres leer?")
        receta = elegir_receta(Path(path_recetario, categoria))

        archivo = open(Path(path_recetario, categoria, receta + ".txt"), "r")
        os.system("cls")
        print(archivo.read())
        archivo.close()

        pausa_menu()

    # Opción 2

    elif (opcion == "2"):

        os.system("cls")

        print("¿En que categoria quieres crear la nueva receta?")
        categoria = elegir_categoria(path_recetario)
        os.system("cls")
        
        # Crear la nueva receta en la categoria seleccionada y escribir en ella.

        print("¿Cual sera el nombre de la receta?")
        nombre_receta = input("\nNombre de la receta: ")
        archivo = open(Path(path_recetario, categoria, nombre_receta + ".txt"), "w")

        os.system("cls")
        print("Escribe tu receta. Para finalizar, digita 'fin'.\n")

        write_estado = True     # Representara que el usuario estara escribiendo (True). Sera False cuando ya no sea asi.
        while (write_estado):

            texto = input()
            if (texto.upper() == "FIN"):
                break
            else:
                archivo.write(texto + "\n")
        
        archivo.close()
        os.system("cls")

    # Opción 3

    elif (opcion == "3"):
        
        os.system("cls")

        no_create_file = True   # Hace referencia a que la carpeta aun no ha sido creada. Cuando lo sea, finalizara el bucle.
        while (no_create_file):

            nueva_categoria = input("\nNombre de la nueva categoria:\n  - ")
            path_new_categoria = Path(path_recetario, nueva_categoria)          # Ruta con el nombre de la carpeta/categoria a crear.
            
            if (path_new_categoria.exists()):               # Verifica que no exista anteriormente una carpeta con el mismo nombre en esa ruta.
                os.system("cls")
                print("\nYa existe una carpeta con el mismo nombre. Elige otro.")
            else:
                os.system('cls')
                os.makedirs(path_new_categoria)             # Crea la carpeta/categoria.
            
                print("¡La categoria se creo satisfactoriamente!")
                no_create_file = False                      # Ahora si fue creada la carpeta/categoria nueva.
                pausa_menu()

                os.system("cls")

    # Opción 4

    elif (opcion == "4"):

        os.system("cls")

        print("¿En que categoria se encuentra la receta a eliminar?")
        categoria = elegir_categoria(path_recetario)
        os.system("cls")

        print("¿Cual es la receta a eliminar?")
        receta = elegir_receta(Path(path_recetario, categoria))
        os.remove(Path(path_recetario, categoria, receta + ".txt"))     # Para remover/eliminar la receta. ("os.remove()" elimina archivos)
        
        os.system("cls")
        print("¡La receta se elimino satisfactoriamente!")

        pausa_menu()

    # Opción 5

    elif (opcion == "5"):
        os.system("cls")

        print("¿Que categoria quieres eliminar?")
        categoria = elegir_categoria(path_recetario)
        os.system("cls")

        os.rmdir(Path(path_recetario, categoria))     # Para remover/eliminar la carpeta/categoria. ("os.remove()" elimina archivos)
        
        os.system("cls")
        print("¡La categoria se elimino satisfactoriamente!")

        pausa_menu()

    # Opción 6

    elif (opcion == "6"):

        os.system("cls")

        no_finish = True
        while (no_finish):

            salida = input("\n¿Seguro quieres salir? (Y/N)\n  - ").upper()
            if (salida == "Y"):
                no_finish = False
                estado = False
                os.system('cls')

            elif (salida == "N"):
                no_finish = False
                os.system('cls')
            
            else:
                os.system("cls")
                print("Debes elegir entre Y/N.")