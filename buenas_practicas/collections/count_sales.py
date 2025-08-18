from collections import Counter

def count_products(orders: list[str]) -> Counter:

    # Usa Counter para contar cuántos productos de cada tipo se han vendido
    return Counter(orders)

sales = ['laptop', 'smart_phone', 'computer', 'head_phone', 'laptop', 'head_phone', 'smartPhone']
result = count_products(sales)
print(result)