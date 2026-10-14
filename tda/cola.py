class Cola:
    """TDA Cola (FIFO): el primero en entrar es el primero en salir."""

    def __init__(self):
        self._elementos = []

    def encolar(self, item):
        self._elementos.append(item)

    def desencolar(self):
        if self.esta_vacia():
            raise IndexError("La cola está vacía")
        return self._elementos.pop(0)

    def frente(self):
        if self.esta_vacia():
            raise IndexError("La cola está vacía")
        return self._elementos[0]

    def esta_vacia(self):
        return len(self._elementos) == 0

    def tamanio(self):
        return len(self._elementos)

    def __iter__(self):
        # Recorre del frente al final sin modificar la cola
        return iter(self._elementos)
