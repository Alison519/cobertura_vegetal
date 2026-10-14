from modelo.historial import HistorialPerdidas
from modelo.registro import RegistroPerdida


class Zona:
    """Zona de Fusagasugá. Puede tener subzonas (municipio > vereda > sector)."""

    def __init__(self, nombre, area_ha):
        self.nombre = nombre
        self.area_ha = area_ha
        self.subzonas = []
        self.coberturas = []
        self.actividades = []
        self.efectos = []
        self.historial = HistorialPerdidas()

    def agregar_subzona(self, zona):
        if zona is self:
            raise ValueError("Una zona no puede ser subzona de sí misma")
        self.subzonas.append(zona)

    def registrar_perdida(self, hectareas, motivo, fecha=None):
        self.historial.registrar(RegistroPerdida(hectareas, motivo, fecha))

    # ---------- métodos recursivos ----------

    def hectareas_perdidas_total(self):
        total = self.historial.total_hectareas()
        for sub in self.subzonas:
            total += sub.hectareas_perdidas_total()
        return total

    def contar_actividades(self, solo_ilegales=False):
        total = sum(1 for a in self.actividades if a.es_ilegal or not solo_ilegales)
        for sub in self.subzonas:
            total += sub.contar_actividades(solo_ilegales)
        return total

    def gravedad_total(self):
        total = sum(e.gravedad for e in self.efectos)
        for sub in self.subzonas:
            total += sub.gravedad_total()
        return total

    def buscar(self, nombre):
        if self.nombre.lower() == nombre.lower():
            return self
        for sub in self.subzonas:
            encontrada = sub.buscar(nombre)
            if encontrada is not None:
                return encontrada
        return None

    def resumen(self, nivel=0):
        sangria = "    " * nivel
        lineas = [
            f"{sangria}- {self.nombre}: {self.hectareas_perdidas_total()} ha perdidas, "
            f"{self.contar_actividades()} actividades, gravedad {self.gravedad_total()}"
        ]
        for a in self.actividades:
            lineas.append(f"{sangria}    causa: {a}")
        for e in self.efectos:
            lineas.append(f"{sangria}    efecto: {e}")
        for sub in self.subzonas:
            lineas.append(sub.resumen(nivel + 1))
        return "\n".join(lineas)
