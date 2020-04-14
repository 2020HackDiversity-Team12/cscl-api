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
