from modulos.scanner import listar_archivos
from modulos.organizador import mover_archivo, cargar_categorias
from datetime import datetime
import os
import sys
from modulos.organizador import obtener_categoria

modo_simulacion = "--simular" in sys.argv
ruta_entradas = "entradas"
ruta_salidas = "salidas"
ruta_log = "logs/registro.txt"

archivos = listar_archivos(ruta_entradas)
try:
    categorias = cargar_categorias()
except FileNotFoundError:
    print("Error: no se encontro config.json")
    sys.exit(1)
except Exception as e:
    print(f"Error al leer config.json: {e}")
    sys.exit(1)

estadisticas = {
    "total": 0,
    "por_categoria": {},
    "duplicados": [],
    "otros": [],
    "errores": []
}

def mostrar_reporte(estadisticas):
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
        print(f"\nErrores: {len(estadisticas['errores'])}")
        for e in estadisticas["errores"]:
            print(f"  - {e}")
        print("=========================")

def organizar(archivos, categorias, ruta_salidas, ruta_log, estadisticas):
    with open(ruta_log, "a", encoding="utf-8") as log:
        for archivo in archivos:
            try:
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
            except Exception as e:
                estadisticas["errores"].append(f"{archivo}: {e}")
                print(f"[ERROR] {archivo}: {e}")
    print("\n Listo.")
    mostrar_reporte(estadisticas)

if not archivos:
    print("No hay archivos en entradas.")

else:
    print("Organizando archivos...\n")
    if modo_simulacion == True:
        for archivo in archivos:
            categoria = obtener_categoria(archivo,categorias)
            print(f" [simulacion] {archivo} --> {categoria} ")
        confirmacion = input("desea continuar?: si/no ").lower()
        if confirmacion == "si":
            organizar(archivos, categorias, ruta_salidas, ruta_log, estadisticas)

        else:
            print("operacion canselada con exito")
    else: 
        organizar(archivos, categorias, ruta_salidas, ruta_log, estadisticas)
