N=int(input("ingrese un valor entero positivo "))

factorial=1

for i in range(1,N+1):

    factorial=factorial*i

print(f"el factorial de " + str (N) + " es " + str ( factorial))