# 📊 Sistema de Análisis de Gastos Hormiga

## Descripción del Proyecto

Este es un sistema de análisis de datos desarrollado como proyecto de formación en **Técnico Laboral en Desarrollo de Software** del **CESDE**.

La aplicación permite cargar, limpiar y analizar datos de gastos personales de usuarios, respondiendo preguntas clave mediante operaciones de:
- **Filtrado y agrupación** de datos
- **Cálculo de estadísticas** (suma, promedio, conteo)
- **Fusión (merge)** de múltiples fuentes de datos

### Características Principales

✅ **Carga de datos** desde archivos CSV
✅ **Limpieza automática** de datos sucios (valores nulos, espacios extras, inconsistencias)
✅ **Estandarización de texto** (minúsculas, eliminación de espacios)
✅ **Eliminación de símbolos monetarios** y conversión a números
✅ **Análisis de frecuencia, agregación y filtrado**
✅ **Fusión de tablas** (merge) entre usuarios y gastos
✅ **Estructura modular** para fácil mantenimiento

---

## Requisitos Previos

- **Python 3.8+** instalado
- **pip** (gestor de paquetes de Python)
- **Git** instalado (para control de versiones)

---

## Configuración del Entorno Virtual

### En Windows (CMD o PowerShell)

```bash
# 1. Crear el entorno virtual
python -m venv venv

# 2. Activar el entorno virtual
venv\Scripts\activate

# 3. Instalar dependencias
pip install -r requirements.txt
```

### En Linux/Mac

```bash
# 1. Crear el entorno virtual
python3 -m venv venv

# 2. Activar el entorno virtual
source venv/bin/activate

# 3. Instalar dependencias
pip install -r requirements.txt
```

---

## Estructura del Proyecto

```
Proyecto_H/
├── data/
│   └── raw/
│       ├── usuarios.csv              # Datos de usuarios
│       └── gastos_hormiga.csv  # Datos de gastos
├── src/
│   ├── __init__.py
│   ├── main.py                       # Punto de entrada principal
│   ├── analisis.py                   # Script de análisis de datos
│   ├── limpiar.py                    # Módulo de limpieza de datos
│   ├── carga.py                      # Módulo de carga de datos
│   ├── datos.py                      # Estructuras de datos
│   └── gastos.py                     # Funciones de gastos
├── documento/
│   └── documento.pdf                 # Documentación del proyecto
├── requirements.txt                  # Dependencias del proyecto
├── README.md                         # Este archivo
└── .gitignore                        # Archivos ignorados por Git
```

---

## Cómo Ejecutar el Proyecto

### Opción 1: Ejecutar directamente

```bash
# Desde la raíz del proyecto
python src/main.py
```

### Opción 2: Ejecutar análisis específico

```bash
# Ejecutar solo el análisis
python src/analisis.py
```

---

## Funcionalidades del Sistema

### 1. Carga de Datos
- Carga automática desde archivos CSV
- Validación de archivos existentes
- Manejo de errores de carga

### 2. Limpieza de Datos
- Eliminación de valores nulos
- Estandarización de texto (minúsculas, espacios)
- Limpieza de símbolos monetarios
- Eliminación de duplicados

### 3. Análisis de Datos

#### Pregunta 1: Análisis de Frecuencia
¿Cuál es la categoría con la mayor cantidad de transacciones?

#### Pregunta 2: Análisis de Agregación
¿Cuál es el monto total de gastos por usuario?

#### Pregunta 3: Análisis de Filtrado y Conteo
¿Cuántos gastos hay por cada medio de pago?

### 4. Análisis Complementario
- Estadísticas descriptivas de montos
- Conteo de usuarios activos
- Categoría que genera más ingresos

---

## Tecnologías Utilizadas

- **Python 3.8+**: Lenguaje de programación principal
- **Pandas**: Manipulación y análisis de datos
- **NumPy**: Operaciones numéricas
- **Git**: Control de versiones
- **Virtualenv**: Entornos virtuales

---

## Control de Versiones (Git Flow)

El proyecto utiliza Git Flow para el control de versiones:

### Ramas principales:
- `main`: Rama de producción
- `develop`: Rama de desarrollo

### Ramas auxiliares:
- `feature/*`: Nuevas funcionalidades
- `hotfix/*`: Corrección de bugs en producción

---

## Documentación

La documentación completa del proyecto se encuentra en `documento/documento.pdf`.

---

## Autor

Proyecto desarrollado como parte del programa **Técnico Laboral en Desarrollo de Software** del **CESDE**.

---

## Licencia

Este proyecto es de uso educativo y no tiene restricciones de licencia.

### Error: "ModuleNotFoundError: No module named 'pandas'"
```bash
# Solución: Asegúrate que el venv está activado
# Windows: venv\Scripts\activate
# Linux/Mac: source venv/bin/activate

# Luego instala las dependencias
pip install -r requirements.txt
```

### Error: "FileNotFoundError" al cargar CSV
- Verifica que el archivo existe en `data/raw/`
- Asegúrate de ejecutar `analisis.py` desde la carpeta `src/`

### El DataFrame está vacío
- Verifica que el archivo CSV no está corrupto
- Abre el archivo con un editor de texto para verificar el contenido

---

## Conocimiento Teórico

### ¿Qué es un DataFrame?
Un **DataFrame** es una estructura de datos bidimensional (como una tabla) similar a un:
- Hoja de cálculo en Excel
- Tabla en SQL
- Matriz con índices nombrados

```python
import pandas as pd

# Crear un DataFrame
df = pd.DataFrame({
    'nombre': ['Ana', 'Juan', 'María'],
    'gasto': [4500, 2800, 5000]
})
```

### ¿Por qué usamos Entornos Virtuales?
Los entornos virtuales (`venv`) permiten:
- ✅ Aislar las dependencias del proyecto
- ✅ Evitar conflictos entre versiones de librerías
- ✅ Facilitar la reproducibilidad en otros equipos
- ✅ Mantener el sistema Python limpio
- ✅ Proyectos independientes con sus propias versiones

---

## Evaluación (Momento 2)

### Conocimiento ✅
- [x] Explicación de DataFrame
- [x] Importancia de entornos virtuales
- [x] Uso de Pandas

### Desempeño ✅
- [x] Instalación correcta de librerías
- [x] Gestión de dependencias en `requirements.txt`
- [x] Uso de funciones modulares

### Producto ✅
- [x] Script sin errores de sintaxis
- [x] Ejecución exitosa
- [x] Estructura Git Flow correcta
- [x] Datos sucios y limpieza documentada

---

## Autor

**Estudiante**: [Tu Nombre]  
**Institución**: CESDE - Técnico Laboral en Desarrollo de Software  
**Fecha**: Abril 2024  
**Versión**: 1.0

---

## Licencia

Este proyecto es de carácter educativo y es libre de usar para fines académicos.

---

**¿Preguntas o problemas?** Consulta el código fuente o contáctame. 😊
