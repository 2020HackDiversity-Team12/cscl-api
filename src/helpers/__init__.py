from .fakedata import fake

FAKE_DATA_LIMIT = 1


def fake_book(limit=FAKE_DATA_LIMIT, **kwargs):
    return [fake.book(**kwargs) for i in range(limit)]
