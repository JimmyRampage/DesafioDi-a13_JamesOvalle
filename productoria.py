
# Creando la funcion de productoria
def productoria (lista):
    """
    Funcion productoria(lista):
    Con esta funcion se puede calcular el productorial de una lista entregaga

    Args:
        lista (list): ingreso de la lista que se precisa calcular

    Returns:
        int: resultado
    """
    resultado = 1
    #print(f"\nProductoria de {lista}")
    for i in lista:
        resultado *= i

    return resultado

#print(productoria([3,6,4,2,8]))
# Solicitando el ingreso de datos al usuario.
# lista = input("Ingresa los números separados por coma, sin espacios: ")

# Transformando el input en una lista numerica mediante comprehensions.
# Para numeros en lista.split() conviertelo a entero y registralo en la lista.
# lista_int = [int(numero) for numero in lista.split(",")]

# Utilizando la funcion productoria
#print(productoria(lista_int))
