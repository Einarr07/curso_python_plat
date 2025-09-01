"""
*args se utiliza para recibir un número variable de argumentos posicionales dentro de una función.
Esto significa que puedes pasar 0, 1 o muchos argumentos y dentro de la función se recibirán como una tupla.
"""

def sum_numbers(*args):
    return sum(args)

print(sum_numbers(1, 2, 3))
print(sum_numbers(1, 2, 43))