# Clase que representa un libro
class Book:
    def __init__(self, title, author):
        self.title = title            # Título del libro
        self.author = author          # Autor del libro
        self.available = True         # Estado de disponibilidad (True = disponible)

    # Método para prestar un libro
    def borrow(self):
        if self.available:
            self.available = False
            print(f"📚 Prestando el libro: '{self.title}'")
        else:
            print(f"❌ El libro '{self.title}' no está disponible para préstamo.")

    # Método para devolver un libro
    def return_book(self):
        self.available = True
        print(f"✅ El libro '{self.title}' ha sido devuelto y está disponible nuevamente.")


# Clase que representa a un usuario
class User:
    def __init__(self, name, user_id):
        self.name = name                  # Nombre del usuario
        self.user_id = user_id             # Identificador único del usuario
        self.borrowed_books = []           # Lista de libros prestados

    # Método para que un usuario tome prestado un libro
    def borrow_book(self, book):
        if book.available:
            book.borrow()
            self.borrowed_books.append(book)
            print(f"👤 {self.name} ha tomado prestado: '{book.title}'")
        else:
            print(f"⚠️ Lo sentimos {self.name}, el libro '{book.title}' no está disponible.")

    # Método para que un usuario devuelva un libro
    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
            print(f"🔄 {self.name} ha devuelto: '{book.title}'")
        else:
            print(f"⚠️ {self.name} no tiene registrado el libro '{book.title}' como prestado.")


# Clase que representa la biblioteca
class Library:
    def __init__(self):
        self.books = []   # Lista de libros disponibles en la biblioteca
        self.users = []   # Lista de usuarios registrados

    # Agregar un libro a la biblioteca
    def add_book(self, book):
        self.books.append(book)
        print(f"📗 Se ha agregado el libro: '{book.title}' de {book.author}")

    # Registrar un usuario en la biblioteca
    def add_user(self, user):
        self.users.append(user)
        print(f"👤 Se ha registrado el usuario: {user.name} (ID: {user.user_id})")

    # Mostrar libros disponibles
    def show_available_books(self):
        print("\n📚 Libros disponibles en la biblioteca:")
        disponibles = [f"  - '{book.title}' de {book.author}" for book in self.books if book.available]
        if disponibles:
            print("\n".join(disponibles))
        else:
            print("  No hay libros disponibles en este momento.")


# ------------------ Creación de objetos ------------------

# Libros
book = Book("How to Learn Programming with Python", "Allen Downey, Jeffrey Elkner, Chris Meyers")
book1 = Book("El dios humeante", "Willis George Emerson")
book3 = Book("Las 4 puertas", "Jorge Benito")
book4 = Book("El santuario en la tierra", "Sixto Paz")

# Usuarios
user = User("James Clear", "2")
user2 = User("Sun Tzu", "4")
user3 = User("Fernando Savater", "5")
user4 = User("Joshua Pazkiewicz", "6")

# Biblioteca
library = Library()

# Agregar libros
library.add_book(book)
library.add_book(book1)
library.add_book(book3)
library.add_book(book4)

# Agregar usuarios
library.add_user(user)
library.add_user(user2)
library.add_user(user3)
library.add_user(user4)

# Mostrar libros disponibles
library.show_available_books()

# Préstamo de libro
user.borrow_book(book3)

# Mostrar libros después del préstamo
library.show_available_books()

# Devolución de libro
user.return_book(book3)

# Mostrar libros después de la devolución
library.show_available_books()
