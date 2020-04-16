import database
import config
import resources
from flask import Flask, Blueprint, make_response, jsonify
from werkzeug import exceptions as w_exceptions

app = Flask(__name__)

app.config.from_object(config.ProdConfig)
app.register_blueprint(resources.books)

database.init(app)

############################
# CORS                     #
############################


@app.after_request
def add_headers(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Methods',
                         'GET, POST, PUT, DELETE')
    response.headers.add('Access-Control-Allow-Headers',
                         'x-requested-with,Content-Type')
    response.headers.add('Access-Control-Expose-Headers',
                         'Content-Type,Content-Length')
    return response


############################
# HTTP ERROR HANDLER       #
############################

@app.errorhandler(w_exceptions.BadRequest)
def bad_request(err):
    resp = jsonify({'status': err.code, 'text': 'bad request'})
    return make_response(resp, err.code)


@app.errorhandler(w_exceptions.NotFound)
def not_found(err):
    resp = jsonify({'status': err.code, 'text': 'resource not found'})
    return make_response(resp, err.code)


@app.errorhandler(w_exceptions.MethodNotAllowed)
def method_not_allowed(err):
    resp = jsonify({'status': err.code, 'text': 'method not allowed'})
    return make_response(resp, err.code)
