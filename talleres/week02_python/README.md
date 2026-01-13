# Semana 02: Fundamentos de Computación Científica para el Agro

> Rol: Ingeniero de Datos / AI Specialist.
> Objetivo: transición de scripts básicos a código que escala.
> Tech Stack: Python, NumPy, vectorización (SIMD).

## Visión general

En la Semana 01 aprendiste a automatizar tareas y registrar evidencia con Git.
En la Semana 02 aprenderás a escribir **código que escala**, especialmente para sensores e imágenes (matrices grandes).

## Objetivos (3)

1) Programación defensiva: validar datos y fallar rápido con mensajes claros.
2) Vectorización: reemplazar bucles `for` por operaciones NumPy.
3) Lógica espacial: operar con matrices y máscaras booleanas.

## Dónde trabajas

Todo se hace en:
`talleres/week02_hpc_numpy/workspace/`

## Hoja de ruta (paso a paso)

### Paso 1: Lógica defensiva

Archivo: `workspace/01_fundamentos_logica/main.py`

Ejecución:

```bash
cd talleres/week02_hpc_numpy/workspace
python 01_fundamentos_logica/main.py
```

### Paso 2: Vectorización NumPy (benchmark)

Archivo: `workspace/02_numpy_vectorizacion/simulacion.py`

Ejecución:

```bash
python 02_numpy_vectorizacion/simulacion.py
```

### Paso 3: Boss final (taller)

Archivo: `workspace/taller_numpy.py`

Ejecución:

```bash
python taller_numpy.py
```

## Reporte en LaTeX (desde Semana 2)

Objetivo: generar un PDF simple (1 página) con tus resultados.

Compilación (en contenedor full-docs):

```bash
cd talleres/week02_hpc_numpy/workspace/report
latexmk -xelatex -interaction=nonstopmode main.tex
```

## Definición de Hecho (DoD)

- Ejecutaste y modificaste los 3 scripts Python.
- Generaste el PDF del reporte en `workspace/report/main.pdf`.
- Subiste tus cambios a GitHub.

## Entrega (simple)

Usa el panel de Source Control de Codespaces:

- Adicionar
- Comentar
- Commit & Push
