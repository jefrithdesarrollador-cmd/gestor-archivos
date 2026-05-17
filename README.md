<div align="center">

# 📁 File Organizer

**Herramienta de automatización en Python para organizar archivos de forma inteligente, segura y configurable.**

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python)
![License](https://img.shields.io/badge/Licencia-Personal-green?style=for-the-badge)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey?style=for-the-badge)

</div>

---

## 🧩 ¿Qué hace?

Elimina el caos en carpetas con archivos acumulados. Clasifica por extensión, renombra duplicados, registra cada operación y puede revertir cualquier cambio — sin perder ningún archivo.

---

## ✅ Características

- 📂 Organización automática por extensión mediante categorías configurables
- 🔁 Soporte completo para subcarpetas
- 🔢 Renombrado inteligente de duplicados (`archivo_1.jpg`, `archivo_2.jpg`)
- 👁️ Modo simulación: previsualiza los cambios antes de ejecutarlos
- 🔇 Modo silencioso: muestra únicamente el reporte final
- ⚖️ Filtro por tamaño mínimo en MB
- ↩️ Deshacer: revierte la última ejecución usando el historial de logs
- 📋 Registro detallado de cada operación con timestamp
- 📊 Reporte final con estadísticas completas
- 🛡️ Manejo de errores: JSON inválido, archivos bloqueados, permisos insuficientes
- 🎨 Colores en terminal para mejor legibilidad

---

## ⚙️ Requisitos

- Python 3.10 o superior

### Dependencias

```bash
pip install colorama
```

---

## 🚀 Instalación

```bash
git clone https://github.com/jefrithdesarrollador-cmd/gestor-archivos.git
cd gestor-archivos
pip install colorama
```

---

## 💻 Uso

### Organización estándar

```bash
python main.py
```

### 👁️ Simular antes de ejecutar

```bash
python main.py --simular
```

Muestra qué archivos serán movidos y solicita confirmación antes de realizar cualquier cambio.

### 🔇 Modo silencioso

```bash
python main.py --quiet
```

Suprime el detalle de cada archivo y muestra únicamente el reporte final.

### ⚖️ Filtrar por tamaño

```bash
python main.py --min-mb 10
```

Solo organiza archivos con un peso mayor a 10 MB.

### ↩️ Deshacer la última ejecución

```bash
python main.py --deshacer
```

Restaura todos los archivos de la última sesión a su ubicación original.

---

## 🚩 Flags disponibles

| Flag | Descripción |
|---|---|
| `--simular` | Previsualiza movimientos y solicita confirmación |
| `--quiet` | Muestra únicamente el reporte final |
| `--deshacer` | Revierte la última sesión |
| `--min-mb N` | Filtra archivos menores a N megabytes |

Los flags son combinables:

```bash
python main.py --simular --min-mb 5
```
---

## 💡 Uso avanzado

### 1. Usar las carpetas internas del proyecto

Organiza archivos desde `entradas/` y los mueve a `salidas/`:

```bash
python main.py
```

---

### 2. Organizar una carpeta relativa del usuario

Permite organizar carpetas dentro del directorio del usuario actual.
El script interpreta automáticamente la ruta como `C:\Users\TU_USUARIO\<carpeta>`:

```bash
python main.py Documents
python main.py Desktop
python main.py Downloads
```

---

### 3. Organizar una ruta absoluta

Cualquier carpeta del sistema usando rutas completas:

```bash
python main.py "D:\Proyectos"
python main.py "C:\Users\jefri\OneDrive\Documentos"
python main.py "/home/user/downloads"
```

---

### Combinando modos con flags

Los flags funcionan en cualquiera de los tres modos anteriores:

```bash
python main.py Downloads --simular
python main.py "D:\Proyectos" --quiet
python main.py Downloads --min-mb 100
python main.py --deshacer
```
---

## 🔧 Configuración

Las categorías y extensiones se definen en `config.json`. No se requiere modificar el código.

```json
{
    "categorias": {
        "imagenes": [".jpg", ".jpeg", ".png", ".gif", ".webp"],
        "videos": [".mp4", ".avi", ".mov", ".mkv"],
        "documentos": [".pdf", ".docx", ".doc", ".txt", ".xlsx"],
        "audio": [".mp3", ".wav", ".aac", ".lrc"],
        "libros": [".epub"],
        "otros": []
    }
}
```

Para agregar una nueva categoría:

```json
"codigo": [".py", ".js", ".html", ".css"]
```

---

## 📋 Sistema de logs

Cada ejecución queda registrada en `logs/registro.txt`:

```
=== SESION 2026-05-17 18:22:01 ===
2026-05-17 18:22:01 | entradas\video.mp4 → salidas\videos\video.mp4
2026-05-17 18:22:01 | entradas\foto.jpg → salidas\imagenes\foto.jpg
=== FIN SESION ===
```

---

## 📊 Reporte final

```
===== REPORTE FINAL =====
Total archivos procesados: 12

Por categoría:
  videos: 5
  audio: 4
  documentos: 2
  libros: 1

Duplicados renombrados: 2
  - video.mp4
  - foto.jpg

Archivos en 'otros': 0
Errores: 0
=========================
```

---

## 🗂️ Estructura del proyecto

```
gestor-archivos/
│
├── 📄 main.py
├── ⚙️ config.json
├── 🚫 .gitignore
├── 📖 README.md
│
├── 📥 entradas/
├── 📤 salidas/
│
├── 📋 logs/
│   └── registro.txt
│
└── 🧩 modulos/
    ├── __init__.py
    ├── scanner.py
    └── organizador.py
```

---

## 🌐 Compatibilidad

| Sistema operativo | Compatible |
|---|---|
| Windows | ✅ |
| Linux | ✅ |
| macOS | ✅ |

---

## 🔮 Futuras mejoras

- 🖥️ Interfaz gráfica de escritorio
- 👁️ Monitoreo automático de carpetas en tiempo real
- 📄 Exportación de reportes en HTML y PDF
- 💾 Sistema de backups antes de cada ejecución
- 🤖 Clasificación con inteligencia artificial
- ☁️ Integración con almacenamiento en la nube

---

## 👨‍💻 Autor

<div align="center">

**Jefrith Madariaga**  
Desarrollador de software especializado en automatización y herramientas con Python.  
Orientado a soluciones prácticas para clientes remotos y proyectos freelance.

[![GitHub](https://img.shields.io/badge/GitHub-jefrithdesarrollador--cmd-black?style=for-the-badge&logo=github)](https://github.com/jefrithdesarrollador-cmd)

</div>

---

## 📜 Licencia

Proyecto de uso libre para fines personales y educativos.
