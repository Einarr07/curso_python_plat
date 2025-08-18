# 1) Recibira una lista de diccionarios
# Claves del diccionario -> nombre, edad, sexo

# 2) Debe devolver una lista de personas con el mismo sexo
from typing import Any

trabajadores = [
    {
        "nombre": "Martin",
        "edad": 18,
        "sexo": "M",
    },
    {
        "nombre": "María",
        "edad": 22,
        "sexo": "F",
    },
    {
        "nombre": "Hernesto",
        "edad": 60,
        "sexo": "M",
    }
]

def hombres(trabajadores: list[dict[str, Any]]) -> list[dict[str, Any]]:

    result = []

    for trabajador in trabajadores:
        if trabajador["sexo"] == "F":
            result.append(trabajador)

    return result


print(hombres(trabajadores))