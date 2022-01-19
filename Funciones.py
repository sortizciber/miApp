def esPrimo(numero):
    primo = 0
    for i in range(2, numero):
        resto = numero % i
        if resto == 0:
            primo = primo+1
    return primo == 0