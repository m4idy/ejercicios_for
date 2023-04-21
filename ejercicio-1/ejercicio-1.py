N = int(input("Ingrese la cantidad de números a leer: "))
pares = 0
impares = 0

for i in range (N):
    numero = int(input(f"Ingrese un número entero {i+1}: "))
    if numero % 2 == 0:
        pares=pares + 1
    else:
        impares=impares+ 1
print(f"Cantidad de números pares: " + str (pares))
print(f"Cantidad de números impares: " + str (impares))


