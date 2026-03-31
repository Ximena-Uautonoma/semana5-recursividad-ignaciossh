"""
Ejercicio 1: Dado un número entero positivo N, retornar una lista con los números desde 1 hasta N.

Debe implementar dos funciones:
1. Una usando iteración (for o while)
2. Una usando recursividad
"""

def contar_ciclo(n):
    lista1 = [] 
    num = 0 
    while num<n:
        num = num+1
        lista1.append(num)
    print (lista1)

n = int(input("ingrese un numero"))
contar_ciclo(n)

    




    
    


def contar_recursivo(n):
    """
    Retorna una lista con los números desde 1 hasta n usando recursividad.
    """
    # Escriba aquí su solución y borre la palabra pass de acontinuación
    pass
