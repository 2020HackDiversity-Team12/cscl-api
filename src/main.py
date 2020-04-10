import database
import database.models as models
import helpers
from flask import Flask, make_response, jsonify, abort
from werkzeug import exceptions as w_exceptions


app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
    'db': 'cscl_test',
    'host': 'localhost',
    'port': 27017
}

database.init(app)

# ###########################
#  HTTP ERROR HANDLER       #
# ###########################


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


# ######################
#  ENDPOINTS           #
# ######################

@app.route('/api/search', methods=['GET'])
def search():
    ''' '''
    pass


@app.route('/api/books', methods=['GET'])
def get_books():
    ''' '''
    pass


@app.route('/api/books', methods=['POST'])
def create_book():
    ''' '''
    pass


@app.route('/api/books/<string:book_id>', methods=['GET'])
def get_book(book_id):
    ''' '''
    pass


@app.route('/api/books/<string:book_id>', methods=['PUT'])
def update_book(book_id):
    ''' '''
    pass


@app.route('/api/books/<string:book_id>', methods=['DELETE'])
def remove_book(book_id):
    ''' '''
    pass
