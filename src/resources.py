from flask import Blueprint, abort, jsonify, request, Response
from database.models import Book
import helpers
import service
import re


books = Blueprint('books', __name__)

HOST = 'https://api-cscl.herokuapp.com'

# ######################
#  BOOK ENDPOINTS      #
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

    try:
        q = request.args.get("q")
        regex = re.compile(f'.*{q}.*')
        book = Book.objects(title=regex).limit(30)

        return jsonify(book)
    except:
        return jsonify({"Error": "Bad query"})


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

    books = None
    book_lastid = None
    param_lastid = request.args.get("lastid")

    if(param_lastid):
        books = Book.objects(id__lt=param_lastid).order_by("-_id").limit(30)
    else:
        books = Book.objects().order_by("-_id").limit(30)

    try:
        book_lastid = books[len(books) - 1].id
    except Exception:
        pass

    next = f'{HOST}/api/books?lastid={book_lastid}' if book_lastid else None
    return jsonify({'books': books, 'next': next})

# Validate books that are created by client (Should we require the images??????)


def ValidateBook(bookObject):
    if ("isbn" in bookObject and "title" in bookObject and "author" in bookObject and
            "publisher" in bookObject and "publication_year" in bookObject and "copies" in bookObject):
        return True
    else:
        return False


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
    entry = request.get_json()
    if ValidateBook(entry):
        newBook = {
            "isbn": entry["isbn"],
            "title": entry["title"],
            "author": entry["author"],
            "publisher": entry["publisher"],
            "publication_year": entry["publication_year"],
            "copies": entry["copies"],
            # "image_url_s": entry["image_url_s"],
            # "image_url_m": entry["image_url_m"],
            # "image_url_l": entry["image_url_l"]
        }
        newBook["available"] = newBook["copies"]
        Book(**newBook).save()
        return jsonify(newBook)
    else:
        return "Invalid Entry"


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
    try:
        book = Book.objects.get(isbn=isbn)
        if request.args.get("act") == "borrow":
            if book["available"] > 0:
                book["available"] -= 1
            else:
                return "This book is unavailable"
        elif request.args.get("act") == "handback":
            if book["available"] < book["copies"]:
                book["available"] += 1
            else:
                return "You can't adda new copy"
        book.save()
        return jsonify(book)
    except:
        return "We don't carry this book"


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
    entry = request.get_json()
    try:
        Book.objects.get(isbn=isbn).update(**entry)
        b = Book.objects.get(isbn=isbn)

        return jsonify(b)
    except:
        return jsonify({"Error": "Invalid Isbn or Invalid request"})


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
    try:
        book = Book.objects.get(isbn=isbn)
        isbn = book.isbn
        book.delete()
        return jsonify({'success': True, 'isbn': isbn})
    except:
        return jsonify({"Error": "Invalid isbn"})

    return "Book Has been deleted"


@books.route('/api/seed/<int:n>', methods=['GET'])
def seed_database(n):
    """
    POPULATE DB WITH FAKE DATA
    ------------------------------------------

    Endpoints:
      DELETE /seed/

    @Response:
      200: BOOKS CREATED

    """

    message = None

    try:
        books = helpers.fake_book(int(n))
        [service.create(book) for book in books]
        message = 'books created'
    except Exception:
        message = 'error while populating db'
    finally:
        return message
