# Cuadrados del 1 al 10
from traceback import print_tb

squares = [x**2 for x in range(1, 11)]
print(f"Los cuadrados son: {squares}")

# Transformación de grados Celsius a Fahrenheit
celsius = [0, 10, 20, 30, 40, 50]
fahrenheit = [round((temp * 9/5) + 32, 1) for temp in celsius]  # redondeado a 1 decimal
print(f"La temperatura en ºF: {fahrenheit}")

# Números pares entre 1 y 19
evens = [x for x in range(1, 21) if x % 2 == 0]
print(evens)

# Trnaspuesta de una matris
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print(matrix)
print(transposed)

