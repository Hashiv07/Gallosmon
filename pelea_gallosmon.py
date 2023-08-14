from funciones_lectura_escritura import leer_archivo_json

def obtener_atributos_gallosmon(gallo_id):
    gallosmon = leer_archivo_json("Gallomon\personajes.json")
    
    atributos = gallosmon[gallo_id]
    return atributos["nombre"], atributos["tipo"], atributos["base"]["ataque"], atributos["base"]["defensa"], atributos["base"]["vida"]
        
def pelea(gallosmon1, gallosmon2):
    vida1, ataque1, defensa1 = gallosmon1
    vida2, ataque2, defensa2 = gallosmon2
     
    vida1 -= max(0, ataque2 - defensa1)
    vida2 -= max(0, ataque1 - defensa2)
    return [vida1, ataque1, defensa1], [vida2, ataque2, defensa2]


#print(obtener_atributos_gallosmon(1))