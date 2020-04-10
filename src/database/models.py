''' 
  MODELS MODULE
'''
from database import db


class Book(db.Document):
    isbn: db.StringField(required=True)
    title: db.StringField(required=True)tr
    author: db.StringField(required=True)
    publisher: db.StringField(required=True)
    image_url_s: db.URLField()
    image_url_m: db.URLField()
    image_url_l: db.URLField()
    copies: db.IntField(default=0)
    available: db.IntField(default=0)
    publication_year: db.IntField(required=True)
