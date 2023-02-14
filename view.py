class CalculatorView:
    def read_number(self, number_name):
        return float(input(f"Enter {number_name}: "))

    def read_operation(self):
        return input("Enter operation (+, -, *, /): ")

    def display_result(self, result):
        print(f"Result: {result}")