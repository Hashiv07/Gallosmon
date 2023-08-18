from pelea_gallosmon import GallosmonClase
import time

gallosmon = GallosmonClase()
idg1 = 1     #id_gallosmon1
idg2 = 2
idg3 = 3
idg4 = 4
idg5 = 5
idg6 = 6
atributos_g1 = gallosmon.o_a_g(idg1)   #atributos_gallosmon1
atributos_g2 = gallosmon.o_a_g(idg2)
atributos_g3 = gallosmon.o_a_g(idg3)
atributos_g4 = gallosmon.o_a_g(idg4)
atributos_g5 = gallosmon.o_a_g(idg5)
atributos_g6 = gallosmon.o_a_g(idg6)

resultado_pelea = gallosmon.pelea(atributos_g1, atributos_g2)

print("\n¡Bienvenido al Mundo Gallosmon!")
time.sleep(3)

print("\n¿Cuál Gallosmon eliges?")

print("\n1- ", atributos_g1[0])
print("2- ", atributos_g2[0])
print("3- ", atributos_g3[0])
print("4- ", atributos_g4[0])
print("5- ", atributos_g5[0])
print("6- ", atributos_g6[0])


eleccion = input("\nElija un número: ")

try:
    eleccion = int(eleccion)
    if eleccion == 1:
        gallosmon_e = atributos_g1    #gallosmon_elegido
    elif eleccion == 2:
        gallosmon_e = atributos_g2
    elif eleccion == 3:
        gallosmon_e = atributos_g3
    elif eleccion == 4:
        gallosmon_e = atributos_g4
    elif eleccion == 5:
        gallosmon_e = atributos_g5
    elif eleccion == 6:
        gallosmon_e = atributos_g6
    else:
        print("Opción inválida. Se usará el Gallosmon por defecto.")
        gallosmon_e = atributos_g1

    time.sleep(3)
    
except ValueError:
        print("Opción inválida. Se usará el Gallosmon por defecto.")
        gallosmon_e = atributos_g1
        time.sleep(3)


print("\n-------BATALLA GALLOSMON--------")
print(F"\nNOMBRE/", gallosmon_e[0])
print("VIDA/", gallosmon_e[4])
print("TIPO/", gallosmon_e[1])
print("ATAQUE/", gallosmon_e[2])
print("DEFENSA/", gallosmon_e[3])
print("\nVS")
print(F"\nNOMBRE/", atributos_g2[0])
print("VIDA/", atributos_g2[4])
print("TIPO/", atributos_g2[1])
print("ATAQUE/", atributos_g2[2])
print("DEFENSA/", atributos_g2[3])

time.sleep(3)

print("\nHA INICIADO LA BATALLA")
print(f"\n{gallosmon_e[0]} se enfreta a {atributos_g2[0]} ...")
time.sleep(5)

print(f"\n{gallosmon_e[0]} ataca a {atributos_g2[0]} ...")
time.sleep(5)

print(f"\nEl ataque es muy efectivo !!!...")
time.sleep(5)

print(f"\n{atributos_g2[0]} ataca a {gallosmon_e[0]} ...")
time.sleep(5)

print(f"\nEl ataque no es muy efectivo !!!...")

time.sleep(5)

if gallosmon_e[4] <= 0:
    print(f"\nGANO {atributos_g2[0]} !!!")
else:  
    print(f"\nGANO {gallosmon_e[0]} !!!")

time.sleep(2)

print("El oponente te pagó $500")

