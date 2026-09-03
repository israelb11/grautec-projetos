# Pede o dia / pede o mes / pede o ano / Verificar se a data é valida

class DataValidator:
    def __init__(self):
            self.day: 0
            self.mouth = 0
            self.year = 0
            self.leapYear = 0

    def receiveData(self):
        self.day = int(input("Digite o dia: "))
        self.mouth = int(input("Digite o mês: "))
        self.year = int(input("Digite o ano: "))
        self.leapYear = self.year % 4

    # def validateData(self):

    # Validação ano bisexto
        if (self.mouth == 2):
            if (self.leapYear != 0) and (self.day > 28):
                print("ERROR! DATA INVALIDA!")
                print("Este ano não é bisexto, os dias de fevereiro vão somente até 28.")
                print("Insira uma data valida.")
                return
            if (self.leapYear == 0) and (self.day > 29):
                print("ERROR! DATA INVALIDA!") 
                print("Este ano é bisexto, os dias de fevereiro vão somente até 29.")
                print("Insira uma data valida.")

        if (self.day > 31) or (self.day < 1):
            print("ERROR! DATA INVALIDA!")
            print("Não existe nenhum mês que possua esse dia preenchido.")
            print("Insira uma data valida.")
            return
        
        if (self.mouth > 12):
            print("ERROR! DATA INVALIDA!")
            print("Não existe esse mês!")
            print("Insira uma data valida.")
            return
        
        if (self.year < 1):
            print("ERROR! DATA INVALIDA!")
            print("Não existe ano negativo.")
            print("Insira uma data valida.")
            return

    # def showResult(self):
        print(f"""{self.day}/{self.mouth}/{self.year}""")
        print("Ano bisexo" if (self.leapYear == 0) else "Ano não bisexto")

        print(type(self.day))
        print(type(self.mouth))
        print(type(self.year))

testaData = DataValidator()
testaData.receiveData()
# testaData.validateData()
# testaData.showResult()