import csv

file_path = 'lectura_y_escritura_archivos/csv/products.csv'
updated_file_path = 'lectura_y_escritura_archivos/csv/updated_products.csv'

with open(file_path, mode='r') as file:
    csv_reader = csv.DictReader(file)
    # Get the names of colums
    field_names = csv_reader.fieldnames + ['total_value']

    with open(updated_file_path, mode='w', newline='') as updated_file:
        csv_writer = csv.DictWriter(updated_file, fieldnames=field_names)
        csv_writer.writeheader() # Write the header

        for row in csv_reader:
            row['total_value'] = float(row['price']) * int(row['quantity'])
            csv_writer.writerow(row)
