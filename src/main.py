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
    """
     Retreive `SIZE_LIMIT` book records based on `q` param
     -----------------------------------------------------

     Endpoints:
        GET /search?q={book_isbn_or_book_title}

     @QueryParams:
        q: (required) query 

     @Response:
        books: return `SIZE_LIMIT` books that macth the query
        next: url to list the next `SIZE_LIMIT` book records
    """

    return f'search in database'


@app.route('/api/books', methods=['GET'])
def get_books():
    """
     Retreive `SIZE_LIMIT` book records 
     ----------------------------------

      Endpoints:
        GET /books
        GET /books?lastid={last_book_id}

     @QueryParams:
        lastid: (optional) last book id to implement forward paging system

     @Response:
        books: return `SIZE_LIMIT` books
        next: url to list the next `SIZE_LIMIT` book records
    """

    return 'Retreive n book records '


@app.route('/api/books', methods=['POST'])
def create_book():
    """
     Create a book record 
     --------------------

     Endpoints:
        POST /books

     @BodyParams:
        isbn: int
        title: str
        author: str
        publisher: str
        publication_year: str
        copies: int

     @Response:
        200: return book ID
    """

    return 'create book record'


@app.route('/api/books/<string:book_id>', methods=['GET'])
def get_book(book_id):
    """
     Retrieve a specific book record by it's ISBN 
     ---------------------------------------------

     Endpoints:
        GET /books/isbn
        GET /books/isbn?act=(borrow|handback) 

     @QueryParams: 
        act: (optional) specific action on book 
             Possible values: borrow, handback 

     @Response:
        200: return book record

    """

    return f'Retrieve book record isbn:{book_id}'


@app.route('/api/books/<string:book_id>', methods=['PUT'])
def update_book(book_id):
    """
     Update a specific book record by it's ISBN 
     ------------------------------------------

     Endpoints:
        PUT /books/isbn

     @BodyParams:
        isbn: int
        title: str
        author: str
        publisher: str
        publication_year: str
        copies: int
        available: int
        image_url_s: url
        image_url_m: url
        image_url_l: url

     @Response:
        200: return book id
    """

    return f'update book ISBN: {book_id}'


@app.route('/api/books/<string:book_id>', methods=['DELETE'])
def remove_book(book_id):
    """
     Update a specific book record by it's ISBN 
     ------------------------------------------

     Endpoints:
        DELETE /books/isbn

     @Response:
        200: return book id
    """

    return f'delete book isbn: {book_id}'
