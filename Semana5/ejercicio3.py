"""
Ejercicio 3:
Dado un número entero positivo N, calcular su factorial.

Debe implementar una versión iterativa y una recursiva.
"""

def factorial_ciclo(n):
    fac = 1
    for i in range (1, n+1):
        fac = fac*i
    return fac


def factorial_recursivo(n):
    if n == 0:
        return 1
    else:
        return n*(factorial_recursivo(n-1))
