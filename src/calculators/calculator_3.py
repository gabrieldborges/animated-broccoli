from audioop import mul
from typing import Dict, List
from flask import request as FlaskRequest

from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface
'''
N número são enviados;

Caso a variância de todos esses números for menor que 
a multiplicação deles, é apresentado uma informação de sucesso ao usuário.

Caso contrário, é apresentado uma informação de falha.  



'''

class Calculator3 :
    def __init__(self, driver_handler : DriverHandlerInterface) -> None:
        self.__driver_handler = driver_handler

    def calculate(self, request : FlaskRequest) -> Dict:
        body = request.json
        input_data = self.__validate_body(body)

        variance = self.__calculate_variance(input_data)
        multiplication = self.__calculate_multiplication(input_data)

        self.__verify_result(variance , multiplication)

        formated_result = self.__format_result(variance)
        
        return formated_result
        



    def __validate_body(self, body : Dict) -> List[float]:
        if "numbers" not in body :
            raise Exception("Invalid request body")

        input_data = body['numbers']
        return input_data

    
    def __calculate_variance(self, numbers: List[float]) -> float:
        variance = self.__driver_handler.variance(numbers)
        return variance

    def __calculate_multiplication(self, numbers : List[float]) -> float:
        multiplication = 1
        for num in numbers: multiplication *= num
        return multiplication
            
    def __verify_result(self, variance : float , multiplication : float) -> None:
        if variance <  multiplication :
            raise Exception("Process failed : variance is lower than the multiplication value.")
        else :
            print("Success!!!!")

    
    def __format_result(self, variance : float) -> Dict :
        return {
            "data" : {
                "calculator" : 3 , 
                "value" : float(variance) , 
                "success" : True
            }
        }