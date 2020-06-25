print("Este programa suma")
print("Introduce dos numeros para hacer la suma")
print ("Presione 'si' para salir")
while True:
    numero1=input("Primer numero:\n")    
    numero2=input("Segundo numero:\n")    
    try:
        k= numero1+numero2
    except TypeError:
        print("No se puede hacer la operacion")
    else:
        print("El resultado de la suma es: "+str(k)) 
    salida= raw_input("Si quiere salir presione 'si' o siga\n")
    if salida=='si':
        break

print("\nPunto 2\n")
print("Lista actual de los gatos:\n")
gatos='gatos.txt'
with open(gatos) as michis:
    lista_gatos=michis.read()
    print (lista_gatos)
i=1
while i<=3:
    t= raw_input("Querido usuario introduzca el nombre del gato "+str(i)+" por favor:\n")
    moncho = 'gatos.txt'
    with open(moncho,'a') as morros:
        morros.write(t+"\n")
    i+=1
print("\nLista final:\n")
gat='gatos.txt'
with open(gat) as mich:
    listafinal=mich.read()
    print (listafinal)

print("\nLista actual de los perros:\n")
perros='perros.txt'
with open(perros) as dog:
    lista_perros=dog.read()
    print (lista_perros)
i=1
while i<=3:
    t= raw_input("Querido usuario introduzca el nombre del perro "+str(i)+" por favor:\n")
    dogi = 'perros.txt'
    with open(dogi,'a') as popos:
        popos.write(t+"\n")
    i+=1
print("\nLista final:\n")
perrr='perros.txt'
with open(perrr) as troka:
    lista_final=troka.read()
    print (lista_final)







