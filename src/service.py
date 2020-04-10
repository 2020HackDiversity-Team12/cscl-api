from database.models import Book


def drop():
    pass


def get_all():
    ''' '''
    return Book.objects()


def get(isbn):
    ''' '''
    return Book.objects(isbn=isbn)


def create(book):
    ''' '''

    return Book(**book).save()


def update(isbn, **kwargs):
    ''' '''
    return get(isbn).update(**kwargs)
