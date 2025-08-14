# Read a file line for line

"""with open('lectura_y_escritura_archivos/txt/caperucita.txt', 'r') as file:
    for lineas in file:
        print(lineas.strip())

# Read all lines in a list
with open('lectura_y_escritura_archivos/txt/caperucita.txt', 'r') as file:
    lines = file.readlines()
    print(lines)

# Add text
with open('lectura_y_escritura_archivos/txt/caperucita.txt', 'a') as file:
    file.write("\n\nBy:ChatGPT")

# overwrite
with open('lectura_y_escritura_archivos/txt/caperucita.txt', 'w') as file:
    file.write("\n\nBy:Hello world")"""

with open('lectura_y_escritura_archivos/txt/caperucita.txt', 'r') as file:
    lineas = file.readlines()
    print(f"Exist {len(lineas)} lineas")