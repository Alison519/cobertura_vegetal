class CoberturaVegetal:
    """Cobertura vegetal de una zona (bosque, rastrojo, pastos...)."""

    def __init__(self, tipo, area_ha, estado="conservada"):
        if area_ha < 0:
            raise ValueError("El área no puede ser negativa")
        self.tipo = tipo
        self.area_ha = area_ha
        self.estado = estado

    def reducir(self, hectareas):
        if hectareas <= 0:
            raise ValueError("Las hectáreas a reducir deben ser mayores que cero")
        if hectareas > self.area_ha:
            raise ValueError("No se puede reducir más área de la que existe")
        self.area_ha -= hectareas
        self.estado = "perdida" if self.area_ha == 0 else "degradada"
