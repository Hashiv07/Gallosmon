import json
import csv

def leer_archivo_texto(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as archivo:
            contenido = archivo.read()
        return contenido
    except FileNotFoundError:
        print(f"Error: Archivo '{nombre_archivo}' no encontrado.")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None

def leer_archivo_json(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as archivo:
            datos = json.load(archivo)
        return datos
    except FileNotFoundError:
        print(f"Error: Archivo '{nombre_archivo}' no encontrado.")
        return None
    except json.JSONDecodeError as e:
        print(f"Error: Error al decodificar JSON - {e}")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None

def leer_archivo_csv(nombre_archivo, delimitador=','):
    try:
        with open(nombre_archivo, 'r', newline='') as archivo:
            lector = csv.DictReader(archivo, delimiter=delimitador)
            datos = [fila for fila in lector]
        return datos
    except FileNotFoundError:
        print(f"Error: Archivo '{nombre_archivo}' no encontrado.")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None

def exportar_archivo_texto(nombre_archivo, contenido):
    try:
        with open(nombre_archivo, 'w') as archivo:
            archivo.write(contenido)
        print(f"Contenido exportado exitosamente a '{nombre_archivo}'.")
    except Exception as e:
        print(f"Error: {e}")

def exportar_archivo_json(nombre_archivo, datos):
    try:
        with open(nombre_archivo, 'w') as archivo:
            json.dump(datos, archivo, indent=4)
        print(f"Datos exportados exitosamente a '{nombre_archivo}'.")
    except Exception as e:
        print(f"Error: {e}")

def exportar_archivo_csv(nombre_archivo, datos, nombres_campos, delimitador=','):
    try:
        with open(nombre_archivo, 'w', newline='') as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=nombres_campos, delimiter=delimitador)
            escritor.writeheader()
            escritor.writerows(datos)
        print(f"Datos exportados exitosamente a '{nombre_archivo}'.")
    except Exception as e:
        print(f"Error: {e}")