from models.base import BaseModel

"""
    Aqui fica todos as classes models
"""


class User(BaseModel):
    class Meta:
        db_name = 'user'


class Client(BaseModel):
    class Meta:
        db_name = 'client'
