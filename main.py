from interfaces.main.form import MainForm
from models.db import Model

if __name__ == "__main__":
    db = Model()
    app = MainForm()
    app.show()
    db.close()
