
# Calculanding factorianding
def factorial(n):
    """
    Funcion factorial(n):
    Con esta funcion se puede calcular el factorial de n

    Args:
        n (int): ingreso del numero que se precisa calcular

    Returns:
        int: resultado
    """
    resultado = 1
    #print(f"\nFactorial de {n}!")
    for i in range(1, n + 1): # el argumento range parte de (1) para que no multiplique por 0 y termina en (n + 1) esto se considera así porque el valor n es el tope, entonces con +1 este valor n si es incluido en la operacion.
        #print(f"{resultado} * {i}")
        resultado *= i # resultado * i = resultado.
        #print(f"-->{resultado}<--") # como puedo hacer un print de una variable antes y despues?
    return resultado

# input
# factorial_input = 4

# Ejemplo de uso
#print(factorial(10))
