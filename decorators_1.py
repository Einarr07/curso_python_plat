def log_transaction(func):

    def wrapper():
        print('1 Logging transaction...')
        func()
        print('3 Log ending')
    return wrapper

@log_transaction
def process_payment():
    print('2 Processing Payment...')

process_payment()


