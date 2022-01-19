from Funciones import esPrimo

num = int(input("Introduce un número para saber si es primo: "))
resultado = esPrimo(num)

if resultado==True:
    print(f"El número {num} es primo")
else:
    print(f"El número {num} no es primo")