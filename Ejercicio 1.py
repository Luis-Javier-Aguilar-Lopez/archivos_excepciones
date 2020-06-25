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
        




