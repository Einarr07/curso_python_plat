# 1. Uso básico de print
# Imprime un texto directamente
print("Nunca pares de aprender")

# 2. Uso de la coma en print
# Python añade espacios automáticamente entre argumentos
print("Nunca", "pares", "de", "aprender")

# Concatenación sin espacios
print("Nunca" + "pares" + "de" + "aprender")

# Concatenación con espacios añadidos manualmente
print("Nunca" + " " + "pares" + " " + "de" + " " + "aprender")

# 3. Uso de sep
# El parámetro sep define el separador entre argumentos
print("Nunca", "pares", "de", "aprender", sep=", ")

# 4. Uso de end
# El parámetro end define lo que se imprime al final
print("Nunca", end=" ")
print("pares de aprender")

# 5. Impresión de variables
frase = "Nunca pares de aprender"
autor = "Platzi"
print("Frase:", frase, "Autor:", autor)

# 6. Uso de formato con f-strings
print(f"Frase: {frase}, Autor: {autor}")

# 7. Uso de formato con format
print("Frase: {}, Autor: {}".format(frase, autor))

# 8. Impresión con formato específico
valor = 3.14159
print("Valor: {:.2f}".format(valor))  # Muestra 2 decimales

# 9. Saltos de línea y caracteres especiales
# \n crea una nueva línea
print("Hola\nmundo")

# Comillas dentro de cadenas
print('Hola soy \'Carli\'')  # Imprime: Hola soy 'Carli'

# Impresión de una ruta con barras invertidas
print("La ruta de archivo es: C:\\Users\\Usuario\\Desktop\\archivo.txt")
