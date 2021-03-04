from models import fields
from models.base import BaseModel

"""
    Aqui fica todos as classes models
"""


class User(BaseModel):
    login = fields.StringField(max_length=200)
    password = fields.StringField(max_length=200)

    class Meta:
        db_name = 'user'


class Product(BaseModel):
    nome = fields.StringField(max_length=200)

    class Meta:
        db_name = 'product'
