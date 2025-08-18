from collections import defaultdict

def count_products(orders: list[str], pro=None) -> defaultdict:

    # Crea un diccionario con valor por defecto 0
    product_count = defaultdict(int)

    for pro in orders:
        product_count[pro] += 1
    return product_count

orders = ['laptop', 'smart_phone', 'computer', 'head_phone', 'laptop']
count = count_products(orders)
print(count)