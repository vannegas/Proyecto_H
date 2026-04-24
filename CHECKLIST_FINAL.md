# ✅ CHECKLIST FINAL - PROYECTO CESDE

## Antes de Presentar, Verifica Todo

---

## 📋 Funcionamiento del Código

### Ejecución Local
- [ ] `cd src` y `python analisis.py` funciona sin errores
- [ ] Aparecen los 3 análisis completos:
  - [ ] Pregunta 1: Categoría con mayor frecuencia
  - [ ] Pregunta 2: Monto total por usuario (merge visible)
  - [ ] Pregunta 3: Cantidad por medio de pago
- [ ] Se moestra resumen de limpieza de datos
- [ ] No hay excepciones (errors)

### Verificar Datos
- [ ] `usuarios.csv`: 100 registros, 5 columnas
- [ ] `gastos_hormiga_mejorado.csv`: 106 registros, 6 columnas
- [ ] Ambos archivos tienen datos sucios intencionales
- [ ] Después de limpiar, número de filas es menor

---

## 📁 Archivos Requeridos Presentes

### Carpeta raíz (Proyecto_H/)
- [ ] `.gitignore`
- [ ] `requirements.txt` (con pandas y numpy)
- [ ] `README.md`
- [ ] `RESUMEN_PROYECTO.md`
- [ ] `GUIA_GITHUB.md`
- [ ] `GIT_FLOW.md` (en documento/)

### Carpeta data/raw/
- [ ] `usuarios.csv` (100 registros)
- [ ] `gastos_hormiga_mejorado.csv` (106 registros)

### Carpeta src/
- [ ] `analisis.py` (script principal)
- [ ] `limpiar.py` (módulo de limpieza)
- [ ] `carga.py` (función original)
- [ ] `datos.py` (variables originales)
- [ ] `gastos.py` (funciones originales)
- [ ] `main.py` (menú original)

### Carpeta documento/
- [ ] `GIT_FLOW.md`

---

## 🧹 Código y Limpieza

### limpiar.py debe tener:
- [ ] Función `cargar_datos(ruta_csv)`
- [ ] Función `manejar_valores_nulos(df, estrategia)`
- [ ] Función `estandarizar_texto(df, columnas)`
- [ ] Función `limpiar_moneda(df, columnas_moneda)`
- [ ] Función `eliminar_duplicados(df, subset)`
- [ ] Función `mostrar_resumen_limpieza(df_original, df_limpio)`
- [ ] Docstrings en todas las funciones
- [ ] Comentarios claros

### analisis.py debe tener:
- [ ] Función `pregunta_1_frecuencia(df_gastos)`
  - Usa: `value_counts()`
  - Responde: ¿Cuál es la categoría con más transacciones?
- [ ] Función `pregunta_2_agregacion(df_gastos, df_usuarios)`
  - Usa: `merge()` y `groupby()`
  - Responde: ¿Cuál es el monto total por usuario?
- [ ] Función `pregunta_3_filtrado_conteo(df_gastos)`
  - Usa: `value_counts()`
  - Responde: ¿Cuántos gastos por medio de pago?
- [ ] Función `analisis_complementario()`
- [ ] Función `main()`
- [ ] Docstrings claros

---

## 📚 Documentación

### README.md debe incluir:
- [ ] Descripción del proyecto
- [ ] Requisitos previos
- [ ] Instrucciones configuración venv (Windows y Linux)
- [ ] Instrucciones para ejecutar `analisis.py`
- [ ] Estructura de carpetas
- [ ] Descripción de módulos
- [ ] Tabla de funciones
- [ ] Dependencias
- [ ] Git Flow explicado
- [ ] Problemas comunes y soluciones
- [ ] Explicación: ¿Qué es un DataFrame?
- [ ] Explicación: ¿Por qué usamos venv?

### GIT_FLOW.md debe incluir:
- [ ] Explicación de Git Flow
- [ ] Comandos básicos de Git
- [ ] Historial de ramas a crear
- [ ] Convenciones de commits
- [ ] Template de PR
- [ ] Checklist de evaluación

### GUIA_GITHUB.md debe incluir:
- [ ] Paso a paso crear GitHub
- [ ] Crear repositorio
- [ ] Configurar Git localmente
- [ ] Crear ramas develop
- [ ] Proteger rama main
- [ ] Crear 3 PRs de ejemplo
- [ ] Crear release
- [ ] Solución de problemas comunes

### RESUMEN_PROYECTO.md debe incluir:
- [ ] Resumen ejecutivo
- [ ] Lo implementado
- [ ] Cómo ejecutar
- [ ] Respuestas a las 3 preguntas
- [ ] Checklist de evaluación CESDE
- [ ] Próximos pasos para GitHub

---

## 🔀 Git Flow (Estructura)

### Ramas que debes crear en GitHub:
- [ ] `main` (protegida)
- [ ] `develop` (base de trabajo)
- [ ] `feature/limpieza-datos` (mergear en develop)
- [ ] `feature/analisis-datos` (mergear en develop)
- [ ] `feature/documentacion` (mergear en develop)
- [ ] `release/analisis-v1` (mergear en main)

### Pull Requests a mostrar:
- [ ] PR #1: feature/limpieza-datos → develop
- [ ] PR #2: feature/analisis-datos → develop
- [ ] PR #3: feature/documentacion → develop
- [ ] PR #4: release/analisis-v1 → main

### Tags:
- [ ] `v1.0` creado en main

---

## 🎯 Conocimiento para Explicar

Prepárate para responder:

### ¿Qué es un DataFrame?
- [ ] Sé explicar que es una tabla bidimensional (filas y columnas)
- [ ] Sé que es como una hoja de Excel en Python
- [ ] Sé que permite operaciones rápidas sobre datos

### ¿Por qué usamos entornos virtuales?
- [ ] Sé explicar que aíslan las dependencias
- [ ] Sé que evitan conflictos entre versiones
- [ ] Sé que facilitan reproducibilidad

### ¿Cómo funcionó tu limpieza de datos?
- [ ] Sé explicar cada función de limpiar.py
- [ ] Sé cuántas filas tenía antes y después
- [ ] Sé qué problemas tenían los datos

### ¿Cómo hiciste el merge?
- [ ] Sé explicar merge() entre usuarios y gastos
- [ ] Sé que une por id_usuario
- [ ] Sé ver el resultado en la tabla

---

## ⚙️ Configuración Técnica

### requirements.txt
- [ ] Tiene pandas==2.0.3
- [ ] Tiene numpy==1.24.3
- [ ] No hay versiones innecesarias
- [ ] Se instaló correctamente con `pip install -r requirements.txt`

### venv (Entorno Virtual)
- [ ] Se creó con `python -m venv venv`
- [ ] Está en `.gitignore` (NO subir a GitHub)
- [ ] Se activa correctamente en Windows

### .gitignore
- [ ] Incluye `venv/`
- [ ] Incluye `__pycache__/`
- [ ] Incluye `.pyc` archivos
- [ ] Incluye `.env`
- [ ] Incluye archivos de IDE (.vscode, .idea)

---

## 📊 Datos del Proyecto

### usuarios.csv
- [ ] Tiene 100 registros
- [ ] Tiene columnas: id_usuario, nombre, email, ciudad, estado_civil
- [ ] Tiene datos sucios:
  - [ ] Nombres con inconsistencias (mayúsculas)
  - [ ] Espacios extras
  - [ ] Valores nulos

### gastos_hormiga_mejorado.csv
- [ ] Tiene 106 registros originales
- [ ] Tiene columnas: id_gasto, id_usuario, categoria, monto, medio_pago, fecha
- [ ] Tiene datos sucios:
  - [ ] Valores nulos en medio_pago
  - [ ] Valores nulos en fecha
  - [ ] Categorías con inconsistencias
  - [ ] Montos con símbolos

---

## 🧪 Pruebas

### Pruebas Locales
- [ ] `cd C:\Users\juane\Desktop\Proyecto_H\src`
- [ ] `python analisis.py`
- [ ] Verificar 3 preguntas respondidas correctamente
- [ ] Verificar estadísticas de limpieza

### Pruebas en GitHub
- [ ] Repositorio visible (privado, pero compartido con profesor)
- [ ] main branch protegida
- [ ] develop branch existe
- [ ] 3+ PRs visibles
- [ ] Release/tag v1.0 visible
- [ ] README.md aparece al entrar al repo

---

## 🚀 Para el Día de Presentación

Prepárate con:
- [ ] Laptop con Python instalado
- [ ] Terminal abierta en proyecto
- [ ] Git Bash o PowerShell listo
- [ ] GitHub abierto en navegador
- [ ] Editor de código (VS Code) listo
- [ ] Explicación de 3 minutos del proyecto
- [ ] Demostración en vivo ejecutando `analisis.py`

---

## 🎤 Respuestas Cortas para Profesores

### "¿Qué hace tu proyecto?"
"Analiza gastos personales. Carga dos archivos CSV con datos sucios, los limpia (elimina nulos, estandariza texto), y responde 3 preguntas usando Pandas: frecuencia de categorías, agregación por usuario, y conteo por medio de pago."

### "¿Cómo manejaste los datos sucios?"
"Creé un módulo llamado limpiar.py con 6 funciones específicas. Detecté valores nulos, eliminé 20 filas problemáticas de 106, estandaricé texto a minúsculas y sin espacios, y convertí símbolos monetarios a números."

### "¿Hiciste merge de datos?"
"Sí, en la pregunta 2. Usé merge() para unir usuarios con gastos por id_usuario, luego groupby() para sumar gastos por usuario. Muestra nombre del usuario y total gastado."

### "¿Cómo estructura tu código?"
"Modular. Tengo limpiar.py (reutilizable), analisis.py (análisis), y funciones documentadas. Cada función tiene docstring. Fácil de mantener y extender."

---

## 📞 Contactos Útiles

Profesor CESDE: [Agrega email de tu profesor]
GitHub: https://github.com/TU_USUARIO/Proyecto_H
Correo: Tu email

---

## ✅ Último Chequeo Antes de Presentar

```
¿Código funciona? [ ]
¿3 preguntas respondidas? [ ]
¿Datos limpios correctamente? [ ]
¿README completo? [ ]
¿GitHub listo con Git Flow? [ ]
¿Puedo explicar qué es un DataFrame? [ ]
¿Puedo explicar por qué venv? [ ]
¿Puedo ejecutar analisis.py en vivo? [ ]
¿Tengo lista la URL del GitHub? [ ]
¿Todos los archivos están? [ ]
```

---

**¡Proyecto 100% Listo para Presentar! 🎉**

Si algo no funciona, revisa:
1. ¿Está el venv activado?
2. ¿Ejecuto desde carpeta src/?
3. ¿Los archivos CSV existen?
4. ¿Pandas está instalado?

Cualquier pregunta, consulta RESUMEN_PROYECTO.md o GUIA_GITHUB.md
