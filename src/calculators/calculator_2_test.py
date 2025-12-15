from .calculator_2 import Calculator2
from typing import Dict, List




class MockRequest:
    def __init__(self, body : Dict) -> None:
        self.json = body


def test_calculate():
    calculator_2 = Calculator2()
    mock_request = MockRequest(body = {"numbers" : [1,2,3]})
    result = calculator_2.calculate(mock_request)
    print()
    print(result)



    assert isinstance(result, dict)

    assert "data" in result
    assert "calculator" in result['data']
    assert "result" in result['data']