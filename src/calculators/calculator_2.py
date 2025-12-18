from typing import List , Dict
from flask import request as FlaskRequest
from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface
from src.errors.http_unprocessable_entity import HttpUnprocessableEntity



class Calculator2 :
    '''
    N número são enviados;

    Todos esses N numeros são multiplicados por 11 e elevados a potencia de 0.95;

    Por fim, é retirado o desvio padrão desses resultados e retornado o inverso desse valor (1/result) ; 
    
    
    '''
    def __init__(self, driver_handler : DriverHandlerInterface) -> None:
        self.__driver_handler = driver_handler
        pass
    
    def calculate(self, request : FlaskRequest) -> Dict:  #type : ignore
        body = request.json
        input_data = self.__validate_body(body)
        calculated_number = self.__process_data(input_data)
       
        formated_result = self.__format_result(calculated_number)
        return formated_result
        
    def __validate_body(self, body : Dict) -> List[float]:
        if "numbers" not in body :
            raise HttpUnprocessableEntity("Invalid request body")

        input_data = body['numbers']
        return input_data


    def __process_data(self, input_data : List[float]) -> float  :
        
        
        first_process_result = [((number * 11) ** 0.95 ) for number in input_data]
        
        result = self.__driver_handler.standard_derivation(first_process_result)
       
        return 1/result

        

    def __format_result(self, calculated_result : float) -> Dict :
        return {
            "data" : {
                "calculator" : 2 , 
                "result" : float(calculated_result)
            }
        }