from datetime import date


class RegistroPerdida:
    """Un registro de hectáreas de cobertura vegetal perdidas."""

    def __init__(self, hectareas, motivo, fecha=None):
        if hectareas <= 0:
            raise ValueError("Las hectáreas deben ser mayores que cero")
        self.hectareas = hectareas
        self.motivo = motivo
        self.fecha = fecha or date.today().isoformat()

    def __str__(self):
        return f"[{self.fecha}] {self.hectareas} ha - {self.motivo}"
