import math as MATH

#intervalo
a = 1
b = 2

#numero de iteraciones
iterations = None; # None es un valor nulo (no te lo han dado)
cantidadEpsilonica = 10**-7


# Funcion
def funcion(X):
    return X**3 + 4*X**2 - 10

def biseccion(func, a, b, iterations):
    print("N\t a\t\t b\t\t p\t\t f(a) \t\t f(b) \t\t f(p) \t\t Error relativo")
    print("------------------------------------------------------------------------------------------------------------------")
    
    if iterations != None and iterations > 0:
        for i in range(iterations + 1):
        
            p = (a + b) / 2
            f_p = func(p)

            error_relativo = abs((b - a) / b)
            print(f"{i}\t{a:.6f}\t{b:.6f}\t{p:.6f}\t{func(a):.6f}\t{func(b):.6f}\t{f_p:.6f}\t{error_relativo:.6f}")

            if(func(a) * f_p < 0):
                b = p
            elif(func(b) * f_p < 0):
                a = p
    elif cantidadEpsilonica != None and cantidadEpsilonica > 0:
        i = 0
        while True:
            p = (a + b) / 2
            f_p = func(p)

            error_relativo = abs((b - a) / b)
            print(f"{i}\t{a:.6f}\t{b:.6f}\t{p:.6f}\t{func(a):.6f}\t{func(b):.6f}\t{f_p:.6f}\t{error_relativo:.6f}")

            if(func(a) * f_p < 0):
                b = p
            elif(func(b) * f_p < 0):
                a = p
            
            if error_relativo < cantidadEpsilonica:
                break

            i += 1

    
    
        
        
    
    

biseccion(funcion, a, b, iterations)