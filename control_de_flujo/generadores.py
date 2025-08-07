# Generador simple
def my_generator():
    yield 1
    yield 2
    yield 3

print("Generador simple:")
for value in my_generator():
    print(value)

print("\n--------- Fibonacci ----------")
def fibonacci(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b

for num in fibonacci(100):
    print(num)

print("\n------------Números pares------------")
def numeros_pares(limit):
   a = 2
   while a < limit:
       yield a
       a +=2

for num in numeros_pares(100):
    print(num)