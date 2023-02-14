class CalculatorModel:
    def __init__(self):
        self.number1 = 0
        self.number2 = 0
        self.result = 0

    def set_number1(self, number1):
        self.number1 = number1

    def set_number2(self, number2):
        self.number2 = number2

    def add(self):
        self.result = self.number1 + self.number2

    def subtract(self):
        self.result = self.number1 - self.number2

    def multiply(self):
        self.result = self.number1 * self.number2

    def divide(self):
        if self.number2 == 0:
            raise ValueError("Cannot divide by zero")
        self.result = self.number1 / self.number2