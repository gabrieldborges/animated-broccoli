from src.drivers.numpy_handler import NumpyHandler
from .calculator_3 import Calculator3
from typing import Dict, List
from pytest import raises
from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface




class MockRequest:
    def __init__(self, body : Dict) -> None:
        self.json = body


class MockDriverHandlerError(DriverHandlerInterface):

    def standard_derivation(self, numbers : List[float] ) -> float:
        return 3

    def variance(self,  numbers : List[float]) -> float:
        return 3

class MockDriverHandler(DriverHandlerInterface):

    def standard_derivation(self, numbers : List[float] ) -> float:
        return 3

    def variance(self,  numbers : List[float]) -> float:
        return 10000







def test_calculate_with_variance_error():
    
    calculator_3 = Calculator3(MockDriverHandlerError())

    mock_request = MockRequest(body = {"numbers" : [1,2,3,4,5]})



    with raises(Exception) as excinfo:
        calculator_3.calculate(mock_request)

    assert str(excinfo.value) == "Process failed : variance is lower than the multiplication value."
    print()
    print(excinfo.value)

def test_calculate():
    
    calculator_3 = Calculator3(MockDriverHandler())

    mock_request = MockRequest(body = {"numbers" : [1,1,1,1,100]})

    result = calculator_3.calculate(mock_request)

    assert result == {'data': {'calculator': 3, 'value': 10000, 'success': True}}

    print()
    print(result)





    




    