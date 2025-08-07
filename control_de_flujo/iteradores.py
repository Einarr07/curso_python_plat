# Ejemplo de iterador

# Creamos una lista
my_list = [1,2,3,4,5]

# Obtener el iterador
my_iter = iter(my_list)

# Usar
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))

print("Iterando en cadenas")
# Iterar en cadenas

text = "Hola mundo"

# Creando el objeto
iter_text = iter(text)

# Iterando la cadena
for char in iter_text:
    print(char)

print("Iterando en cadenas")

# Numeros impares

# Limite
limit = 10

# Crear iterador
odd_itter = iter(range(1, limit+1, 2))

# Usando el iterador
for number in odd_itter:
    print(number)