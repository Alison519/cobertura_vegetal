class ActividadHumana:
    """Causa del problema. 'intensidad' = hectáreas estimadas que afecta."""

    def __init__(self, nombre, intensidad, es_ilegal=False):
        if intensidad <= 0:
            raise ValueError("La intensidad debe ser mayor que cero")
        self.nombre = nombre
        self.intensidad = intensidad
        self.es_ilegal = es_ilegal

    def impactar(self, cobertura):
        cobertura.reducir(self.intensidad)

    def __str__(self):
        marca = " (ilegal)" if self.es_ilegal else ""
        return f"{self.nombre}{marca} - {self.intensidad} ha"


class TalaIndiscriminada(ActividadHumana):
    def __init__(self, intensidad, especies_demandadas=None, volumen_madera=0.0):
        super().__init__("Tala indiscriminada", intensidad, es_ilegal=True)
        self.especies_demandadas = especies_demandadas or []
        self.volumen_madera = volumen_madera


class ExpansionAgricola(ActividadHumana):
    def __init__(self, intensidad, nuevos_cultivos="", area_ocupada=0.0):
        super().__init__("Expansión agrícola", intensidad)
        self.nuevos_cultivos = nuevos_cultivos
        self.area_ocupada = area_ocupada


class AmpliacionPastizales(ActividadHumana):
    def __init__(self, intensidad, cabezas_ganado=0, area_ocupada=0.0):
        super().__init__("Ampliación de pastizales", intensidad)
        self.cabezas_ganado = cabezas_ganado
        self.area_ocupada = area_ocupada


class ConstruccionRural(ActividadHumana):
    def __init__(self, intensidad, cercas_postes=0, tipo_obra=""):
        super().__init__("Construcción rural", intensidad)
        self.cercas_postes = cercas_postes
        self.tipo_obra = tipo_obra


class ExtraccionIlegal(ActividadHumana):
    def __init__(self, intensidad, recurso_extraido="", hay_denuncia=False):
        super().__init__("Extracción ilegal", intensidad, es_ilegal=True)
        self.recurso_extraido = recurso_extraido
        self.hay_denuncia = hay_denuncia
