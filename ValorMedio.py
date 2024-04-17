# Para encontrar los valores de c que satisfacen f'(c) = f_c en un intervalo [a, b] 
# y aplicar el Teorema del Valor Medio
import sympy as sp

# Intervalos
a = 0
b = 2

# Función
x = sp.Symbol('x')
funcion = 1/(x-1)

# Verificar si es continua
def is_continue(func, a, b):
    # Verificar si la función está definida y continua en todo el intervalo [a, b]
    for value in range(a, b+1):
        try:
            func.subs(x, value)
        except Exception as e:
            print(f"La funcion no es continua en el intervalo [a, b]: {e}")
            return False
    print("La funcion es continua en el intervalo [a, b]")
    return True

# Verificar si es diferenciable
def is_differentiable(func, a, b):
    try:
        x = sp.Symbol('x')
        sp.diff(func, x)
    except Exception as e:
        print(f"La funcion no es diferenciable en el intervalo [a, b]: {e}")
        return False
    else:
        print("La funcion es diferenciable en el intervalo [a, b]")
        return True

# Encontrar valores de c que satisfacen f'(c) = f_c
def encontrandoValorC(func, a, b, f_c):
    # Derivar la función
    f_prime = sp.diff(func, x)
    
    # Resolver la ecuación f'(c) = f_c para encontrar el valor de c
    soluciones = sp.solve(f_prime - f_c, x)
    
    # Filtrar las soluciones que son reales y están dentro del intervalo [a, b]
    soluciones_validas = [solucion.evalf() for solucion in soluciones if solucion.is_real and a <= solucion.evalf() <= b]
    
    return soluciones_validas


# Aplicar el Teorema del Valor Medio
def aplicandoValorMedio(func, a, b):
    if is_continue(func, a, b) and is_differentiable(func, a, b):
        print("Se puede aplicar el metodo de Valor Medio")
        f_a = func.subs(x, a)
        f_b = func.subs(x, b)
        f_c = (f_b - f_a) / (b - a)
        print("f'(c): ", f_c)
        c = encontrandoValorC(func, a, b, f_c)
        print("Los valores de c que cumplen con la condición son ", c)
    else:
        print("No se puede aplicar el metodo de Valor Medio")
        
# Ejemplo de uso
aplicandoValorMedio(funcion, a, b)
