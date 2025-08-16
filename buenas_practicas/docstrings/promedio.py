def calculate_average(numbers):
    """
    Calcula el promedio de una lista de números

    :param numbers:
    numbers (list): Una lista de números enteros o flotantes
    :return:
    float: El promedio de los números en la lista
    """
    return sum(numbers) / len(numbers)

# Imprimiendo el resultado de la función
print(calculate_average([1, 2, 3, 4, 5]))
