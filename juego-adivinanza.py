import random


numero_secreto = random.randint(1,101)
cant_int = 0
cant_int_max = 5
adivinado = False

print("\-------------------------------------------------")
print("Bienvenido al juego de adivinar el número secreto")
print("-------------------------------------------------")
print("\nSolo tendras 5 intentos")

while not adivinado and cant_int < cant_int_max:
    entrada = input("\nIntroduce un número del 1 al 100: ") 
    numero = int(entrada)

    if numero == numero_secreto:
        print("\n--------------------------------------------------")
        print("¡Felicitaciones has adivinado el número secreto!")
        print("--------------------------------------------------")
        adivinado = True
    elif numero < numero_secreto:
        print("\nEl número es mayor al ingresado")
    else:
        print("\nEl número es menor al ingresado")
    cant_int +=1

if not cant_int < cant_int_max:
    print("¡\nGAME OVER! No has podido adivinar dentro de los 5 intentos")