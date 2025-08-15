contador = 0
palabra = ""

while palabra != "fin":
    palabra = input("Escribe una palabra (escribe 'fin' para terminar): ")
    if palabra != "fin":
        contador += 1

print("Leyendo", contador, "palabras.")
