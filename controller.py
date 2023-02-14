class CalculatorController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def run(self):
        self.model.set_number1(self.view.read_number("first number"))
        self.model.set_number2(self.view.read_number("second number"))
        operation = self.view.read_operation()

        if operation == "+":
            self.model.add()
        elif operation == "-":
            self.model.subtract()
        elif operation == "*":
            self.model.multiply()
        elif operation == "/":
            self.model.divide()

        self.view.display_result(self.model.result)