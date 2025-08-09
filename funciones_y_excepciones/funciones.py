def greet(name, last_name):
    print(f"Hello World {name} {last_name}")

greet("Marco", "Eurelio")

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def power(a, b):
    return a ** b

def calculator():
    while True:
        print("--------Calculadora-------")
        print("1.Sumar")
        print("2.Restar")
        print("3.Multiplicar")
        print("4.Dividir")
        print("5.Eleva")
        print("0.Salir")
        print("--------------------------------------")

        option = int(input("Seleccione una operacion: "))

        if option == 0:
            print("Saliendo del programa")
            break

        if option in [1,2,3,4,5]:
            a = float(input("Ingrese el valor de a: "))
            b = float(input("Ingrese el valor de b: "))

            if option == 1:
                print(f"Resultado: {add(a, b)}")
            elif option == 2:
                print(f"Resultado: {subtract(a, b)}")
            elif option == 3:
                print(f"Resultado: {multiply(a, b)}")
            elif option == 4:
                print(f"Resultado: {divide(a, b)}")
            elif option == 5:
                print(f"Resultado: {power(a, b)}")
            else:
                print("Operación no valida, intente de nuevo.")


calculator()

