__author__ = 'jc.cerquera10@uniandes.edu.co'


class Calculadora:
    def __init__(self):
        print("constructor")

    def sumar(self, cadena):
        print("sumar: " + cadena)
        if cadena and cadena.strip():
            return 1
        else:
            return 0