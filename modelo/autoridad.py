from tda.cola import Cola


class Autoridad:
    """Autoridad ambiental: atiende los reportes en orden de llegada (Cola)."""

    def __init__(self, nombre):
        self.nombre = nombre
        self._reportes = Cola()
        self.zonas_vigiladas = []

    def recibir_reporte(self, reporte):
        self._reportes.encolar(reporte)

    def atender_reporte(self):
        """Atiende el reporte más antiguo (None si no hay pendientes)."""
        if self._reportes.esta_vacia():
            return None
        reporte = self._reportes.desencolar()
        reporte.estado = "atendido"
        return reporte

    def siguiente_reporte(self):
        """Ve el próximo reporte sin atenderlo (None si no hay)."""
        if self._reportes.esta_vacia():
            return None
        return self._reportes.frente()

    def pendientes(self):
        return self._reportes.tamanio()

    def vigilar(self, zona):
        if zona not in self.zonas_vigiladas:
            self.zonas_vigiladas.append(zona)
