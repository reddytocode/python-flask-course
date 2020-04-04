# init app
from flask import Flask

from flask_restful import Api

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('db/db_config.py')
    return app

def init_api(app):
    api = Api(app)
    from .resource.Login import Login
    from .resource.Suma import Suma
    from .resource.Register import Register
    
    api.add_resource(Login, "/auth/login")
    api.add_resource(Suma, "/suma")
    api.add_resource(Register, "/auth/register")