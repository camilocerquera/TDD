from unittest import TestCase
from Calculadora import Calculadora

__author__ = 'jc.cerquera10@uniandes.edu.co'


class TestCalculadora(TestCase):
    def test_sumar(self):
        return

    def test_sumar_cadenaVacia(self):
        self.assertEqual(Calculadora().sumar(""), 0, "cadena vacia")