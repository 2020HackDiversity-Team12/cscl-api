import random
from faker import Faker
from faker.providers import BaseProvider
import helpers

fake = Faker()


class Provider(BaseProvider):

    ''' Doctype '''

    def book(self):
        MAX_COPIES = 5
        book = {
            'isbn': self.generator.isbn10(''),
            'title': self.generator.sentence(),
            'author': self.generator.name(),
            'publisher': self.generator.company(),
            'image_url_s': 'https://placeimg.com/48/75/any',
            'image_url_m': 'https://placeimg.com/100/160/any',
            'image_url_l': 'https://placeimg.com/350/500/any',
            'copies': MAX_COPIES,
            'available': self.generator.random_int(min=0, max=MAX_COPIES),
            'publication_year': self.generator.year()
        }
        return book


fake.add_provider(Provider)
