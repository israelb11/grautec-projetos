# Pedir dois numeros
# Pedir a opção (adição/substração/multiplicação/ divisão)
# Fazer calculo de acordo com a opção selecionada
# Imprimir resultado

class Calculadora:
    def __init__(self):
        self.num1 = 0.0
        self.num2 = 0.0
        self.operator = ""
        self.result = None

    # def __init__(self):
    def receiveData(self):
        self.num1 = float(input("Digite o primeiro número: "))
        self.operator = input("Digite o simbolo do calculo que será feito (+, -, *, /): ")
        self.num2 = float(input("Digite o segundo número: "))
        # return(num1, num2, operator)

    def calc(self):
        if self.operator  == "+":
            self.result = (self.num1 + self.num2)
        elif self.operator in ("*", "x"):
            self.result = (self.num1 * self.num2)
        elif self.operator  == "-":
            self.result = (self.num1 - self.num2)
        elif self.operator  == "/":
            self.result = (self.num1 / self.num2)

    def showResult(self):
            print(f"O resultado de {self.num1} {self.operator} {self.num2} é: {self.result}")
   
Calc = Calculadora()

Calc.receiveData()
Calc.calc()
Calc.showResult()