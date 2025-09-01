class Employee:
    def __init__(self, name, *args, **kwargs):
        self.name = name
        self.skills = args
        self.detail = kwargs

    def show_employee(self):
        print(f'Nombre: {self.name}\nHabilidades: {self.skills}\nDetalles:\n{self.show_detail()}')


    def show_detail(self) -> dict:
        details = {}
        for key, value in self.detail.items():
            details[key] = value
        return details

romero = Employee('Pepito', 'Python', 'Java', 'React', age=32, city='Loja')

romero.show_employee()