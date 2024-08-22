# Crear una calculadora en Python (Suma, Resta, Multiplicación y División)
print("-------Bienvenido al programa de Calculadora----------\n")


while True:

    print("Elige entre las siguientes opciones del 1 al 5")
    print("1-Suma\n2-Resta\n3-Multi\n4-Division\n5-Salir")

    print("-------------------------------------------------------\n")

    # funciones de suma, restar, multi, dividir}

    def suma():
        numero_uno = int(input(("Ingrese primer valor: ")))
        numero_dos = int(input(("Ingrese segundo valor: ")))
        return numero_uno + numero_dos

    def restar():
        numero_uno = int(input(("Ingrese primer valor: ")))
        numero_dos = int(input(("Ingrese segundo valor: ")))
        return numero_uno - numero_dos

    def multi():
        numero_uno = int(input(("Ingrese primer valor: ")))
        numero_dos = int(input(("Ingrese segundo valor: ")))
        return numero_uno * numero_dos

    def dividir():
        numero_uno = int(input(("Ingrese primer valor: ")))
        numero_dos = int(input(("Ingrese segundo valor: ")))
        try:
            numero_uno / numero_dos
        except ZeroDivisionError as error:
            return f"Lo siento no puedes dividir entre 0"
        else:
            return numero_uno / numero_dos

    eleccion_usuario = input("Ingrese una opción del 1 al 5: ")

    match eleccion_usuario:
        case "1":
            print("---Usted escogió sumar---\n")
            sumatoria = suma()
            print(f"La suma total es: {sumatoria}\n")

        case "2":
            print("---Usted escogió restar---\n")
            restar_numeros = restar()
            print(f"La resta total es: {restar_numeros}\n")
        case "3":
            print("---Usted escogió multiplicar---\n")
            multiplicar = multi()
            print(f"La multiplicación total es: {multiplicar}\n")
        case "4":
            print("---Usted escogió dividir---\n")
            dividiendo = dividir()
            print(f"La división total es: {dividiendo}\n")
        case "5":
            print("Usted está saliendo del programa.")
            break
        case _:
            print("Elige una opción válida.")
