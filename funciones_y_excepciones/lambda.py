add = lambda x, y: x + y
print(f"Función lambda suma en funcion lambda: {add(15, 3)}")

multiply = lambda x, y: x * y
print(f"Multiplicacion: {multiply(10, 5)}")

# Cuadrado de cada numero
number = range(11)
squared_numbers = list(map(lambda x: x ** 2, number))
print(f"Cuadrados: {squared_numbers}")

# Pares
evens_numbers = list(filter(lambda x: x % 2 == 0, number))
print(f"Evens: {evens_numbers}")

