from src.drivers.numpy_handler import NumpyHandler
from .calculator_4 import Calculator4
from typing import Dict, List
from pytest import raises
from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface
from src.errors.error_controller import handle_errors




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
        return 1

    def variance(self,  numbers : List[float]) -> float:
        return 1


def test_calculate():
    calculator_4 = Calculator4(MockDriverHandler())

    mock_request = MockRequest(body = {"numbers" : [5,5,5,5,5]})

    result = calculator_4.calculate(mock_request)
    print(result)
    print("Sucesso")



    assert "data" in result 
    assert result == {'data': {'calculator': 4, 'value': 5.0, 'success': True}}

    print()

def test_calculate_with_list_Len_error():
    try:
        calculator_4 = Calculator4(MockDriverHandler())

        mock_request = MockRequest(body = {"numbers" : []})

        result = calculator_4.calculate(mock_request)
        print(result)
        print("Sucesso")

    except Exception as exception:
        error_response = handle_errors(exception)
        print()
        print(error_response['body'])


    assert str(error_response["body"]["errors"][0]["detail"]) == "Invalid request body : not enough numbers to calculate average."
