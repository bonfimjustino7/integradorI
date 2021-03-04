import MySQLdb

hostname = 'localhost'
username = 'root'
password = '123'
database = 'loja'


class SingletonMeta(type):
    """
    The Singleton class can be implemented in different ways in Python. Some
    possible methods include: base class, decorator, metaclass. We will use the
    metaclass because it is best suited for this purpose.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """

        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Model(metaclass=SingletonMeta):
    """
        Aqui fica todas as manipulações de SQL
    """
    def __init__(self):
        self._connection = MySQLdb.connect(host=hostname, user=username, passwd=password, db=database)
        self._cursor = self._connection.cursor(MySQLdb.cursors.DictCursor)
        print('Conexão Iniciada.')

    def all(self, **kwargs):
        db_name = kwargs.pop('db_name')
        self._cursor.execute(f"Select * from {db_name}")
        return self._cursor.fetchall()

    def get(self, **kwargs):
        db_name = kwargs.pop('db_name')
        self._cursor.execute(f"Select * from {db_name} LIMIT 1")
        return self._cursor.fetchall()

    def save(self, **kwargs):
        try:
            db_name = kwargs.pop('db_name')
            args_keys = ' ,'.join(kwargs.keys())
            args_values = ", ".join('"%s"' % n for n in kwargs.values())
            sql = f"INSERT INTO {db_name} ({args_keys}) VALUES ({args_values})"
            self._cursor.execute(sql)
            self._connection.commit()
        except MySQLdb.DatabaseError as error:
            print(error)
            self._connection.rollback()

    def filter(self, **kwargs):
        db_name = kwargs.pop('db_name')
        args = []
        for key, value in kwargs.items():
            args.append('%s="%s"' % (key, value))

        args = ' and '.join(args)
        try:
            sql = f"SELECT * from {db_name} WHERE {args}"
            self._cursor.execute(sql)
            return self._cursor.fetchall()
        except MySQLdb.DatabaseError as error:
            print(error)
            return ()

    def close(self):
        print('Close Connection')
        self._connection.close()