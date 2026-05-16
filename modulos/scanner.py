import os

def listar_archivos(ruta):
    archivos = []
    for elemento in os.listdir(ruta):
        ruta_completa = os.path.join(ruta, elemento)
        if os.path.isfile(ruta_completa):
            archivos.append(ruta_completa)
    return archivos