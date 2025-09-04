from packages.inventory import add_product, delete_product
from packages.sales import process_sale

if __name__ == '__main__':
    add_product('Laptop', 10)
    delete_product('Laptop')
    process_sale('Laptop', 2)