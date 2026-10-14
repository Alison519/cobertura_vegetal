from tda.pila import Pila
from modelo.registro import RegistroPerdida


class HistorialPerdidas:
    """Historial de pérdidas apoyado en una Pila: el último registro queda en el tope."""

    def __init__(self):
        self._registros = Pila()

    def registrar(self, registro):
        if not isinstance(registro, RegistroPerdida):
            raise TypeError("Se esperaba un RegistroPerdida")
        self._registros.apilar(registro)

    def ultimo(self):
        """Devuelve el registro más reciente sin quitarlo (None si no hay)."""
        if self._registros.esta_vacia():
            return None
        return self._registros.tope()

    def deshacer(self):
        """Elimina y devuelve el último registro (None si no hay)."""
        if self._registros.esta_vacia():
            return None
        return self._registros.desapilar()

    def total_hectareas(self):
        return sum(r.hectareas for r in self._registros)

    def cantidad(self):
        return self._registros.tamanio()
