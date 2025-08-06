# Diccionario simple con números
numbers = {1: "uno", 2: "dos", 3: "tres"}

print("Diccionario numbers:")
print(numbers)

# Acceder a las claves, valores y pares clave-valor
print("\nClaves del diccionario:", numbers.keys())
print("Valores del diccionario:", numbers.values())
print("Elementos del diccionario (clave, valor):", numbers.items())

# Diccionario con datos personales
information = {
    "Nombre": "Juan",
    "Apellido": "Córdoba",
    "Altura": 1.30,
    "Edad": 19
}

print("\nDiccionario de información personal:")
print(information)

# Eliminar una clave
del information["Edad"]
print("\nDiccionario después de eliminar 'Edad':")
print(information)

contacts = {"Juan": {
"Nombre": "Juan",
    "Apellido": "Córdoba",
    "Altura": 1.30,
    "Edad": 19
},
    "Maria": {"Nombre": "Maria",
    "Apellido": "Córdoba",
    "Altura": 1.60,
    "Edad": 15}}

print("\nContactos:")
print(contacts)
print(f"\nInformación del contacto Maria {contacts["Maria"]}")
