import unittest
import prender


class Testing(unittest.TestCase):

    def test_ciclo_normal(self):

        self.assertEqual(prender.ciclo_normal(), None)

    def test_ciclo_interrupcion(self):

        self.assertEqual(prender.ciclo_interrupcion(), None)

    def test_inicializar(self):

        self.assertEqual(prender.inicializar(), None)

if __name__ == "__main__":
    unittest.main()