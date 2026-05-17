import os

def listar_archivos(ruta, min_mb=0):
    archivos = []
    for carpeta, subcarpetas, ficheros in os.walk(ruta):
        for fichero in ficheros:
            ruta_completa = os.path.join(carpeta, fichero)
            tamanio_mb = os.path.getsize(ruta_completa) / (1024 * 1024)
            if tamanio_mb >= min_mb:
                archivos.append(ruta_completa)
    return archivos