__author__ = 'jc.cerquera10@uniandes.edu.co'


class Calculadora:
    def __init__(self):
        print("constructor")

    def sumar(self, cadena):
        print("sumar: " + cadena)
        if cadena and cadena.strip():
            cadena = cadena.replace(":", ",")
            array = cadena.split(",")
            if len(array) > 1:
                total = 0
                for x in array:
                    total+=int(x)
                return total
            else:
                return cadena
        else:
            return 0
