from flask import Blueprint, abort, jsonify
import database.models as models

books = Blueprint('books', __name__)

# ######################
#  BOOK ENDPOINTS       #
# ######################


@books.route('/api/search', methods=['GET'])
def search():
    """
    Retrieve `SIZE_LIMIT` book records based on `q` param
    -----------------------------------------------------

    Endpoints:
      GET /search?q={book_isbn_or_book_title}

    @QueryParams:
      q: (required) query

    @Response:
      books: return `SIZE_LIMIT` books that macth the query
      next: url to list the next `SIZE_LIMIT` book records

    """
    abort(404)
    return f'search in database'


@books.route('/api/books', methods=['GET'])
def get_books():
    """
    Retrieve `SIZE_LIMIT` available book records
    -------------------------------------------

    Endpoints:
      GET /books
      GET /books?lastid={last_book_id}

    @QueryParams:
      lastid: (optional) last book id to implement forward paging system

    @Response:
      books: return `SIZE_LIMIT` books
      next: url to list the next `SIZE_LIMIT` book records

    """
    return 'get book'


@books.route('/api/books', methods=['POST'])
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


@books.route('/api/books/<string:isbn>', methods=['GET'])
def get_book(isbn):
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

    return f'Retrieve book record isbn:{isbn}'


@books.route('/api/books/<string:isbn>', methods=['PUT'])
def update_book(isbn):
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

    return f'update book ISBN: {isbn}'


@books.route('/api/books/<string:isbn>', methods=['DELETE'])
def remove_book(isbn):
    """
    Update a specific book record by it's ISBN 
    ------------------------------------------

    Endpoints:
      DELETE /books/isbn

    @Response:
      200: return book id

    """

    return f'delete book isbn: {isbn}'
