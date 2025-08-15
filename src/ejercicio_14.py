import random 


numero_secreto = random.randint(1, 10)

adivinanza = None

while adivinanza != numero_secreto:
    adivinanza = int(input("Adivina el número (entre 1 y 10): "))
    if adivinanza != numero_secreto:
        print("No es el número, intenta de nuevo.")

print(f"¡Felicidades! Adivinaste el número {numero_secreto}.")
