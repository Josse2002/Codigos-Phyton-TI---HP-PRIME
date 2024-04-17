import math

# Intervalos
a = 0
b = 9

# Funcion
def funcion(X):
    return math.sqrt(X)

# Verificar si es continua
def is_continue(func, a, b):
    # Verificar si la función está definida y continua en todo el intervalo [a, b]
    for x in range(a, b):
        try:
            func(x)
        except Exception as e:
            print(f"La funcion no es continua en el intervalo [a, b]: {e}")
            return False
    print("La funcion es continua en el intervalo [a, b]")
    return True

# Verificar si es diferenciable
def is_differentiable(func, a, b):
    # Existe la derivada en el intervalo [a, b]?
    try:
        for x in range(a, b):
            func(x)
    except ZeroDivisionError:
        print("La funcion no es diferenciable en el intervalo [a, b]")
        return False
    else:
        print("La funcion es diferenciable en el intervalo [a, b]")
        return True

def aplicandoValorMedio(func, a, b):
    if is_continue(func, a, b) and is_differentiable(func, a, b):
        print("Se puede aplicar el metodo de Valor Medio")
        c = (func(a) - func(b)) / (a - b)
        print("El valor medio es: ", c)
        print("La funcion evaluada en el valor medio es: ", func(c))
    else:
        print("No se puede aplicar el metodo de Valor Medio")
        

# Ejemplo de uso
aplicandoValorMedio(funcion, a, b)
