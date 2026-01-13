from __future__ import annotations

def validar_sensor_row(row: dict) -> None:
    """
    Fail fast: valida un registro de sensor.
    row ejemplo: {"id": "SENSOR_01", "temp": 24.2, "hum": 55}
    """
    # Guard clauses (salir temprano con error claro)
    if "id" not in row or not str(row["id"]).strip():
        raise ValueError("Falta 'id' o está vacío.")

    if "temp" not in row:
        raise ValueError("Falta 'temp' (temperatura).")
    if not isinstance(row["temp"], (int, float)):
        raise ValueError("'temp' debe ser numérica (int/float).")
    if row["temp"] < -10 or row["temp"] > 60:
        raise ValueError("'temp' fuera de rango esperado [-10, 60].")

    if "hum" not in row:
        raise ValueError("Falta 'hum' (humedad).")
    if not isinstance(row["hum"], (int, float)):
        raise ValueError("'hum' debe ser numérica (int/float).")
    if row["hum"] < 0 or row["hum"] > 100:
        raise ValueError("'hum' fuera de rango esperado [0, 100].")


def main() -> None:
    datos = [
        {"id": "SENSOR_01", "temp": 24.2, "hum": 55},
        {"id": "SENSOR_02", "temp": 25.1, "hum": 56},
        {"id": "SENSOR_XX", "temp": 999, "hum": 10},   # dato imposible (debe fallar)
        {"id": "", "temp": 23.0, "hum": 50},         # id vacío (debe fallar)
    ]

    ok = 0
    for row in datos:
        try:
            validar_sensor_row(row)
            ok += 1
        except ValueError as e:
            print(f"[ERROR] Registro inválido: {row} -> {e}")

    print(f"Registros válidos: {ok}/{len(datos)}")


if __name__ == "__main__":
    main()
