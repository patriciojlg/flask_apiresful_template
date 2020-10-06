from flask_restful import Resource
from flask import jsonify

class Foo(Resource):
    def get(self):
        return jsonify({"Método":"GET"})
    def post(self):
        return jsonify({"Método":"POST"})

