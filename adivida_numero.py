from random import *

numero_secreto = randint(1,100)
intentos = 1
acierto = False
fallo = False

nombre = input("Escribe tu nombre: ")
print(f"\nBueno, {nombre}, he pensado un número del 1 al 100, y tienes solo ocho intentos para adivinar cuál crees que es el número.")

while acierto != True and fallo != True:
    numero = int(input("Adivina el numero: "))
    if intentos == 8 and numero != numero_secreto:
        print(f"\nTu respuesta es incorrecta. Ademas, te haz quedado sin intentos. El numero secreto era: {numero_secreto}")
        break

    elif numero not in range(1,101): # Si el número que dijo el usuario es menor a 1 o superior a 100, le va a decir que ha elegido un número que no está permitido.
        print("\nHaz elegido un número que no esta permitido.")
        intentos += 1

    elif numero < numero_secreto: # Si el número que ha elegido el usuario es menor al que ha pensado el programa, le va a decir que su respuesta es incorrecta y que ha elegido un número menor al número secreto.
        print("\nTú respuesta es incorrecta. Haz elegido un número menor al número secreto.")
        intentos += 1

    elif numero > numero_secreto: # Si el usuario eligió un número mayor al número secreto, también se lo hará saber de la misma manera.
        print("\nTú respuesta es incorrecta. Haz elegido un número mayor al número secreto.")
        intentos += 1

    elif numero == numero_secreto: # Y si el usuario acertó el número secreto, se le va a informar que ha ganado y cuántos intentos le ha tomado.
        print(f"\nCorrecto. Haz acertado el numero secreto. Y te ha tomado {intentos} intentos.")
        acierto = True
