TIPOS_EFECTO = (
    "erosion y degradacion del suelo",
    "riesgo de deslizamiento",
    "alteracion de la regulacion hidrica",
    "alteracion del microclima",
    "perdida de habitats",
)


class EfectoAmbiental:
    """Consecuencia de la pérdida de cobertura. Gravedad de 1 (baja) a 5 (alta)."""

    def __init__(self, tipo, gravedad, descripcion=""):
        if tipo not in TIPOS_EFECTO:
            raise ValueError(f"Tipo de efecto no válido: {tipo}")
        if not 1 <= gravedad <= 5:
            raise ValueError("La gravedad debe estar entre 1 y 5")
        self.tipo = tipo
        self.gravedad = gravedad
        self.descripcion = descripcion

    def __str__(self):
        return f"{self.tipo} (gravedad {self.gravedad})"
