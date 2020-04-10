import database
import service
from flask import Flask, make_response, jsonify

app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
    'host': 'localhost',
    'port': 27017
}

database.init(app)

book = {
    "isbn": "0195153448",
    "title": "Classical Mythology",
    "author": "Mark P. O. Morford",
    "publication_year": 2002,
    "publisher": "Oxford University Press",
    "image_url_s": "http://images.amazon.com/images/P/0195153448.01.THUMBZZZ.jpg",
    "image_url_m": "http://images.amazon.com/images/P/0195153448.01.MZZZZZZZ.jpg",
    "image_url_l": "http://images.amazon.com/images/P/0195153448.01.LZZZZZZZ.jpg",
    "copies": 2,
    "available": 0
}


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


# ###############
#  ENDPOINTS    #
# ###############
@app.route('/api/search', methods=['GET'])
def search():
    ''' '''

    return 'search'


@app.route('/api/books', methods=['GET'])
def get_books():
    ''' '''

    return 'all books'


@app.route('/api/books', methods=['POST'])
def create_book():
    ''' '''

    return jsonify(service.create(book))


@app.route('/api/books/<string:book_id>', methods=['GET'])
def get_book(book_id):
    ''' '''

    return f'get book id:{book_id}'


@app.route('/api/books/<string:book_id>', methods=['PUT'])
def update_book(book_id):
    ''' '''

    return f'update book id:{book_id}'


@app.route('/api/books/<string:book_id>', methods=['DELETE'])
def remove_book(book_id):
    ''' '''

    return f'remove book id:{book_id}'


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="8000", debug=True)
