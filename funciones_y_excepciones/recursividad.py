def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


print(f"Factorial del valor 3: {factorial(3)}")

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(f"Fibonacci de 21: {fibonacci(21)}")

def sumatoria_numeros_naturales(n):
    if n == 0:
        return 0
    else:
        return n + sumatoria_numeros_naturales(n-1)

print(sumatoria_numeros_naturales(4))
