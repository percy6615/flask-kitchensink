from __future__ import unicode_literals

from dotenv import load_dotenv
from werkzeug.middleware.proxy_fix import ProxyFix
from argparse import ArgumentParser
from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from flask_jwt_extended import JWTManager
from flask_cache import Cache

import os
load_dotenv()
from app.controller.line_controller_pro import LineControllerPro, StaticPathController, FuckController

basedirs = os.path.abspath(os.path.dirname(__file__))
basedir = basedirs + '/cache'

# app = Flask(__name__, static_url_path="/images", static_folder="./images/")
app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_host=1, x_proto=1)
CORS(app)
jwt = JWTManager(app)
# 設定 JWT 密鑰
app.config['JWT_SECRET_KEY'] = 'this-should-be-change'

# api = Api(app, resources={r"/api/*": {"origins": "*"}})
cache = Cache(app, config={'CACHE_TYPE': 'filesystem', 'CACHE_DIR': basedir})
api = Api(app)
# api.add_resource(LineController, '/webhooks/line', resource_class_kwargs={'static_tmp_path': static_tmp_path})
api.add_resource(LineControllerPro, '/webhooks/line')
api.add_resource(StaticPathController, '/static/<path:path>')
api.add_resource(FuckController, '/fuck')
if __name__ == '__main__':
    arg_parser = ArgumentParser(
        usage='Usage: python ' + __file__ + ' [--port <port>] [--help]'
    )
    arg_parser.add_argument('-p', '--port', type=int, default=8000, help='port')
    arg_parser.add_argument('-d', '--debug', default=False, help='debug')
    options = arg_parser.parse_args()
    # app.run(host='0.0.0.0', port=8000, debug=True)
    app.run(host='0.0.0.0', debug=options.debug, port=options.port)
