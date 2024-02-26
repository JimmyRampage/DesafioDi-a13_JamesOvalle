# importando funciones creadas
import factorial as f
import productoria as p

def calcular(fact_1, prod_1, fact_2):
    resultado_fact_1 = f.factorial(fact_1)
    resultado_prod_1 = p.productoria(prod_1)
    resultado_fact_2 = f.factorial(fact_2)

    print(f"\nResultado factorial 1: {resultado_fact_1}")
    print(f"\nResultado productoria: {resultado_prod_1}")
    print(f"\nResultado factorial 2: {resultado_fact_2}\n")

calcular(fact_1 = 5, prod_1 = ([3,6,4,2,8]), fact_2 = 6)
