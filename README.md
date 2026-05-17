## 💻 Uso

El script puede trabajar de tres maneras distintas dependiendo de la ruta proporcionada.

---

### 📁 1. Usar las carpetas internas del proyecto

Organiza archivos desde:

```text
entradas/
```

y los mueve automáticamente a:

```text
salidas/
```

Ejecutar:

```bash
python main.py
```

---

### 🏠 2. Organizar una carpeta relativa del usuario

Permite organizar carpetas dentro del directorio del usuario actual.

Ejemplos:

```bash
python main.py Documents
```

```bash
python main.py Desktop
```

```bash
python main.py Downloads
```

El script interpretará automáticamente la ruta como:

```text
C:\Users\TU_USUARIO\
```

---

### 🌐 3. Organizar cualquier ruta absoluta

También es posible organizar carpetas ubicadas en cualquier parte del sistema.

Ejemplos:

```bash
python main.py "D:\Proyectos"
```

```bash
python main.py "C:\Users\jefri\OneDrive\Documentos"
```

```bash
python main.py "/home/user/downloads"
```

---

## 👁️ Simular antes de ejecutar

```bash
python main.py --simular
```

Muestra qué archivos serán movidos y solicita confirmación antes de realizar cualquier cambio.

---

## 🔇 Modo silencioso

```bash
python main.py --quiet
```

Suprime el detalle de cada archivo y muestra únicamente el reporte final.

---

## ⚖️ Filtrar por tamaño

```bash
python main.py --min-mb 10
```

Solo organiza archivos con un peso mayor a 10 MB.

---

## ↩️ Deshacer la última ejecución

```bash
python main.py --deshacer
```

Restaura todos los archivos de la última sesión a su ubicación original.

---

## 🔗 Uso combinado con flags

Los flags funcionan en cualquiera de los modos anteriores.

### Simulación + filtro por tamaño

```bash
python main.py Downloads --simular --min-mb 5
```

### Ruta absoluta + modo silencioso

```bash
python main.py "D:\Proyectos" --quiet
```