numero = int(input("Ingrese un número entero positivo: "))

suma_digitos = 0
for digito in str(numero):
    suma_digitos += int(digito)

print(f"La suma de los dígitos de {numero} es: {suma_digitos}")
