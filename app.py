from flask import Flask
from flask_restful import Api
from myapi.resources.foo import Foo


app = Flask(__name__)
api = Api(app)

api.add_resource(Foo, '/Foo')
