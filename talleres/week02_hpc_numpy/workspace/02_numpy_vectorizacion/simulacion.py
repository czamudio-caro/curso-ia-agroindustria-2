from __future__ import annotations

import time
import numpy as np


def loop_for(x: np.ndarray) -> np.ndarray:
    y = np.empty_like(x)
    for i in range(x.shape[0]):
        y[i] = np.sin(x[i]) + np.cos(x[i])
    return y


def vectorizado(x: np.ndarray) -> np.ndarray:
    # Vectorización: operar sobre todo el array en una sola llamada
    return np.sin(x) + np.cos(x)


def main() -> None:
    n = 1_000_000
    x = np.random.rand(n).astype(np.float64)

    t0 = time.perf_counter()
    y1 = loop_for(x)
    t1 = time.perf_counter() - t0  # perf_counter es un temporizador de alta resolución [web:266]

    t0 = time.perf_counter()
    y2 = vectorizado(x)
    t2 = time.perf_counter() - t0  # perf_counter es un temporizador de alta resolución [web:266]

    diff = float(np.max(np.abs(y1 - y2)))
    speedup = t1 / t2 if t2 > 0 else float("inf")

    print(f"Tiempo for-loop:    {t1:.4f} s")
    print(f"Tiempo vectorizado: {t2:.4f} s")
    print(f"Speedup:            {speedup:.2f}x")
    print(f"Max diff:           {diff:.6e}")


if __name__ == "__main__":
    main()
