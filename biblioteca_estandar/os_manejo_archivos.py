import os

cwd = os.getcwd()
target_dir = os.path.join(cwd, "biblioteca_estandar")

print(f"Directory : {target_dir}")

#txt_files = []
#for f in os.listdir(target_dir)
#   if f.endwish('.txt')
#       txt_files.append(f)
txt_files = [f for f in os.listdir(target_dir) if f.endswith(".txt")]

if not txt_files:
    with open(os.path.join(target_dir,"archivo.txt"), "w") as file:
        file.write("")
    txt_files.append("archivo.txt")
    print(f"Se creo el archivo con éxito")

print(f"Files : {txt_files}")

old_name = os.path.join(target_dir, txt_files[0])
new_name = os.path.join(target_dir, 'renombre.txt')

os.rename(old_name, new_name)

print(f"Archivo renombrado: {old_name} -> {new_name}")