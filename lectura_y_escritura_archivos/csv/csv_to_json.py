import csv
import json

data_list = []
with open('lectura_y_escritura_archivos/csv/products.csv', mode='r', newline='') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        data_list.append(row)

with open('lectura_y_escritura_archivos/csv/products_copy.json', mode='w', newline='') as json_file:
    json.dump(data_list,
               json_file,
               indent=4
    )

print("Json created successfully")


