from models.objects import User, Client


def get_users(id, nome):
    user = User().filter(id=id, nome=nome)
    return user is not ()
