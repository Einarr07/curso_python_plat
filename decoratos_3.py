from functools import wraps

def check_access(required_role: str):
    """Decorator factory to enforce role-based access control."""
    def decorator(func):
        @wraps(func)
        def wrapper(employee: dict, *args, **kwargs):
            if employee.get("role") == required_role:
                return func(employee, *args, **kwargs)
            print(f"Access denied: requires role '{required_role}'.")
        return wrapper
    return decorator

def log_action(func):
    """Decorator to log employee actions."""
    @wraps(func)
    def wrapper(employee: dict, *args, **kwargs):
        print(f"Registering action of {employee['name']}...")
        return func(employee, *args, **kwargs)
    return wrapper

@check_access("admin")
@log_action
def delete_employee(employee: dict):
    """Delete an employee record (only allowed for admins)."""
    print(f"Employee {employee['name']} has been deleted.")

if __name__ == "__main__":
    admin = {"name": "Dominica", "role": "admin"}
    employee = {"name": "Jaime", "role": "employee"}

    delete_employee(admin)     # ✅ Permitido
    #delete_employee(employee)  # ❌ Denegado
