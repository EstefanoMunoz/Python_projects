import random

lista_words = ['mariposa', 'computadora', 'extraordinario']  # Lista con las palabras que se puedes adivinar.
secret_word = random.choice(lista_words)

lista_sw = list(enumerate(secret_word))

vidas = 5

rellenar = []
for i in range(len(secret_word)):
    rellenar.append("_")

def interfaz(rellenar):

    print(f"\nVidas: {vidas}")
    for j in rellenar:
        print(j, end = '')

print("\nJuego del \"Ahorcado\"")

while ((vidas != 0)):

    interfaz(rellenar)
    letra = input('\n\nIngresa una letra: ')

    if ((letra in secret_word) == True):
        
        for a,b in lista_sw:   # Para iterar por cada letra en la palabra oculta.
            if (b == letra):
                rellenar[a] = letra

        if (''.join(rellenar) == secret_word):
            print(f"¡Ganaste! La palabra secreta era: {secret_word}")
            break

    else:
        vidas -= 1

if (vidas == 0):
    print(f"\n¡Perdiste! La palabra completa era: {secret_word}")

# Falta crear una lista donde se guarden las letras que son incorrectas, para imprimirlas en cada ingreso de letra.
