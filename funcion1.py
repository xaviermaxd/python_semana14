def number_is_even(number):
    return True if number % 2 == 0 else False


def number_is_odd(number):
    return True if number % 2 != 0 else False


def lista_numeros_pares(numeros):
    lista = []
    for i in range(numeros+1):
        lista.append(i) if i % 2 == 0 else None

    return lista