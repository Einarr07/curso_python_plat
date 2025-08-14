import csv

#with open('lectura_y_escritura_archivos/products.csv', mode='r') as file:
#    csv_reader = csv.DictReader(file)
#    for row in csv_reader:
#        print(row)

# Show colums information
with open('lectura_y_escritura_archivos/csv/products.csv', mode='r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        print(f"Produto {row['name']}, Precio: {row['price']}")