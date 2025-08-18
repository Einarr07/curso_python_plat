def divide(a: int, b: int) -> float:
    # Validar que ambos sean enteros
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("El valor de a y b debe ser un número entero")

    # Verificar que el divisor no sea 0
    if b == 0:
        raise ValueError("El valor de b no debe ser cero")

    return a / b


try:
    print(divide(10, "fs"))
except TypeError as e:
    print("Error de tipo:", e)

try:
    print(divide(10, 0))
except ValueError as e:
    print("Error de valor:", e)

