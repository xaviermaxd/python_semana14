import operaciones

lista = []
x = int(input("cantidad de terminos de una lista: "))
for i in range(x):
    n = int(input("ingrese un numero: "))
    lista.append(n)
print(lista)


print("la suma es: ",operaciones.funcion_suma(lista))
print("la multiplicacion es :",operaciones.funcion_producto(lista))