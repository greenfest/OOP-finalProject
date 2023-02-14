from model import CalculatorModel
from view import CalculatorView
from controller import CalculatorController

model = CalculatorModel()
view = CalculatorView()
controller = CalculatorController(model, view)

controller.run()