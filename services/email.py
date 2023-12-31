from django.core.mail import send_mail
from django.conf import settings

import random


def get_verification_code() -> str:
    """Generates four-digits verification code."""
    code = "".join([str(random.randint(1, 9)) for i in range(4)])
    return code


def send_registration_email(user_email: str, verification_code: str):
    """Send email after user registration to confirm email and activate user profile."""
    send_mail(
        'Завершение регистрации',
        f'Добро пожаловать {user_email}! \n'
        f'Для окончания регистрации пройдите по ссылке:\n'
        f'http://localhost:8000/users/verify/{verification_code}',
        settings.EMAIL_HOST_USER,
        [user_email]
    )


def send_recover_password_email(user_email: str, new_password: str):
    """Send email to setup new user password."""
    send_mail(
        'Завершение регистрации',
        f'Изменение пароля для {user_email}! \n'
        f'Новый пароль для входа: {new_password}',
        settings.EMAIL_HOST_USER,
        [user_email]
    )


def send_mailing_message(title: str, body: str, recipients: list['str']):
    """Main sender. Sends mailing messages to user."""
    send_mail(
        f'{title}',
        f'{body}',
        settings.EMAIL_HOST_USER,
        recipients
    )
