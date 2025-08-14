import json

# Read the file
with open('lectura_y_escritura_archivos/json/products.json', mode='r') as json_file:
    products = json.load(json_file)

# Show content
for product in products:
    #print(product)
    print(f"Product name: {product['name']}, price: {product['price']}")