class Calculadora:
    def __init__(self):
        # Inicialização dos atributos que serão compartilhados entre as funções
        self.num1 = 0
        self.num2 = 0
        self.operator = ""
        self.result = 0.0

    def pedir_dados(self):
        """1. Solicita e armazena os dois números e o operador."""
        self.num1 = float(input("Digite o primeiro número: "))
        self.operator = input("Digite o símbolo (+, -, *, /): ")
        self.num2 = float(input("Digite o segundo número: "))

    def calcular(self):
        """2. Executa a operação matemática correspondente."""
        if self.operator == "+":
            self.result = self.num1 + self.num2
        elif self.operator == "-":
            self.result = self.num1 - self.num2
        elif self.operator in ("*", "x"):
            self.result = self.num1 * self.num2
        elif self.operator == "/":
            if self.num2 != 0:
                self.result = self.num1 / self.num2
            else:
                print("Erro: Divisão por zero!")
                self.result = None
        else:
            print("Operador inválido!")
            self.result = None

    def exibir_resultado(self):
        """3. Exibe o resultado calculado."""
        if self.result is not None:
            print(f"O resultado de {self.num1} {self.operator} {self.num2} é: {self.result}")


# --- Execução ---
# 1. Cria a instância (executa o __init__)
calc = Calculadora()

# 2. Chama as 3 funções na ordem desejada
calc.pedir_dados()
calc.calcular()
calc.exibir_resultado()