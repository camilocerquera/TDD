from unittest import TestCase
from Calculadora import Calculadora

__author__ = 'jc.cerquera10@uniandes.edu.co'


class TestCalculadora(TestCase):
    def test_sumar(self):
        return

    def test_sumar_cadenaVacia(self):
        self.assertEqual(Calculadora().sumar(""), 0, "cadena vacia")

    def test_sumar_unNumero(self):
        numero = "1"
        self.assertEqual(Calculadora().sumar(numero), numero, "un numero")

    def test_sumar_dosNumeros(self):
        self.assertEqual(Calculadora().sumar("1,2"), 3, "dos numeros")

    def test_sumar_tresNumeros(self):
        self.assertEqual(Calculadora().sumar("1,2,3"), 6, "tres numeros")

    def test_sumar_Nnumeros(self):
        self.assertEqual(Calculadora().sumar("1,2,3,4,5,6,7,8,9,10"), 55, "n numeros")
