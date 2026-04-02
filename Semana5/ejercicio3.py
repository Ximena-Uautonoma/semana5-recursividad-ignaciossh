"""
Ejercicio 3:
Dado un número entero positivo N, calcular su factorial.

Debe implementar una versión iterativa y una recursiva.
"""

def factorial_ciclo(n):
    fac = 1
    for i in range (1, n+1):
        fac = fac*n
    return fac


def factorial_recursivo(n):
    pass
