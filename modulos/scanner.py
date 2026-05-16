import os

def listar_archivos(ruta, min_mb=0):
    archivos = []
    for elemento in os.listdir(ruta):
        ruta_completa = os.path.join(ruta, elemento)
        if os.path.isfile(ruta_completa):
            tamanio_mb = os.path.getsize(ruta_completa) / (1024 * 1024)
            if tamanio_mb >= min_mb:
                archivos.append(ruta_completa)
    return archivos