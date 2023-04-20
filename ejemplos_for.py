# ejemplo 1
rta= "salida = |"
for numero in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    rta=rta + str(numero) + " , "
rta = rta + "|"
print(rta)

# ejemplo 2
for numero in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    print("UIS NO ES UNO .....")

# ejemplo 3 
rta= "salida = |"
for nuemro in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10):
    rta=rta + str(numero) + " , "
rta = rta + "|"
print(rta)

# ejemplo 4 
rta= "salida = |"
for numero in range (1, 11):
    rta=rta + str(numero) + " , "
rta = rta + "|"
print(rta)

# ejemplo 5 
rta= "salida = |"
for numero in "UIS NO ES UNO":
    rta = rta + str (numero) + " , "
rta = rta + " | "
print(rta)

# ejemplo 6 
suma=0 
for numero in range (1, 11):
    suma=suma+1
print(f"la suma es {suma} ")

#ejemplo7
frase= input("digite una frase: ")
vocales= "aeiouAEIOU"
numero_vocales= 0
for i in frase:
    if i in vocales:
        numero_vocales=numero_vocales+1
print(f"en la frase hay {numero_vocales} vocales")


