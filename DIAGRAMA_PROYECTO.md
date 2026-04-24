# 📊 Visualización del Proyecto

## Flujo de Datos

```
┌─────────────────────────────────────────────────────────────┐
│                   PROYECTO_H ANALISIS                        │
└─────────────────────────────────────────────────────────────┘

                    ┌───────────┐
                    │  Usuarios │  100 registros
                    │  (CSV)    │  SUCIOS
                    └─────┬─────┘
                          │
                          ▼
          ┌──────────────────────────────┐
          │   LIMPIEZA (limpiar.py)      │
          │  - manejar_valores_nulos()   │
          │  - estandarizar_texto()      │
          │  - eliminar_duplicados()     │
          └──────────────┬───────────────┘
                          │
                          ▼
                    ┌───────────┐
                    │ Usuarios  │  100 registros
                    │  LIMPIOS  │  (Sin cambios)
                    └─────┬─────┘
                          │
              ┌───────────┴────────────┐
              │                        │
              ▼                        ▼
     ┌──────────────┐         ┌──────────────┐
     │  Gastos CSV  │         │   MERGE()    │
     │ 106 SUCIOS   │◄────────┘              │
     └──────┬───────┘                        │
            │                                │
            ▼                                │
┌──────────────────────────────┐             │
│   LIMPIEZA (limpiar.py)      │             │
│  - manejar_valores_nulos()   │             │
│  - limpiar_moneda()          │             │
│  - estandarizar_texto()      │             │
│  - eliminar_duplicados()     │             │
└──────────────┬───────────────┘             │
               │                             │
               ▼                             │
      ┌──────────────┐                       │
      │  Gastos      │                       │
      │  LIMPIOS     │◄──────────────────────┘
      │ 86 registros │
      └──────┬───────┘
             │
      ┌──────┴──────┐
      │             │
      ▼             ▼
  P1:GROUPBY    P2:GROUPBY+MERGE
  Categorías    Usuarios Total
      │             │
      ▼             ▼
  ┌──────────┐  ┌──────────┐
  │ CAFE: 19 │  │ Ana: 8700│
  │ BEBIDA:19│  │ Juan:4500│
  │ SNACK:16 │  └──────────┘
  └──────────┘
      
  P3:GROUPBY
  Medio Pago
      │
      ▼
  ┌──────────────┐
  │ TARJETA: 28  │
  │ EFECTIVO: 26 │
  │ NEQUI: 25    │
  └──────────────┘
```

---

## Estructura de Carpetas

```
Proyecto_H/
├── 📄 README.md                       ← Documentación principal
├── 📄 RESUMEN_PROYECTO.md             ← Resumen ejecutivo
├── 📄 GUIA_GITHUB.md                  ← Instrucciones GitHub
├── 📄 CHECKLIST_FINAL.md              ← Verificación antes de presentar
├── 📄 requirements.txt                ← Dependencias (pandas, numpy)
├── 📄 .gitignore                      ← Excluye venv y basura
├── 🔧 venv/                           ← Entorno virtual (NO subir)
│
├── 📁 data/
│   └── raw/
│       ├── 📊 usuarios.csv            ← 100 registros sucios
│       └── 📊 gastos_hormiga_mejorado.csv ← 106 registros sucios
│
├── 📁 documento/
│   └── 📄 GIT_FLOW.md                 ← Guía Git Flow paso a paso
│
└── 📁 src/
    ├── 🐍 analisis.py                 ← MAIN: 3 preguntas + análisis
    ├── 🐍 limpiar.py                  ← Módulo de limpieza (6 funciones)
    ├── 🐍 carga.py                    ← Función cargar datos (original)
    ├── 🐍 datos.py                    ← Variables globales (original)
    ├── 🐍 gastos.py                   ← Funciones gastos (original)
    ├── 🐍 main.py                     ← Menú interactivo (original)
    └── 📁 __pycache__/                ← Archivos compilados (ignorar)
```

---

## Módulos Python

### limpiar.py (Limpieza)
```python
┌─────────────────────────────────────────┐
│         MÓDULO: limpiar.py              │
├─────────────────────────────────────────┤
│                                         │
│ ✓ cargar_datos()                        │
│   → Lee CSV, maneja errores             │
│                                         │
│ ✓ manejar_valores_nulos()               │
│   → Detecta NaN, elimina filas          │
│                                         │
│ ✓ estandarizar_texto()                  │
│   → Minúsculas, quita espacios          │
│                                         │
│ ✓ limpiar_moneda()                      │
│   → Elimina $, convierte a números      │
│                                         │
│ ✓ eliminar_duplicados()                 │
│   → Quita filas repetidas               │
│                                         │
│ ✓ mostrar_resumen_limpieza()            │
│   → Imprime estadísticas                │
│                                         │
└─────────────────────────────────────────┘
```

### analisis.py (Análisis Principal)
```python
┌─────────────────────────────────────────┐
│        SCRIPT: analisis.py              │
├─────────────────────────────────────────┤
│                                         │
│ ✓ cargar_y_limpiar_datos()              │
│   → Carga usuarios + gastos             │
│   → Aplica limpieza automática          │
│                                         │
│ ✓ pregunta_1_frecuencia()               │
│   → ¿Categoría con más transacciones?   │
│   → Método: value_counts()              │
│   → Respuesta: CAFE (19 trans)          │
│                                         │
│ ✓ pregunta_2_agregacion()               │
│   → ¿Monto total por usuario?           │
│   → Método: merge() + groupby()         │
│   → Respuesta: Tabla con totales        │
│                                         │
│ ✓ pregunta_3_filtrado_conteo()          │
│   → ¿Gastos por medio de pago?          │
│   → Método: value_counts()              │
│   → Respuesta: TARJETA, EFECTIVO, etc   │
│                                         │
│ ✓ analisis_complementario()             │
│   → Estadísticas adicionales            │
│   → Min, max, promedio                  │
│                                         │
│ ✓ main()                                │
│   → Ejecuta todo el flujo               │
│                                         │
└─────────────────────────────────────────┘
```

---

## Flujo de Ejecución

```
$ python analisis.py

1️⃣  CARGANDO DATOS
    ├─ Lee usuarios.csv
    └─ Lee gastos_hormiga_mejorado.csv

2️⃣  LIMPIEZA USUARIOS
    ├─ Manejo de valores nulos
    ├─ Estandarización de texto
    ├─ Eliminación de duplicados
    └─ Resumen: 100 → 100 registros

3️⃣  LIMPIEZA GASTOS
    ├─ Manejo de valores nulos
    ├─ Limpieza de moneda ($)
    ├─ Estandarización de texto
    ├─ Eliminación de duplicados
    └─ Resumen: 106 → 86 registros

4️⃣  PREGUNTA 1: Frecuencia
    └─ Respuesta: CAFE (19)

5️⃣  PREGUNTA 2: Agregación (MERGE)
    └─ Tabla: Usuario → Total Gastado

6️⃣  PREGUNTA 3: Filtrado
    └─ Respuesta: TARJETA(28), EFECTIVO(26), NEQUI(25)

7️⃣  ANÁLISIS COMPLEMENTARIO
    └─ Estadísticas: min, max, promedio, etc.

✅ COMPLETADO
```

---

## Ciclo de Vida de los Datos

```
DATOS ORIGINALES (SUCIOS)
    │
    ├─ usuarios.csv (100)
    │   ├─ Espacios extras
    │   ├─ Mayúsculas inconsistentes
    │   └─ Valores nulos
    │
    └─ gastos.csv (106)
        ├─ Valores nulos en medio_pago
        ├─ Valores nulos en fecha
        ├─ Símbolos monetarios ($)
        └─ Categorías con mayúsculas
            │
            ▼
        LIMPIEZA (limpiar.py)
            │
            ├─ manejar_valores_nulos() ─→ 106 → 86
            ├─ limpiar_moneda()
            ├─ estandarizar_texto()
            └─ eliminar_duplicados()
            │
            ▼
        DATOS LIMPIOS (LISTOS PARA ANÁLISIS)
            │
            ├─ usuarios_limpios: 100
            └─ gastos_limpios: 86
            │
            ▼
        ANÁLISIS (analisis.py)
            │
            ├─ Pregunta 1: Frecuencia
            ├─ Pregunta 2: Merge + Agregación
            ├─ Pregunta 3: Filtrado
            └─ Complementario: Estadísticas
            │
            ▼
        RESPUESTAS Y REPORTES ✅
```

---

## Requisitos CESDE: Checklist Visual

```
┌──────────────────────────────────────────┐
│          EVALUACIÓN MOMENTO 2             │
├──────────────────────────────────────────┤
│                                          │
│  CONOCIMIENTO (Explicaciones)            │
│  ✅ DataFrame = tabla bidimensional      │
│  ✅ venv = aislamiento de dependencias   │
│  ✅ Pandas = manipulación de datos       │
│                                          │
│  DESEMPEÑO (Habilidades)                 │
│  ✅ pip install -r requirements.txt      │
│  ✅ Gestión de venv y dependencias       │
│  ✅ Modularidad en código                │
│                                          │
│  PRODUCTO (Entrega)                      │
│  ✅ Script .py sin errores               │
│  ✅ Datos sucios y limpios (100+)        │
│  ✅ 3 preguntas respondidas              │
│  ✅ Merge de tablas funcionando          │
│  ✅ .gitignore y README.md               │
│  ✅ Git Flow documentado                 │
│  ✅ venv configurado                     │
│  ✅ Repo GitHub con estructura           │
│                                          │
└──────────────────────────────────────────┘
```

---

## Resultados Esperados al Ejecutar

```
======================================================================
SISTEMA DE ANÁLISIS DE GASTOS HORMIGA
======================================================================

=== CARGANDO DATOS DE USUARIOS ===
Valores nulos encontrados: ...
Se eliminaron 0 filas con valores nulos

=== CARGANDO DATOS DE GASTOS ===
Valores nulos encontrados: ...
Se eliminaron 20 filas con valores nulos

=== PREGUNTA 1: ANÁLISIS DE FRECUENCIA ===
¿Cuál es la categoría con la mayor cantidad de transacciones?

Frecuencia de transacciones por categoría:
cafe          19
bebida        19
panaderia     19
snack         16
transporte    12
dulces         1

✓ Respuesta: La categoría 'cafe' tiene 19 transacciones

=== PREGUNTA 2: ANÁLISIS DE AGREGACIÓN ===
¿Cuál es el monto total de gastos por usuario?

[Tabla mostrando Usuario | Total Gastado | Cantidad | Promedio]

✓ Respuesta: [Usuario con mayor gasto]

=== PREGUNTA 3: ANÁLISIS DE FILTRADO ===
¿Cuántos gastos hay por cada medio de pago?

tarjeta    28
efectivo   26
nequi      25

=== ANÁLISIS COMPLEMENTARIO ===
📊 Estadísticas de Montos:
   Monto máximo: $5,000
   Monto mínimo: $2,200
   Promedio: $3,800
   Mediana: $3,850

👥 Usuarios activos: 45

💰 Categoría que genera más dinero: café ($85,500

✅ Análisis completado exitosamente
```

---

## Git Flow: Ramas Visualización

```
main (protegida) ─────────→ release/analisis-v1 ─────→ [v1.0 tag]
     ↑                             ↑
     │                             │
     └─────────────────────────────┘
                    │
                    │
develop ──→ feature/limpieza-datos ─┐
     ↑                                 │
     ├─→ feature/analisis-datos ──────┼─→ develop
     │                                 │
     └─→ feature/documentacion ────────┘


     [PR #1]  [PR #2]  [PR #3]  [PR #4]
      ↓        ↓        ↓        ↓
   feature  feature  feature release
   merge    merge    merge    merge
```

---

## Archivos por Propósito

```
CONFIGURACIÓN
  .gitignore          ← Excluye venv, basura
  requirements.txt    ← pandas==2.0.3, numpy==1.24.3

DOCUMENTACIÓN
  README.md              ← Guía principal
  RESUMEN_PROYECTO.md    ← Ejecutivo
  GUIA_GITHUB.md         ← GitHub step-by-step
  GIT_FLOW.md            ← Git Flow explicado
  CHECKLIST_FINAL.md     ← Verificación final

CÓDIGO FUNCIONAL
  src/analisis.py      ← PRINCIPAL (3 preguntas)
  src/limpiar.py       ← Módulo de limpieza

DATOS
  data/raw/usuarios.csv              ← 100 registros
  data/raw/gastos_hormiga_mejorado.csv ← 106 registros

ORIGINAL (Mantener)
  src/carga.py         ← Función carga
  src/datos.py         ← Variables
  src/gastos.py        ← Funciones
  src/main.py          ← Menú
```

---

**Diagrama completado. Proyecto 100% estructurado para presentación.** 🎉
