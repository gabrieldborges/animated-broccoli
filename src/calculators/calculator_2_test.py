from .calculator_2 import Calculator2
from typing import Dict, List
from src.drivers.numpy_handler import NumpyHandler
from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface



class MockRequest:
    def __init__(self, body : Dict) -> None:
        self.json = body

class MockDriverHandler(DriverHandlerInterface):

    def standard_derivation(self, numbers : List[float] ) -> float:
        return 3



def test_calculate_integration():
    driver = MockDriverHandler()
    calculator_2 = Calculator2(driver)
    mock_request = MockRequest(body = {"numbers" : [1,2,3]})
    result = calculator_2.calculate(mock_request)
    print()
    print(result)

    assert result["data"]["result"] == 1/3
    assert isinstance(result, dict)
    assert "data" in result
    assert "calculator" in result['data']
    assert "result" in result['data']

    
    
    
    
def test_calculate():
    driver = NumpyHandler()
    calculator_2 = Calculator2(driver)
    mock_request = MockRequest(body = {"numbers" : [1,2,3]})
    result = calculator_2.calculate(mock_request)
    print()
    print(result)



    assert isinstance(result, dict)
    assert "data" in result
    assert "calculator" in result['data']
    assert "result" in result['data']