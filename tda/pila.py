class Pila:
    """TDA Pila (LIFO): el último en entrar es el primero en salir."""

    def __init__(self):
        self._elementos = []

    def apilar(self, item):
        self._elementos.append(item)

    def desapilar(self):
        if self.esta_vacia():
            raise IndexError("La pila está vacía")
        return self._elementos.pop()

    def tope(self):
        if self.esta_vacia():
            raise IndexError("La pila está vacía")
        return self._elementos[-1]

    def esta_vacia(self):
        return len(self._elementos) == 0

    def tamanio(self):
        return len(self._elementos)

    def __iter__(self):
        # Recorre del tope hacia la base sin modificar la pila
        return iter(reversed(self._elementos))
