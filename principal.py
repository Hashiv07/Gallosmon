from pelea_gallosmon import obtener_atributos_gallosmon, pelea

id_gallosmon1 = 1
id_gallosmon2 = 2
id_gallosmon3 = 3
id_gallosmon4 = 4
id_gallosmon5 = 5
id_gallosmon6 = 6
atributos_gallosmon1 = obtener_atributos_gallosmon(id_gallosmon1)
atributos_gallosmon2 = obtener_atributos_gallosmon(id_gallosmon2)
atributos_gallosmon3 = obtener_atributos_gallosmon(id_gallosmon3)
atributos_gallosmon4 = obtener_atributos_gallosmon(id_gallosmon4)
atributos_gallosmon5 = obtener_atributos_gallosmon(id_gallosmon5)
atributos_gallosmon6 = obtener_atributos_gallosmon(id_gallosmon6)


resultado_pelea = pelea(atributos_gallosmon1, atributos_gallosmon2)

print("\n¡Bienvenido al Mundo Gallosmon!")

print("\n¿Cuál Gallosmon eliges?")

print("\n1- ", atributos_gallosmon1[0])
print("2- ", atributos_gallosmon2[0])
print("3- ", atributos_gallosmon3[0])
print("4- ", atributos_gallosmon4[0])
print("5- ", atributos_gallosmon5[0])
print("6- ", atributos_gallosmon6[0])

eleccion = input("\nElija un número: ")

if eleccion == "1":
    gallosmon_elegido = atributos_gallosmon1
elif eleccion == "2":
    gallosmon_elegido = atributos_gallosmon2
elif eleccion == "3":
    gallosmon_elegido = atributos_gallosmon3
elif eleccion == "4":
    gallosmon_elegido = atributos_gallosmon4
elif eleccion == "5":
    gallosmon_elegido = atributos_gallosmon5
elif eleccion == "6":
    gallosmon_elegido = atributos_gallosmon6
else:
    print("Opción inválida. Se usará el Gallosmon por defecto.")
    gallosmon_elegido = atributos_gallosmon1

#resultado_pelea = pelea(gallosmon_elegido, atributos_gallosmon2)


print("\n-------BATALLA GALLOSMON--------")
print(F"\nNOMBRE/", gallosmon_elegido[0])
print("VIDA/", gallosmon_elegido[4])
print("TIPO/", gallosmon_elegido[1])
print("ATAQUE/", gallosmon_elegido[2])
print("DEFENSA/", gallosmon_elegido[3])
print("\nVS")
print(F"\nNOMBRE/", atributos_gallosmon2[0])
print("VIDA/", atributos_gallosmon2[4])
print("TIPO/", atributos_gallosmon2[1])
print("ATAQUE/", atributos_gallosmon2[2])
print("DEFENSA/", atributos_gallosmon2[3])


print("\nHA INICIADO LA BATALLA")
print(f"\n{gallosmon_elegido[0]} se enfreta a {atributos_gallosmon2[0]}")


if gallosmon_elegido[4] <= 0:
    print("\n GANO ", atributos_gallosmon2[0])
else:  
    print("\n GANO ", gallosmon_elegido[0])



"""print("\nResultado de la pelea:")
print("Gallosmon 1:", resultado_pelea[0])
print("Gallosmon 2:", resultado_pelea[1])"""
