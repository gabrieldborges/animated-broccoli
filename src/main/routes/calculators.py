from flask import Blueprint, jsonify , request
from src.calculators.calculator_1 import Calculator1
from src.main.factories.calculator_2_factory import calculator_2_factory
from src.main.factories.calculator_1_factory import calculator_1_factory


calc_route_bp = Blueprint("calc_routes", __name__)

@calc_route_bp.route("/calculator/1", methods=['POST'])
def calculator_1() :
    calc = calculator_1_factory()
    result = calc.calculate(request)
 
    return jsonify(result), 200



@calc_route_bp.route("/calculator/2", methods=['POST'])
def calculator_2() :
    calc = calculator_2_factory()   

    result = calc.calculate(request)
 
    return jsonify(result), 200

