def outer_function():
    x = "enclosing"

    def inner_function():
        nonlocal x # nonlocal permite que una función interna modifique variables de su función contenedora, pero no globales.
        x = "modified"
        print(f"El valor en inner de x es: {x}")

    inner_function()
    print(f"El valor outer de x es: {x}")

outer_function()