import string
import random

from app_users.models import User
from services.email import send_recover_password_email


def create_password() -> str:
    """Creates 12-digits password."""
    password = ''
    password += ''.join([random.choice(string.digits) for i in range(3)])
    password += ''.join([random.choice(string.ascii_lowercase) for i in range(3)])
    password += ''.join([random.choice(string.ascii_uppercase) for i in range(3)])
    password += ''.join([random.choice(string.punctuation) for i in range(3)])
    return password


def user_set_random_password(user: User):
    """Sets new user password."""
    new_password = create_password()
    user.set_password(new_password)
    user.save()
    send_recover_password_email(user.email, new_password)


