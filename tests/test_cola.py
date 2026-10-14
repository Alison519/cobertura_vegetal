import unittest
from tda.cola import Cola


class TestCola(unittest.TestCase):
    def test_cola_nueva_esta_vacia(self):
        self.assertTrue(Cola().esta_vacia())

    def test_encolar_y_frente(self):
        c = Cola()
        c.encolar("a")
        c.encolar("b")
        self.assertEqual(c.frente(), "a")
        self.assertEqual(c.tamanio(), 2)

    def test_orden_fifo(self):
        c = Cola()
        for x in (1, 2, 3):
            c.encolar(x)
        self.assertEqual([c.desencolar() for _ in range(3)], [1, 2, 3])

    def test_desencolar_vacia_lanza_error(self):
        with self.assertRaises(IndexError):
            Cola().desencolar()


if __name__ == "__main__":
    unittest.main()
