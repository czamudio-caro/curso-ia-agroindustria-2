# Guía LaTeX (Semana 2) — Reporte PDF simple

Esta guía te permite generar un PDF (reporte) desde LaTeX usando **un solo comando**.

## 1) Dónde trabajar

Entra a la carpeta del reporte:

```bash
cd talleres/week02_hpc_numpy/workspace/report
```

## 2) Archivos esperados

- `main.tex`: tu reporte en LaTeX.
- `main.pdf`: salida final (se genera al compilar).

## 3) Compilar (1 comando)

Compila con `latexmk`:

```bash
latexmk -xelatex -interaction=nonstopmode main.tex
```

Si compila bien, se crea `main.pdf`.

## 4) Limpiar archivos temporales (opcional)

LaTeX genera archivos auxiliares. Para borrarlos:

```bash
latexmk -c
```

## 5) Errores comunes y solución rápida

### A) “File `main.tex` not found”

- Estás en otra carpeta.
- Solución:

```bash
pwd
ls -lh
```

y vuelve a `workspace/report`.

### B) “! LaTeX Error: File `XXXX.sty` not found.”

Falta un paquete en el entorno.

- Solución simple: asegúrate de estar usando el contenedor **full-docs**.
- Si sigue, avisa al docente el paquete faltante (el nombre aparece en el error).

### C) “Overfull \\hbox ...”

No es un error, es un *warning* (una línea se salió del margen).
Soluciones típicas:

- Partir líneas largas (sobre todo URLs).
- Evitar texto muy largo en una sola línea en `verbatim`.
- Usar listas o saltos de línea.

### D) “Runaway argument” / “Paragraph ended before …”

Esto suele pasar cuando hay bloques especiales mal cerrados.

- Revisa que cada:
  - `\begin{...}` tenga su `\end{...}`
  - `{}` estén balanceadas
  - no falte un `}` en títulos/sections

## 6) Qué debe tener tu reporte (mínimo)

- Título + autor + fecha.
- Resumen (5–8 líneas).
- Resultados del benchmark (tiempos + speedup).
- Resultados del taller satelital (porcentajes / hallazgos).
- Comando de compilación (reproducibilidad).

## 7) Entrega (simple)

Cuando ya exista `main.pdf`:

```bash
git add talleres/week02_hpc_numpy/workspace/report
git commit -m "docs: reporte latex semana 2"
git push
```
