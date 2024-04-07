import math as MATH

#intervalo
a = 1
b = 2

# Criterio de parada
epsilon = 10**-3 

def cantidadIteraciones(a, b, epsilon):
    iteraciones = round(MATH.log2((b - a) / epsilon))
    print("La cantidad de iteraciones en biseccion es: " + str(iteraciones))

cantidadIteraciones(a, b, epsilon)
