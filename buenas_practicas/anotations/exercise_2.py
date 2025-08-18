#Estudiantes
from typing import Any

estudiantes = [
    {"nombre": "Ana", "nota": 8.5, "curso": "Matemáticas"},
    {"nombre": "Luis", "nota": 6.9, "curso": "Historia"},
    {"nombre": "Marta", "nota": 9.0, "curso": "Inglés"},
]


def aprobados(estudiantes: list[dict[str, Any]]) -> list[dict[str, Any]]:

    return [aprobado for aprobado in estudiantes if aprobado["nota"] > 7]

print(f"Los estudiantes aprobados son:\n{aprobados(estudiantes)}")

# Productos

productos = [
    {"nombre": "Laptop", "precio": 1200.50, "stock": 10},
    {"nombre": "Mouse", "precio": 25.99, "stock": 50},
    {"nombre": "Teclado", "precio": 75.00, "stock": 30},
    {"nombre": "Monitor", "precio": 250.00, "stock": 15},
]

def productos_caros(productos: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return [caro for caro in productos if caro["precio"] > 100]

print(f"Los productos caros son:\n{productos_caros(productos)}")

# Pelicula

peliculas = [
    ("El Señor de los Anillos", 201, "Fantasía"),
    ("Toy Story", 81, "Animación"),
    ("Titanic", 195, "Romance"),
    ("Intensamente", 102, "Animación"),
]

Pelicula = tuple[str,int,str]

def peliculas_largas(peliculas: list[Pelicula]) -> list[Pelicula]:
    return [peli for peli in peliculas if peli[1] > 120]

print(f"La lista de peliculas largas son:\n{peliculas_largas(peliculas)}")
