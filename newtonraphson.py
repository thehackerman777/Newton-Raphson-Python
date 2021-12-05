import sympy as sp
from math import *


def NewtonRapson(x0,tol,n):
    x=sp.symbols('x')
    #INGRESAR LA FUNCIÓN
    f=input('Digite la función (variable x): ')
    df=sp.diff(f)#derivada de la función
    f=sp.lambdify(x,f)#convertimo en una expresión que se pueda evaluar numéricamente f
    df=sp.lambdify(x,df)#convertimo en una expresión que se pueda evaluar numéricamente derivada f
    for k in range(n):
        x1=x0-f(x0)/df(x0)#para calcular xi+1
        if(abs(x1-x0)<tol):
            print('iteración',k+1,'Xi+1 =',x1,end=' ')
            print('es una buena aproximación de la raíz')
            return
        x0=x1#cambiamos a xi por xi+1 para seguir iterando
        print('iteración',k+1,'Xi+1 =',x1)


print ("====== Metódo de Newton Rapshon ======\n")

#INGRESAR LOS DATOS
x0=int(input('Digite el primer valor : (x0)'))
n=int(input('Digite el numero de iteraciones: (n)'))

NewtonRapson(x0,0.0000001,n)