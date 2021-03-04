from models.objects import User


def get_users(login, password):
    user = User().filter(login=login, password=password)
    return user is not ()
