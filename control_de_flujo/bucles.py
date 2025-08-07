numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in numbers:
    if i == 3:
        continue
    print(f"El valor de 'i' es igual a: {i}")

print("-----------------------")

for i in range(1,11):
    print(f"El valor de 'i' es igual a: {i}")

print("-----------------------")

fruits = ["apple", "banana", "cherry", "orange", "strawberry", "grapefruit"]

for index, fruit in enumerate(fruits):
    index += 1
    if fruit == "banana":
        print(f"Banana encontrada en la posición {index}")

print("-----------------------")

x = 0
while(x < 5):
    if x == 3:
        break
    x += 1
    print(x)
