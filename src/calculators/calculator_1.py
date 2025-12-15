from flask import request as FlaskRequest
from typing import Dict


class Calculator1:
    '''
    Um número é dividido em 3 partes iguais;

    A primeira parte é dividida por 4 e seu resultado somado a 7.
    Após isso, o resultado é elevado ao quadrado e multiplicado por um valor de 0.257.

    DONE

    A segunda parte é elevada a potência de 2.121 , dividida por 5 e somado a 1. 

    A terceira parte se mantem no mesmo valor. 
    
    '''



    def calculate(self, request : FlaskRequest) -> Dict:
        body = request.json
        input_data = self.__validate_body(body)

        splited_number = input_data / 3

        first_process_result = self.__first_process(splited_number)
        second_process_result = self.__second_process(splited_number)
        third_process_result = splited_number

        calc_result = first_process_result + second_process_result + third_process_result

        result = self.__format_result(calc_result)

        return result



        print(input_data)
        print(first_process_result)


    def __validate_body(self, body : Dict) -> float :
        if "number" not in body :
            raise Exception ("Invalid request body")

        input_data = body["number"]
        return input_data

    def __first_process(self, first_number : float) -> float:
        first_part = (first_number / 4) + 7
        second_part = (first_part ** 2) * 0.257
        return second_part

    def __second_process(self, second_number: float) ->float : 
        first_part = (second_number ** 2.121)
        second_part = (first_part / 5) + 1
        return second_part

    def __format_result(self, calc_result : float) -> Dict :
        return {
            "data" : {
                "calculator" : 1 , 
                "result" : round(calc_result, 2)
            }
        }