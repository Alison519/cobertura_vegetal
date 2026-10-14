from datetime import date


class ReporteActividad:
    """Denuncia sobre una actividad que afecta la cobertura vegetal."""

    def __init__(self, id_reporte, descripcion, actividad=None, fecha=None):
        if not descripcion or not descripcion.strip():
            raise ValueError("El reporte necesita una descripción")
        self.id = id_reporte
        self.descripcion = descripcion.strip()
        self.actividad = actividad
        self.fecha = fecha or date.today().isoformat()
        self.estado = "pendiente"

    def __str__(self):
        return f"#{self.id} [{self.estado}] {self.fecha}: {self.descripcion}"
