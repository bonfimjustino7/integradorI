from models import fields
from models.db import Model


class BaseModel(object):
    id = fields.IntegerField(primary_key=True, auto_increment=True)

    def __init__(self):
        self.model = Model()

    def all(self):
        return self.model.all(db_name=self.Meta.db_name)

    def get(self):
        return self.model.get(db_name=self.Meta.db_name)

    def filter(self, **kwargs):
        return self.model.filter(db_name=self.Meta.db_name, **kwargs)

    def save(self, **kwargs):
        self.model.save(db_name=self.Meta.db_name, **kwargs)

    def create_table(self):
        lista = []
        atributos = vars(self.__class__)
        for attr in atributos:
            if not attr.startswith('_') and not attr == 'Meta':
                lista.append(f"{attr} " + str(getattr(self, attr)))
        sql = ' , '.join(lista)
        query = f"CREATE TABLE {self.Meta.db_name} ({sql})"
        self.model.create_table(query)
