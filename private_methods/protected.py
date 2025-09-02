class BaseClass:
    def __init__(self) -> None:
        # Variable protegida: se indica con un solo guion bajo (_).
        # Convención: no debería ser usada fuera de la clase o de sus subclases.
        # PERO en realidad Python no lo impide, es solo una "convención".
        self._protected_variable = 'Protected variable'

        # Variable privada: se indica con doble guion bajo (__).
        # Python aplica *name mangling*, es decir, internamente la variable se renombra
        # a _NombreDeClase__nombre_variable. Esto dificulta (pero no impide) el acceso
        # directo desde fuera de la clase.
        self.__private_variable = 'Private variable'

    # Método protegido: mismo concepto que la variable protegida,
    # se debería usar solo dentro de la clase y subclases.
    def _protected_methods(self):
        print(f"This is a protected method with one variable: {self._protected_variable}")

    # Método privado: solo debería usarse dentro de la misma clase.
    # Python renombra el método con *name mangling* para evitar accesos accidentales.
    def __private_method(self):
        print(f"This is a private method with one variable: {self.__private_variable}")

    # Método público: es accesible desde cualquier parte del código.
    # Aquí, aunque sea público, puede llamar a un método privado interno.
    def public_method(self):
        self.__private_method()


# Instancia de la clase
base = BaseClass()

# Acceso a variable protegida:
# Aunque por convención no deberías hacerlo, se puede acceder directamente.
# print(base._protected_variable)

# Llamada a método protegido:
# También accesible, aunque no es recomendado fuera de la clase/subclase.
# base._protected_methods()

# Llamada a método público:
# Recomendado. Puede internamente usar métodos privados.
# base.public_method()

# Acceso a variable privada directamente:
# Esto da error porque Python la renombró internamente.
print(base.__private_variable)  # ❌ AttributeError
# Si realmente quisieras acceder (NO recomendado), tendrías que hacerlo así:
# print(base._BaseClass__private_variable)  # ✅ funciona por name mangling
