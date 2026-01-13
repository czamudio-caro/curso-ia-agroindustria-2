from __future__ import annotations

import numpy as np


def render_ascii(mapa: np.ndarray, step: int = 5) -> str:
    """
    Render simple:
    - "R" = sequía
    - "D" = inundación
    - "." = normal
    """
    lines = []
    for r in range(0, mapa.shape[0], step):
        lines.append("".join(mapa[r, ::step].tolist()))
    return "\n".join(lines)


def main() -> None:
    np.random.seed(7)

    # Terreno 100x100 -> simula 10.000 m² si 1 celda = 1 m²
    terreno = np.random.rand(100, 100)

    # Máscaras booleanas (lógica espacial sin iterar celda por celda)
    sequia = terreno < 0.2
    inundacion = terreno > 0.85

    pct_sequia = 100.0 * float(sequia.mean())
    pct_inundacion = 100.0 * float(inundacion.mean())

    # Acción por celda con np.where (vectorizado)
    acciones = np.where(sequia, "R", np.where(inundacion, "D", "."))

    print("=== Reporte rápido (terreno 100x100) ===")
    print(f"% sequía (<0.2):     {pct_sequia:.2f}%")
    print(f"% inundación (>0.85): {pct_inundacion:.2f}%")
    print("")
    print("Mapa ASCII (muestreo cada 5 celdas):")
    print(render_ascii(acciones, step=5))


if __name__ == "__main__":
    main()
