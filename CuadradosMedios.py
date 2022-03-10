
##TERMINADO

semilla = input("Escriba semilla: ")
tam1 = 4
print("Cantidad de dígitos: ", tam1)
numero1 = int(semilla)
for i in range(10):
    # Elevamos al cuadrado
    numero2 = numero1**2
    snumero2 = str(numero2)
    # Obtenemos el largo del numero
    tam2 = len(snumero2)
    primerc = int((tam2 - tam1) / 2)

    # posición inicial de la subcadena
    # posición final de la subcadena (excluida)

    # Hacemos el substring
    snumero3 = snumero2[primerc:primerc+tam1]
    print("{}.  {}".format(i, snumero3))
    numero1 = int(snumero3)