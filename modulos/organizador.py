import os
import shutil
import json

def cargar_categorias():
    ruta_base = os.path.dirname(os.path.abspath(__file__))
    ruta_config = os.path.normpath(os.path.join(ruta_base, "..", "config.json"))
    with open(ruta_config, "r", encoding="utf-8") as f:
        datos = json.load(f)
    return datos["categorias"]


def obtener_categoria(archivo, categorias):
    _, extension = os.path.splitext(archivo)
    extension = extension.lower()
    for categoria, extensiones in categorias.items():
        if extension in extensiones:
            return categoria
    return "otros"

def mover_archivo(archivo, ruta_salida, categorias):
    categoria = obtener_categoria(archivo, categorias)
    destino = os.path.join(ruta_salida, categoria)
    os.makedirs(destino, exist_ok=True)

    nombre_archivo = os.path.basename(archivo)
    nombre, extension = os.path.splitext(nombre_archivo)
    ruta_final = os.path.join(destino, nombre_archivo)

    contador = 1
    while os.path.exists(ruta_final):
        nuevo_nombre = f"{nombre}_{contador}{extension}"
        ruta_final = os.path.join(destino, nuevo_nombre)
        contador += 1

    shutil.move(archivo, ruta_final)
    return os.path.basename(ruta_final), categoria
