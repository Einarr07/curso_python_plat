import json
import csv

with open('lectura_y_escritura_archivos/json/products.json', mode='r') as json_file:
    products = json.load(json_file)

with open('lectura_y_escritura_archivos/json/products_copy.csv', mode='w', newline='') as csv_file:
    filenames = products[0].keys()

    writer = csv.DictWriter(csv_file, fieldnames=filenames)

    writer.writeheader()

    for data in products:
        writer.writerow(data)

print("Archivo csv creado con exito.")