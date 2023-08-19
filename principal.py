from pelea_gallosmon import GallosmonClase
import time

gallosmon = GallosmonClase()
ids_gallosmon = [1, 2, 3, 4, 5, 6]
atributos_gallosmon = []

for id_gallosmon in ids_gallosmon:
    atributos_gallosmon.append(gallosmon.o_a_g(id_gallosmon))

print("\n¡Bienvenido al Mundo Gallosmon!")
time.sleep(3)

print("\n¿Cuál Gallosmon eliges?")
for i, atributos_g in enumerate(atributos_gallosmon):
    print(f"{i+1}- {atributos_g[0]}")

eleccion = input("\nElija un número: ")
try:
    eleccion = int(eleccion)
    if 1 <= eleccion <= len(atributos_gallosmon):
        gallosmon_e = atributos_gallosmon[eleccion - 1]
    else:
        print("Opción inválida. Se usará el Gallosmon por defecto.")
        gallosmon_e = atributos_gallosmon[1]
    time.sleep(3)
except ValueError:
    print("Opción inválida. Se usará el Gallosmon por defecto.")
    gallosmon_e = atributos_gallosmon[1]
    time.sleep(3)

print("\n-------BATALLA GALLOSMON--------")
print(F"\nNOMBRE/{gallosmon_e[0]}")
print("VIDA/", gallosmon_e[4])
print("TIPO/", gallosmon_e[1])
print("ATAQUE/", gallosmon_e[2])
print("DEFENSA/", gallosmon_e[3])
print("\nVS")
print(F"\nNOMBRE/{atributos_gallosmon[1][0]}")
print("VIDA/", atributos_gallosmon[1][4])
print("TIPO/", atributos_gallosmon[1][1])
print("ATAQUE/", atributos_gallosmon[1][2])
print("DEFENSA/", atributos_gallosmon[1][3])

time.sleep(3)

resultado_pelea = gallosmon.pelea(gallosmon_e, atributos_gallosmon[1])

print("\nHA INICIADO LA BATALLA")
print(f"\n{gallosmon_e[0]} se enfrenta a {atributos_gallosmon[1][0]} ...")
time.sleep(5)

print(f"\n{gallosmon_e[0]} ataca a {atributos_gallosmon[1][0]} ...")
time.sleep(5)

print(f"\nEl ataque es muy efectivo !!!...")
time.sleep(5)

print(f"\n{atributos_gallosmon[1][0]} ataca a {gallosmon_e[0]} ...")
time.sleep(5)

print(f"\nEl ataque no es muy efectivo !!!...")

time.sleep(5)

if gallosmon_e[4] <= 0:
    print(f"\nGANO {atributos_gallosmon[1][0]} !!!")
else:  
    print(f"\nGANO {gallosmon_e[0]} !!!")

time.sleep(2)

print("El oponente te pagó $500")

