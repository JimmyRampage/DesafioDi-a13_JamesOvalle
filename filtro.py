# importando librerias.
import sys

# Diccionario con los datos proporcionados por la empresa.
precios = {
    'Notebook': 700000,
    'Teclado': 25000,
    'Mouse': 12000,
    'Monitor': 250000,
    'Escritorio': 135000,
    'Tarjeta de Video': 1500000
}

# Funcion de filtro.
def filtro(u, o):
    """
    Funcion filtro(u, o)

    Args:
        u (int): Valor del umbral
        o (str): | mayor | menor

    Returns:
        list: retorna un listado con el corte del umbral y una opcion mayor o menor
    """
    # Si alguna de las dos condicion se se cumple, hara un print texto y creara la variable prod_filtrados con el diccionario correspondiente.
    if o == "mayor":
        print("\nlos poductos mayores al umbral son:")
        prod_filtrados = {k for k,v in precios.items() if v > u}

    elif o == "menor":
        print("\nlos poductos menores al umbral son:")
        prod_filtrados = {k for k,v in precios.items() if v < u}

    # Si ninguna condicion se cumple, entonces retornara el else.
    else:
        return "Lo sentimos, no es una operción válida"

    # utilizando el metodo .join() para concatenar strings, en este caso el set prod_filtrados.
    return ', '.join(prod_filtrados)

# Definiendo los argumentos a utilizar en las funciones.
umbral = float(sys.argv[1]) # Valor ingresado por consola.
opcion = "mayor" # Valor seteado en "mayor" por defecto.
if len(sys.argv) == 3: # En caso de ingresar un 3er argumento en consola.
    opcion = sys.argv[2] # se crea esta variable para hacer uso del 3er valor.

# Ejecutando la funcion y mostrandola su resultado en consola.
print(f"{filtro(umbral, opcion)}\n")

# Valores para ejecutar en consola:
#           [0]     [1]   [2]
# python filtro.py 30000
# python filtro.py 30000 mayor
# python filtro.py 30000 menor
# python filtro.py 30000 otro