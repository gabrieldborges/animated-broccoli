from typing import Dict, List
from flask import request as FlaskRequest
from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface
from src.errors.http_unprocessable_entity import HttpUnprocessableEntity
from src.errors.http_bad_request import HttpBadRequest


class Calculator4 :
    def __init__(self, driver_handler : DriverHandlerInterface) -> None:
        self.__driver_handler = driver_handler

    def calculate(self, request : FlaskRequest) -> Dict:
        body = request.json
        input_data = self.__validate_body(body)

        result = self.__calculate_average(input_data)

        formated_result = self.__format_result(result)

        return formated_result





    def __validate_body(self, body : Dict) -> List[float]:
        if "numbers" not in body:
            raise HttpUnprocessableEntity("Invalid request body")

        if len(body["numbers"]) == 0 :
            raise HttpUnprocessableEntity("Invalid request body : not enough numbers to calculate average.")

        
        input_data = body["numbers"]
        return input_data

    def __calculate_average(self, input_data : List[float]) -> float:
        sum = 0
        for num in input_data:
            sum += num
        average = sum/(len(input_data))
        return average

    def __format_result(self, result : float) -> Dict :
        return {
        "data" : {
            "calculator" : 4 , 
            "value" : float(result) , 
            "success" : True
                }
            }
        
