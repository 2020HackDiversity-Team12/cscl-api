import random
import string
from .fakedata import fake

FAKE_DATA_LIMIT = 1


def build_response(payload, response=None):
    json = {}
    json['meta'] = {'succes': True, 'message': ''}
    json['payload'] = payload
    return json


def fake_book(limit=FAKE_DATA_LIMIT, **kwargs):
    return [fake.book(**kwargs) for i in range(limit)]


def random_string(length):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))
