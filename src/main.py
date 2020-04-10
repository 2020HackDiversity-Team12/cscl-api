import database
import service
import helpers
from flask import Flask, make_response, jsonify

app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
    'db': 'cscl_test',
    'host': 'localhost',
    'port': 27017
}

database.init(app)


# ERROR HANDLER
@app.errorhandler(404)
def resource_not_found(e):
    return make_response(
        jsonify({
            'status': 404,
            'text': 'resource not found'
        }), 404)


@app.errorhandler(405)
def method_not_allowed(e):
    return make_response(
        jsonify({
            'status': 405,
            'text': 'method not allowed'
        }), 405)


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


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="8000", debug=True)
