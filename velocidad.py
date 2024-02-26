# Lista de datos entregados por la empresa (60).
velocidad = [
    25, 12, 19, 16, 11, 11, 24, 1,
    14, 14, 16, 10, 6, 23, 13, 25, 4, 19,
    14, 20, 18, 9, 18, 4, 18, 1, 3, 4, 2,
    14, 23, 19, 23, 9, 18, 20, 22, 14, 1,
    10, 5, 23, 3, 5, 9, 5, 3, 12, 20, 5,
    11, 10, 18, 10, 14, 5, 23, 20, 23, 21
]
# Creando una funcion para calcular el promedio de una lista.
def promedio_lista(lista):
    """
    Funcion promedio_lista
    Esta funcion permite calcular el valor medio de una lista.

    Args:
        lista (list[int|float]): el argumento debe ser una lista numerica.

    Returns:
        float: retorna el promedio de la lista utilizando las funciones sum() y len().
    """
    promedio = sum(lista) / len(lista)
    return promedio

# Definiendo la variable promedio fuera de la funcion, pero al mismo tiempo utilizando la funcion para determinal el valor de promedio.
promedio = promedio_lista(velocidad)

# Creando una lista ordenada utilizando comprehensions y enumerate().
# i=indice n=valor
# para i, n en enumerate(velocidad) | enumerate sirve para que me devuelva el i & n de una lista | si el valor de n es mayor al promedio, entonces anotame el indice de velocidad 'i' en la lista
sobre_prom = [i for i, n in enumerate(velocidad) if n > promedio]


print(f"\nEl promedio de la lista es: {promedio_lista(velocidad)}")
print(f"\nLa posicion de las coreas sobre el promedio son:\n{sobre_prom}\n")

# para ejecutar el script utilizar:
# python velocidad.py