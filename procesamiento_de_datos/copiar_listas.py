a = [1,2,3,4,5]
b = a           # b es una referencia a la misma lista que a
print(a)
print(b)
del a[0]        # modifica la lista original (y también afecta a b)
print(id(a))
print(id(b))    # id(a) == id(b), porque apuntan al mismo objeto

# Forma correcta de copiar listas
c = a[:]        # copia superficial de la lista
print(id(a))
print(id(b))
print(f"Esto es C: {id(c)}")  # id(c) != id(a), es una lista nueva
a.append(6)
print(a)        # a fue modificada
print(b)        # b también muestra los cambios porque es la misma lista que a
print(c)        # c se mantiene intacta
