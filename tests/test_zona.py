import unittest
from modelo.actividad import ExtraccionIlegal, ExpansionAgricola
from modelo.autoridad import Autoridad
from modelo.efecto import EfectoAmbiental
from modelo.reporte import ReporteActividad
from modelo.zona import Zona


class TestZona(unittest.TestCase):
    def setUp(self):
        self.municipio = Zona("Municipio", 1000)
        self.vereda = Zona("Vereda", 400)
        self.sector = Zona("Sector", 100)
        self.municipio.agregar_subzona(self.vereda)
        self.vereda.agregar_subzona(self.sector)

    def test_zona_sin_subzonas_devuelve_su_valor(self):
        self.sector.registrar_perdida(2, "tala")
        self.assertEqual(self.sector.hectareas_perdidas_total(), 2)

    def test_hectareas_recursivas(self):
        self.municipio.registrar_perdida(1, "a")
        self.vereda.registrar_perdida(2, "b")
        self.sector.registrar_perdida(3, "c")
        self.assertEqual(self.municipio.hectareas_perdidas_total(), 6)

    def test_deshacer_actualiza_total(self):
        self.vereda.registrar_perdida(5, "a")
        self.vereda.historial.deshacer()
        self.assertEqual(self.municipio.hectareas_perdidas_total(), 0)

    def test_contar_actividades(self):
        self.vereda.actividades.append(ExtraccionIlegal(1))
        self.sector.actividades.append(ExpansionAgricola(1))
        self.assertEqual(self.municipio.contar_actividades(), 2)
        self.assertEqual(self.municipio.contar_actividades(solo_ilegales=True), 1)

    def test_gravedad_total(self):
        self.vereda.efectos.append(EfectoAmbiental("riesgo de deslizamiento", 4))
        self.sector.efectos.append(EfectoAmbiental("alteracion del microclima", 2))
        self.assertEqual(self.municipio.gravedad_total(), 6)

    def test_buscar_en_subzonas(self):
        self.assertIs(self.municipio.buscar("sector"), self.sector)
        self.assertIsNone(self.municipio.buscar("no existe"))

    def test_perdida_invalida(self):
        with self.assertRaises(ValueError):
            self.vereda.registrar_perdida(0, "x")


class TestAutoridad(unittest.TestCase):
    def test_reportes_en_orden_de_llegada(self):
        a = Autoridad("Test")
        a.recibir_reporte(ReporteActividad(1, "primero"))
        a.recibir_reporte(ReporteActividad(2, "segundo"))
        self.assertEqual(a.siguiente_reporte().id, 1)
        self.assertEqual(a.atender_reporte().estado, "atendido")
        self.assertEqual(a.atender_reporte().id, 2)
        self.assertIsNone(a.atender_reporte())

    def test_reporte_sin_descripcion(self):
        with self.assertRaises(ValueError):
            ReporteActividad(1, "   ")


if __name__ == "__main__":
    unittest.main()
