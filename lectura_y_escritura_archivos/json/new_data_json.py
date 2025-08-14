import json

file_path = 'lectura_y_escritura_archivos/json/products.json'

new_product = {
    "name": "Wireless Charger",
     "price": 80,
    "quantity": 40,
    "brand": "ChargerMaster",
    "category": "Electronics",
    "entry_date": "2025-09-25"
}

with open(file_path, mode='r') as json_file:
    products = json.load(json_file)

products.append(new_product)

with open(file_path, mode='w') as json_file:
    json.dump(products, json_file, indent=4)