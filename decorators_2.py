def check_access(func):

    def wrapper(employee):
        # Comproved if the employee have role 'admin'
        if employee.get('role') == 'admin':
            return func(employee)
        else:
            return print('Access denied, only the administrator can access.')

    return wrapper

@check_access
def delete_employee(employee: dict):
    print(f'Employee {employee["name"]} deleted.')

admin = {'role': 'admin', 'name': 'Hernesto'}
employee = {'role': 'employee', 'name': 'María'}

delete_employee(admin)
delete_employee(employee)
