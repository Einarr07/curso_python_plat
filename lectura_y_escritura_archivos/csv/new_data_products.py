import csv

new_product = {
    "name": "Wireless Charger",
     "price": 80,
    "quantity": 40,
    "brand": "ChargerMaster",
    "category": "Electronics",
    "entry_date": "2024-07-01"
}

with open('lectura_y_escritura_archivos/csv/products.csv', mode='a', newline='') as file:
    file.write("\n")
    csv_writer = csv.DictWriter(file, fieldnames=new_product.keys())
    csv_writer.writerow(new_product)