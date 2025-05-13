#Parte Angie
def saludo():
    print("Hola, soy Angie")

import datetime

def saludar():
    print("\n¡Hola! Bienvenido/a al menú.")

def mostrar_fecha():
    fecha_actual = datetime.date.today()
    print(f"\nLa fecha de hoy es: {fecha_actual}")

def mostrar_materia():
    print("\nEstamos en la materia: Análisis de Sistemas")

def mostrar_menu():
    print("\n--- Menú de Opciones ---")
    print("1. Saludar")
    print("2. Mostrar fecha de hoy")
    print("3. Mostrar en qué materia estamos")
    print("4. Salir")
    print("------------------------")

def main():
    while True:
        mostrar_menu()
        opcion = input("Escribe el número de la opción que quieres: ")

        if opcion == '1':
            saludar()
        elif opcion == '2':
            mostrar_fecha()
        elif opcion == '3':
            mostrar_materia()
        elif opcion == '4':
            print("\nSaliendo del programa. ¡Hasta luego!")
            break
        else:
            print("\nOpción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()
