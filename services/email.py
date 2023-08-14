from django.core.mail import send_mail
from django.conf import settings

import random


def get_verification_code() -> str:
    code = "".join([str(random.randint(1, 9)) for i in range(4)])
    return code


def send_registration_email(user_email: str, verification_code: str):
    send_mail(
        'Завершение регистрации',
        f'Добро пожаловать {user_email}! \n'
        f'Для окончания регистрации пройдите по ссылке:\n'
        f'http://localhost:8000/users/verify/{verification_code}',
        settings.EMAIL_HOST_USER,
        [user_email]
    )


def send_recover_password_email(user_email: str, new_password: str):
    send_mail(
        'Завершение регистрации',
        f'Изменение пароля для {user_email}! \n'
        f'Новый пароль для входа: {new_password}',
        settings.EMAIL_HOST_USER,
        [user_email]
    )
