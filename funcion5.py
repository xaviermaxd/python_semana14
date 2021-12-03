def serie_fibonacci(x):
    a=0
    b=1
    c=0
    for i in range (0,x):
        c = a + b
        print(a,"+",b,"=",c)
        a=b
        b=c


def suma_fibonacci(x):
    a=0
    b=1
    c=0
    suma=0
    for i in range (0,x):
        c = a + b
        suma += c
        a=b
        b=c
    return suma


def factorial(x):
    fact=1
    for i in range(1,x+1):
        fact *= i
    return fact