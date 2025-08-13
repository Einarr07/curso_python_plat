# Definición de la clase BankAccount para representar una cuenta bancaria
class BankAccount:

    # Método constructor para inicializar la cuenta con titular y saldo inicial
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder  # Nombre del titular de la cuenta
        self.balance = balance                # Saldo inicial de la cuenta
        self.is_active = True                  # Estado de la cuenta (activa por defecto)

    # Método para depositar dinero en la cuenta
    def deposit(self, amount):
        if self.is_active:  # Solo permite depósitos si la cuenta está activa
            self.balance += amount
            print(f"Deposit Successful {amount}. Balance: {self.balance}")
        else:
            print("Deposit Failed, account is not active")

    # Método para retirar dinero de la cuenta
    def withdraw(self, amount):
        if self.is_active:  # Solo permite retiros si la cuenta está activa
            if amount <= self.balance:  # Verifica que haya saldo suficiente
                self.balance -= amount
                print(f"Withdraw Successful {amount}. Balance: {self.balance}")

    # Método para desactivar la cuenta
    def deactivate(self):
        self.is_active = False
        print("Deactivate Successful")

    # Método para activar nuevamente la cuenta
    def activate_account(self):
        self.is_active = True
        print("Activate Account Successful")


# --- Ejemplo de uso de la clase ---

# Se crea una cuenta llamada 'chipincha' para el titular "James" con saldo inicial de 300
chipincha = BankAccount("James", 300)

# Depósito de 100 unidades
chipincha.deposit(100)

# Retiro de 10 unidades
chipincha.withdraw(10)

# Se desactiva la cuenta
chipincha.deactivate()

# Se activa la cuenta nuevamente
chipincha.activate_account()

# Se deposita un monto de 800 unidades
chipincha.deposit(800)
