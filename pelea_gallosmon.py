from funciones_lectura_escritura import leer_archivo_json
GALLOSMON = leer_archivo_json("Gallomon\personajes.json")

def obtener_atributos_gallosmon(gallo_id):
    for gallomon in GALLOSMON:
        if gallomon["id"] == gallo_id:
            atributos = gallomon
    
    nombre = atributos["nombre"]
    tipo = atributos["tipo"]
    ataque = atributos["base"]["ataque"]
    defensa = atributos["base"]["defensa"]
    vida = atributos["base"]["vida"]
    
    return nombre, tipo, ataque, defensa, vida
        
def pelea(gallosmon1, gallosmon2):
    nombre1, tipo1, ataque1, defensa1, vida1 = gallosmon1
    nombre2, tipo2, ataque2, defensa2, vida2 = gallosmon2
     
    vida1 -= max(0, ataque2 - defensa1)
    vida2 -= max(0, ataque1 - defensa2)
    return [nombre1, tipo1, ataque1, defensa1, vida1], [nombre2, tipo2, ataque2, defensa2, vida2]


#print(obtener_atributos_gallosmon(1))
