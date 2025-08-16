x = 5

def modify_global():
    global x
    x += 1
    print(f"El valor de x es: {x}")

modify_global()