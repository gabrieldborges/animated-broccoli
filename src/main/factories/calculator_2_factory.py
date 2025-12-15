from src.calculators.calculator_2 import Calculator2
from src.drivers.numpy_handler import NumpyHandler

def calculator_2_factory():
    driver = NumpyHandler()
    calc = Calculator2(driver)
    return calc