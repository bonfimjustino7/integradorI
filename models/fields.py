
class Field(object):
    def __init__(self, **kwargs):
        self.max_length = kwargs.get('max_length', 255)
        self.primary_key = kwargs.get('primary_key')
        self.null = kwargs.get('null')


class StringField(Field):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._type = 'VARCHAR'

    def __repr__(self):
        sql = f"{self._type} ({self.max_length}) "
        if not self.null:
            sql += 'NOT NULL'
        else:
            sql += 'NULL'
        return sql


class IntegerField(Field):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._type = 'INT'
        self.auto_increment = kwargs.get('auto_increment')

    def __repr__(self):
        sql = f"{self._type} "
        if not self.null:
            sql += 'NOT NULL '
        else:
            sql += 'NULL '

        if self.primary_key:
            sql += 'PRIMARY KEY '
        if self.auto_increment:
            sql += 'AUTO_INCREMENT'
        return sql


