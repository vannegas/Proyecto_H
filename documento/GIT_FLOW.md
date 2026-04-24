# Guía Git Flow para el Proyecto

## ¿Qué es Git Flow?

**Git Flow** es un modelo de ramificación que organiza el desarrollo en ramas específicas:

```
main (producción)
  ↓
develop (integración)
  ↓
feature/ (nuevas características)
release/ (preparación para producción)
hotfix/ (correcciones urgentes)
```

---

## Configuración Inicial en GitHub

### 1. Crear el Repositorio en GitHub

1. Ve a https://github.com/new
2. Nombre: `Proyecto_H`
3. Descripción: "Sistema de análisis de gastos hormiga - CESDE"
4. Selecciona: **Private** (privado)
5. Crea el repositorio

### 2. Proteger Ramas

En tu repositorio GitHub:

1. Ve a **Settings** → **Branches**
2. Haz clic en "Add rule" para `main`:
   - ✅ Require a pull request before merging
   - ✅ Require approvals (mínimo 1)
   - ✅ Dismiss stale pull request approvals
   - ✅ Require status checks to pass

---

## Comandos Git Flow Esenciales

### Inicio Rápido

```bash
# 1. Clonar el repositorio
git clone https://github.com/TU_USUARIO/Proyecto_H.git
cd Proyecto_H

# 2. Crear rama develop localmente (solo primera vez)
git checkout -b develop
git push -u origin develop

# 3. Crear rama feature
git checkout develop
git pull origin develop
git checkout -b feature/nombre-caracteristica

# 4. Trabajo en la rama feature
git add .
git commit -m "feat: descripción del cambio"
git push -u origin feature/nombre-caracteristica

# 5. Crear Pull Request en GitHub
# (Copia el link que aparece en la terminal)

# 6. Después de mergear en develop, eliminar rama
git checkout develop
git pull origin develop
git branch -d feature/nombre-caracteristica
git push origin --delete feature/nombre-caracteristica
```

---

## Historial de Ramas para este Proyecto

### 1. Rama `feature/limpieza-datos`
```bash
git checkout -b feature/limpieza-datos

# Cambios:
# - Crear limpiar.py
# - Agregar funciones de limpieza
# - Limpiar gastos_hormiga.csv

git add src/limpiar.py
git commit -m "feat: módulo de limpieza con funciones para valores nulos y estandarización"
git push -u origin feature/limpieza-datos
```
→ **Mergear en develop vía Pull Request**

---

### 2. Rama `feature/analisis-datos`
```bash
git checkout develop
git pull origin develop
git checkout -b feature/analisis-datos

# Cambios:
# - Crear analisis.py
# - Implementar las 3 preguntas
# - Agregar análisis complementario

git add src/analisis.py
git commit -m "feat: script de análisis con 3 preguntas clave (frecuencia, agregación, filtrado)"
git push -u origin feature/analisis-datos
```
→ **Mergear en develop vía Pull Request**

---

### 3. Rama `feature/documentacion`
```bash
git checkout develop
git pull origin develop
git checkout -b feature/documentacion

# Cambios:
# - Crear/mejorar README.md
# - Agregar .gitignore
# - Actualizar requirements.txt

git add README.md .gitignore requirements.txt
git commit -m "docs: documentación completa del proyecto y configuración de dependencias"
git push -u origin feature/documentacion
```
→ **Mergear en develop vía Pull Request**

---

### 4. Rama `release/analisis-v1`
```bash
# Una vez que develop está listo para producción
git checkout -b release/analisis-v1 develop

# Cambios finales/versioning (opcional):
git add .
git commit -m "chore: preparación versión 1.0"
git push -u origin release/analisis-v1

# Hacer Pull Request de release/analisis-v1 → main
# Hacer Pull Request de release/analisis-v1 → develop (back-merge)

# Después de mergear en main:
git tag -a v1.0 -m "Versión 1.0 - Análisis de Gastos Hormiga"
git push origin v1.0

# Eliminar rama release
git push origin --delete release/analisis-v1
```

---

## Convenciones de Commits

Usa el formato **Conventional Commits**:

```
<type>(<scope>): <subject>

<body>

<footer>
```

### Tipos:
- `feat:` Nueva característica
- `fix:` Corrección de error
- `docs:` Cambios en documentación
- `style:` Formato, indentación (sin cambios lógicos)
- `refactor:` Refactorización de código
- `test:` Agregación o modificación de tests
- `chore:` Cambios en build, dependencies, etc.

### Ejemplos:

```bash
git commit -m "feat: función para cargar CSV con manejo de errores"
git commit -m "fix: corregir valores nulos en columna monto"
git commit -m "docs: agregar sección Git Flow en README.md"
git commit -m "refactor: modularizar funciones de análisis"
```

---

## Pull Request (PR) Template

Cuando crees un PR, usa este formato:

```markdown
## Descripción
Breve descripción de los cambios realizados.

## Tipo de Cambio
- [ ] Nueva característica (feature)
- [ ] Corrección de error (bug fix)
- [ ] Cambio que rompe compatibilidad (breaking change)
- [ ] Documentación

## Cambios Realizados
- Punto 1
- Punto 2
- Punto 3

## Verificación
- [ ] Mi código sigue las normas del proyecto
- [ ] He actualizado la documentación
- [ ] He probado los cambios localmente
- [ ] No hay errores de sintaxis

## Links Relacionados
Closes #(issue number si existe)
```

---

## Checklist de Evaluación Git Flow

Para verificar que cumples con los requisitos:

- [ ] Repositorio en GitHub
- [ ] Rama `main` protegida con PRs requeridos
- [ ] Rama `develop` como base de trabajo
- [ ] Mínimo 3 ramas `feature/*` creadas
- [ ] PRs con descripciones claras
- [ ] Rama `release/analisis-v1` creada
- [ ] Tags de versión (v1.0)
- [ ] Commits con mensajes claros y descriptivos
- [ ] Código limpio y bien documentado

---

## Comandos Útiles Git

```bash
# Ver estado actual
git status

# Ver commits recientes
git log --oneline -10

# Ver ramas locales y remotas
git branch -a

# Ver diferencias antes de commit
git diff

# Deshacer cambios en archivo específico
git checkout -- archivo.py

# Actualizar rama local con cambios remotos
git pull origin rama-actual

# Ver quién hizo qué (blame)
git blame archivo.py

# Buscar cambios en historial
git log -S "palabra_clave"
```

---

## Flujo Completo: Paso a Paso

```bash
# 1. Clonar proyecto (solo primera vez)
git clone <url-repo>
cd Proyecto_H

# 2. Asegurar que tengo develop local
git checkout -b develop
git push -u origin develop

# 3. Crear nueva rama feature
git checkout develop
git pull origin develop
git checkout -b feature/mi-cambio

# 4. Trabajar en la rama
# ... hacer cambios ...
git add .
git commit -m "feat: descripción clara"
git push -u origin feature/mi-cambio

# 5. Crear PR en GitHub (copiar link de la terminal)

# 6. Esperar review y mergear (en GitHub)

# 7. Actualizar local después del merge
git checkout develop
git pull origin develop
git branch -d feature/mi-cambio

# 8. Cuando esté listo el release
git checkout -b release/analisis-v1 develop
git push -u origin release/analisis-v1
# ... crear PR en GitHub ...
git tag v1.0
git push origin v1.0
```

---

## Resumen para el CESDE

**Lo que debes demostrar:**
1. ✅ Estructura Git Flow completa
2. ✅ Múltiples ramas feature con PRs
3. ✅ Rama release creada y taggueada
4. ✅ Commits descriptivos
5. ✅ Rama main protegida
6. ✅ Documentación clara en README

**Resultado esperado:** Un repositorio profesional que demuestre control de versiones eficaz.
