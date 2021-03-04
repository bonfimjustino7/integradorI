from gui.login.form import LoginForm
from models.db import Model

if __name__ == "__main__":
    db = Model()
    app = LoginForm()
    app.show()
    db.close()
