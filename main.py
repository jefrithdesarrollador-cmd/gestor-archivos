from modulos.scanner import listar_archivos
from modulos.organizador import mover_archivo, cargar_categorias
from datetime import datetime
import os

ruta_entradas = "entradas"
ruta_salidas = "salidas"
ruta_log = "logs/registro.txt"

archivos = listar_archivos(ruta_entradas)
categorias = cargar_categorias()
estadisticas = {
    "total": 0,
    "por_categoria": {},
    "duplicados": [],
    "otros": [],
    "errores": []
}

if not archivos:
    print("No hay archivos en entradas.")
else:
    print("Organizando archivos...\n")
    with open(ruta_log, "a", encoding="utf-8") as log:
        for archivo in archivos:
            nombre_final, categoria = mover_archivo(archivo, ruta_salidas, categorias)
            estadisticas["total"] += 1
            estadisticas["por_categoria"][categoria] = estadisticas["por_categoria"].get(categoria, 0) + 1
            nombre_original = os.path.basename(archivo)
            if nombre_original != nombre_final:
                estadisticas["duplicados"].append(nombre_original)
            if categoria == "otros":
                estadisticas["otros"].append(nombre_final)
            linea = f"{datetime.now()} | {archivo} → {categoria} -> {nombre_final} \n"
            print(linea.strip())
            log.write(linea)
    print("\nListo.")
    print("\n===== REPORTE FINAL =====")
    print(f"Total archivos procesados: {estadisticas['total']}")
    print("\nPor categoría:")
    for cat, cantidad in estadisticas["por_categoria"].items():
        print(f"  {cat}: {cantidad}")
    print(f"\nDuplicados renombrados: {len(estadisticas['duplicados'])}")
    for d in estadisticas["duplicados"]:
        print(f"  - {d}")
    print(f"\nArchivos en 'otros': {len(estadisticas['otros'])}")
    for o in estadisticas["otros"]:
        print(f"  - {o}")
    print("=========================")