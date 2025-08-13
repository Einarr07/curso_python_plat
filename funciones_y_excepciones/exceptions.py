# Exeptions in python
def print_exceptions(exception_class, indent=0):
    print(' ' * indent + exception_class.__name__)
    for subclass in exception_class.__subclasses__():
        print_exceptions(subclass, indent + 4)

print("----------------------------------")
print_exceptions(Exception)
print("----------------------------------")


try:
    divisor = int(input("Ingresa el divisor: "))
    result = 100/divisor
    print(result)
except ZeroDivisionError as e:
    print(f"Error: {e} \nEl divisior no puede ser cero")
except ValueError as e:
    print(f"Error: {e} \nDebes introducir un número valido")
except Exception as e:
    print(f"Error: {e}")

