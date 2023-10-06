class Calculadora:
    def _init_(self):
        pass

    def suma(self, num1, num2):
        return num1 + num2

    def resta(self, num1, num2):
        return num1 - num2

    def multiplicacion(self, num1, num2):
        return num1 * num2

    def division(self, num1, num2):
        if num2 == 0:
            return "Error: No se puede dividir por cero"
        else:
            return num1 / num2

def main():
    calc = Calculadora()
    while True:
        print("Opciones:")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Salir")
        
        opcion = input("Elije una opción (1/2/3/4/5): ")

        if opcion == '5':
            print("Saliendo de la calculadora.")
            break

        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))

        if opcion == '1':
            print("Resultado: ", calc.suma(num1, num2))
        elif opcion == '2':
            print("Resultado: ", calc.resta(num1, num2))
        elif opcion == '3':
            print("Resultado: ", calc.multiplicacion(num1, num2))
        elif opcion == '4':
            print("Resultado: ", calc.division(num1, num2))
        else:
            print("Opción no válida. Por favor, elija una opción válida.")

