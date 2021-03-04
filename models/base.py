from models.db import Model


class BaseModel(object):
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