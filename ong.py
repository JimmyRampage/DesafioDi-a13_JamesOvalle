## Esto
# importando funciones creadas
from factorial import factorial as f
from productoria import productoria as p

def calcular(**kwargs):
    """
    _summary_
    Esta funcion opera con argumentos keywords arguments **

    Args:
        Los argumentos validos para operar esta funcion con **kwargs
        fact_1 = (int) : calcula factorial 1
        fact_2 = (int) : calcula factorial 2
        prod_1 = [list] : calcula productoria 1
        prod_2 = [list] : calcula productoria 2

    Returns:
        Resultados de hasta 2 factoriales y hasta dos productorias. (int)
    """
    if 'fact_1' in kwargs: # Verifica si 'fact_1' está presente en kwargs y llama a la función factorial.
        resultado_fact_1 = f(kwargs['fact_1']) # Utilizando kwards le digo que el valor se encuentra dentro de la variable, y con ['fact_1'] le estoy indicando que esta funcion opera especificamente con ese string.
        print(f"\nResultado factorial 1: {resultado_fact_1}")
    else:
        print("\nfact_1 no proporcionado")

    if 'prod_1' in kwargs: # Verifica si 'prod_1' está presente en kwargs y llama a la función productoria.
        resultado_prod_1 = p(kwargs['prod_1'])
        print(f"Resultado productoria: {resultado_prod_1}")
    else:
        print("prod_1 no proporcionado")

    if 'fact_2' in kwargs: # Verifica si 'fact_2' está presente en kwargs y llama a la función factorial.
        resultado_fact_2 = f(kwargs['fact_2'])
        print(f"Resultado factorial 2: {resultado_fact_2}")
    else:
        print("fact_2 no proporcionado")

    if 'prod_2' in kwargs: # Verifica si 'prod_2' está presente en kwargs y llama a la función productoria.
        resultado_prod_2 = p(kwargs['prod_2'])
        print(f"Resultado productoria: {resultado_prod_2}\n")
    else:
        print("prod_2 no proporcionado\n")



# Linea solicitada para ejecutar el script
calcular(fact_1=5, prod_1=[3,6,4,2,8], fact_2=6)
# output | fact_1 = 120 | prod_1 = 1152 | fact_2 = 720 | prod_2 no proporcionado


# Opcional para verificar
# calcular(fact_1 = 4, prod_1 = [1,4,2,6,3], fact_2 = 3, prod_2 = [5,3,1,5])
# output | fact_1 = 24 | prod_1 = 144 | fact_2 = 6 | prod_2 = 75