__author__ = 'jc.cerquera10@uniandes.edu.co'


class Calculadora:
    def __init__(self):
        print("constructor")

    def sumar(self, cadena):
        print("sumar: " + cadena)
        if cadena and cadena.strip():
            array = cadena.split(",")
            if len(array) > 1 and len(array) <= 3:
                if len(array) == 2:
                    numero1 = int(array[0])
                    numero2 = int(array[1])
                    total = numero1 + numero2
                    return total
                elif len(array) == 3:
                    numero1 = int(array[0])
                    numero2 = int(array[1])
                    numero3 = int(array[2])
                    total = numero1 + numero2 + numero3
                    return total
            else:
                return cadena
        else:
            return 0
