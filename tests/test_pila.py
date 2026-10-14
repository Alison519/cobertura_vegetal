import unittest
from tda.pila import Pila


class TestPila(unittest.TestCase):
    def test_pila_nueva_esta_vacia(self):
        self.assertTrue(Pila().esta_vacia())

    def test_apilar_y_tope(self):
        p = Pila()
        p.apilar(1)
        self.assertEqual(p.tope(), 1)
        self.assertEqual(p.tamanio(), 1)

    def test_orden_lifo(self):
        p = Pila()
        for x in (1, 2, 3):
            p.apilar(x)
        self.assertEqual([p.desapilar() for _ in range(3)], [3, 2, 1])

    def test_desapilar_vacia_lanza_error(self):
        with self.assertRaises(IndexError):
            Pila().desapilar()

    def test_tope_no_elimina(self):
        p = Pila()
        p.apilar("a")
        p.tope()
        self.assertEqual(p.tamanio(), 1)


if __name__ == "__main__":
    unittest.main()
