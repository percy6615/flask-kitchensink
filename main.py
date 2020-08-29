# from __future__ import unicode_literals
# import pandas as pd
# import json, requests
# # from database import sqlengine, Mysqls
# #
# # engine = sqlengine.create_ng_mysql()
#
#
# # url = 'http://api.finmindtrade.com/api/v3/data'
# # payload = {'dataset': 'FinancialStatements', 'stock_id': "2449","date": "2020-01-01"}
# # res = requests.get(url, verify=True, params=payload)
# # temp = res.json()
# # data = pd.DataFrame(temp['data'])
# # # data.to_sql(name='stock_fin_stat', con=engine, if_exists='append', index=False)
# # print(temp)
#
#
# # datajson={'data': [{'dateT': '2020-03-31', 'stock_id': '2449', 'type': 'ASSO', 'value': 3996000.0, 'origin_name': '採用權益法認列之關聯企業及合資損益之份額淨額'}]}
# #
# # data = pd.DataFrame(datajson['data'])
# #
# # data.to_sql(name='stock_fin_stat', con=engine, if_exists='append', index=False, chunksize = None)
#
# # mysqls = Mysqls()
# # checkSql = 'select 1 from disaster_userlist where userid=\'' + 'U46af7fe06da5a3705281d861e832bff' + '\' and CHANNELTOKEN=\'' + 'vNwfo4I31lehKReKXPbhhk7HdX2OYwebl/pGObq5/2ZDV6N1cPUeX5q6LE2X3OBWueLVPxCB2dQX+GOKp9YrpW/ShXwP01xyphW/z6hM3A9gmFCNjquY2lNdD9LzA9s/c6yRGuK8pROO28c9GzEQLAdB04t89/1O/w1cDnyilFU=' + '\''
# # print(len(mysqls.get(checkSql)))
#
#
#
#
# from dotenv import load_dotenv
# from werkzeug.middleware.proxy_fix import ProxyFix
# from argparse import ArgumentParser
# from flask import Flask, request, abort, render_template, make_response, Response
# from flask_cors import CORS
# from flask_restful import Api,Resource
# load_dotenv()
#
# import os
# class TemplateLine(Resource):
#     def __init__(self):
#         print()
#     def post(self):
#         print()
#     def get(self):
#         return Response(response=render_template('lineregister.html',name={'name':'percy'}))
#
# static_tmp_path = os.path.join(os.path.dirname(__file__), 'static', 'tmp')
# # app = Flask(__name__, static_url_path="/images", static_folder="./images/")
# app = Flask(__name__)
# app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_host=1, x_proto=1)
# CORS(app)
# # api = Api(app, resources={r"/api/*": {"origins": "*"}})
# api = Api(app)
#
# api.add_resource(TemplateLine, '/TemplateLine')
#
#
#
#
#
#
# if __name__ == '__main__':
#     arg_parser = ArgumentParser(
#         usage='Usage: python ' + __file__ + ' [--port <port>] [--help]'
#     )
#     arg_parser.add_argument('-p', '--port', type=int, default=8000, help='port')
#     arg_parser.add_argument('-d', '--debug', default=False, help='debug')
#     options = arg_parser.parse_args()
#     # app.run(host='0.0.0.0', port=8000, debug=True)
#     app.run(host='0.0.0.0', debug=options.debug, port=options.port)
#
var = 'delete from disaster_userlist where userid = %(eventSourceUserId)s and CHANNELTOKEN = %(channel_access_token)s'% ({"eventSourceUserId":"1","channel_access_token":"self.channel_access_token"})
print(var)