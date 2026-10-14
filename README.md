# Pérdida de cobertura vegetal en Fusagasugá

Prototipo en Python con TDA (pilas y colas) y recursividad.

## Ejecutar
    python main.py

## Pruebas
    python -m unittest discover -s . -t .

## Estructura
    tda/      Pila y Cola (TDA propios)
    modelo/   Clases del diagrama (Zona, ActividadHumana, Autoridad, ...)
    tests/    Pruebas unitarias
    main.py   Menú del prototipo

## Dónde se usa cada concepto
- Cola: `Autoridad` atiende los reportes en orden de llegada.
- Pila: `HistorialPerdidas` guarda los registros; el último queda en el tope (deshacer).
- Recursividad: `Zona` (hectareas_perdidas_total, contar_actividades, gravedad_total, buscar, resumen).
