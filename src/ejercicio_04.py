suma_total = 0
numero = None  

while numero != 0:
    numero = float(input("Ingresa un número (0 para salir): "))
    if numero != 0:  
        suma_total += numero


print("La suma total de los números ingresados es:", suma_total)
