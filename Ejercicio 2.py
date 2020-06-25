print("Ejercicios: En la carpeta de ArchivosExternos se encuentra un archivo apellidos-es.txt, abrir y leer el archivo, pedir al usuario un nombre y un apellido, el programa debe de buscar en la lista de nombres si el nombre se encuentra, también debe hacer de lo mismo con los apellidos, solo si se localiza el nombre y apellido, la búsqueda será exitosa y deberá mostrar la posición del nombre y la posición del apellido.")
lista_apellidos = 'ArchivosExternos/apellidos-es.txt'
with open(lista_apellidos) as apellidos:
    lanos = apellidos.readlines()
lista_nombres= 'ArchivosExternos/nombres-propios-es.txt'
with open(lista_nombres) as nombres:
    lines= nombres.readlines()
name = raw_input("Introduzca el nombre a buscar:\n")
apellido= raw_input ("Ahora introduzca el apellido:\n")
name_buscar = name + '\n'
apellido_buscar= apellido  + '\n'
found = False
funde= False
for i in range(len(lines)):
    if name_buscar == lines[i]:
        print("\nEl nombre: " + name + " se encontró en la posición: " + str(i)) 
        found = True
        break
if not found:
    print("\nEl nombre no se encuentra en la lista")

for o in range(len(lanos)):
    if apellido_buscar==lanos[o]:
        print("\nEl apellido: " + apellido + " se encontró en la posición: " + str(o))
        funde=True
        break;
if not funde:
    print("\nEl apellido no se encuentra en la lista")
        

print ("Ejercicios: 1.- Cree un programa que se le pida a un usuario su nombre y boleta, guádelo en un archivo llamado usuarios.txt")
print ("2.- Genere un programa que lea 15 usuarios con sus 15 boletas, los datos del usuario y boletas, se deben de agregar al archivo usuarios.txt.")
print ("3.- Genere un programa que una vez que haya leído los 15 usuarios debe de revisar que no haya nombres y boletas repetidas, en caso de ser así, se deben de borrar de la lista y los nombres y boletas resultantes deben de guardarse en un archivo usuarios_filtrados.txt")

print("\nPunto 1:")
l= raw_input("Querido usuario, introduzca su nombre por favor:\n")
k= input("Ahora introduzca su boleta:\n")
usuarios = 'usuarios.txt'
with open(usuarios,"w") as registros:
   registros.write(l+"\n")
   registros.write(str(k)+"\n")

print("\nPunto 2:")
i=1
while i<=15:
    t= raw_input("Querido usuario "+str(i)+": introduzca su nombre por favor:\n")
    p= input("Ahora introduzca su boleta:\n")
    usuarios = 'usuarios.txt'
    with open(usuarios,'a') as circulo:
        circulo.write(t+"\n")
        circulo.write(str(p)+"\n")
    i+=1


print("\nPunto 3:")
input_file='usuarios.txt'
output_file='usuarios.txt'

with open(input_file) as input:
    unique = set(line.rstrip('\n') for line in input.readlines())
with open(output_file, 'w') as output:
    output.write('\n'.join(unique))

import shutil, os
ruta = os.getcwd() + os.sep
origen = ruta + 'usuarios.txt'
destino = ruta + 'usuarios_filtrados.txt'

if os.path.exists(origen):
    with open(origen, 'rb') as forigen:
        with open(destino, 'wb') as fdestino:
            shutil.copyfileobj(forigen, fdestino)
            print("Archivo copiado")

