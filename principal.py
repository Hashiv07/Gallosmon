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


resultado_pelea = pelea(atributos_gallosmon1[2:], atributos_gallosmon2[2:], atributos_gallosmon3[2:], atributos_gallosmon4[2:], atributos_gallosmon5[2:], atributos_gallosmon6[2:])

print("¡Bienvenido al Mundo Gallosmon!")

print("¿Cuál Gallosmon eliges?\n")

print("1- ", atributos_gallosmon1[0])
print("2- ", atributos_gallosmon2[0])
print("3- ", atributos_gallosmon3[0])
print("4- ", atributos_gallosmon4[0])
print("5- ", atributos_gallosmon5[0])
print("6- \n", atributos_gallosmon6[0])


print("-------BATALLA GALLOSMON--------")
print(F"\nNOMBRE/", atributos_gallosmon1[0])
print("VIDA/", atributos_gallosmon1[4])
print("TIPO/", atributos_gallosmon1[1])
print("ATAQUE/", atributos_gallosmon1[2])
print("DEFENSA/", atributos_gallosmon1[3])
print("\nVS")
print(F"\nNOMBRE/", atributos_gallosmon2[0])
print("VIDA/", atributos_gallosmon2[4])
print("TIPO/", atributos_gallosmon2[1])
print("ATAQUE/", atributos_gallosmon2[2])
print("DEFENSA/", atributos_gallosmon2[3])





print("\nResultado de la pelea:")
print("Gallosmon 1:", resultado_pelea[0])
print("Gallosmon 2:", resultado_pelea[1])

