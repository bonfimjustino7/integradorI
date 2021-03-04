import MySQLdb

from gui.login.form import LoginForm
from models.db import Model
from models.objects import Product, User

if __name__ == "__main__":

    try:
        Product().create_table()
        User().create_table()
    except MySQLdb.DatabaseError:
        pass

    db = Model()
    app = LoginForm()
    app.show()
    db.close()
