# Modulo "Detalles de las funciones"

# Decoradores:

def Decoracion_turno(funcion):

    """Este decorador sera usado para mencionar informacion dirigida al usuario sobre las funciones generadores de turnos"""

    def mensaje_sandwich(self):

        print(f"Su turno es: {funcion(self)}\nAguarde y sera atentido.\n")

    """ print(f"Su turno es:", end = 0)
        print(funcion(self))
        print("Aguarde y sera atentido.\n")"""

    return mensaje_sandwich

# Generadores:

def nro_espera_P():
        
    """Genera y retorna un turno consecutivo diferente para el area de Perfumeria."""
    p = 0
    while True:
        p += 1
        yield f"P - {p}"

def nro_espera_F():

    """Genera y retorna un turno consecutivo diferente para el area de Farmacia."""
    f = 0
    while True:
        f += 1
        yield f"F - {f}"

def nro_espera_C():

    """Genera y retorna un turno consecutivo diferente para el area de Cosmetica."""

    c = 0
    while True:
        c += 1
        yield f"C - {c}"