import math as MATH

a = 1
b = 2
decimales = 3  # Cantidad de decimales a mostrar

def funcion(X):
    return X - MATH.sqrt(X+1)

def intervalo_contiene_raiz(func, a, b):
    if func(a) * func(b) < 0:
        print("Existe una raiz en [a, b]")
    else:
        print("No existe una raiz en [a, b]")

    f_a = round(func(a), decimales)
    f_b = round(func(b), decimales)
    print("La funcion evaluada en " + str(a) + " da " + str(f_a))
    print("La funcion evaluada en " + str(b) + " da " + str(f_b))

intervalo_contiene_raiz(funcion, a, b)