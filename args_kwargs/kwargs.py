"""
**kwargs se utiliza para recibir un número variable de argumentos nombrados (keyword arguments).
Esto significa que puedes pasar 0 o muchos argumentos con nombre y dentro de la función se recibe
como un diccionario (key: value)
"""

def print_info(**kwargs):
    print("------")
    for key, value in kwargs.items():
        print(f'{key}: {value}')


print_info(name='Marco', age=43, city='Loja')
print_info(name='María', age=52, city='Cuenca', country='Ecuador')