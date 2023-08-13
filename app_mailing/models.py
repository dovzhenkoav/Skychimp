from django.db import models

from app_users.models import User


NULLABLE = {'blank': True, 'null': True}


class Client(models.Model):
    email = models.EmailField(max_length=50, verbose_name='почта')
    full_name = models.CharField(max_length=128, verbose_name='фио')
    comment = models.TextField(**NULLABLE, verbose_name='комментарий')

    def __str__(self):
        return f'{self.email} {self.full_name}'

    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'


class Message(models.Model):
    """Mailing message that sends to users."""
    title = models.CharField(max_length=128, verbose_name='заголовок')
    body = models.TextField(verbose_name='тело сообщения')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Создатель')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'сообщение'
        verbose_name_plural = 'сообщения'


class Mailing(models.Model):
    """Mailing settings."""
    PERIODICITY_CHOICES = [
        ('day', 'раз в день'),
        ('week', 'раз в неделю'),
        ('month', 'раз в месяц')
    ]
    PERIODICITY_STATUS = [
        ('stopped', 'завершена'),
        ('created', 'создана'),
        ('launched', 'запущена')
    ]

    time = models.TimeField(verbose_name='время рассылки')
    periodicity = models.CharField(max_length=5,
                                   choices=PERIODICITY_CHOICES,
                                   verbose_name='периодичность')
    status = models.CharField(max_length=8,
                              choices=PERIODICITY_STATUS,
                              verbose_name='статус', default='created')
    message = models.ForeignKey(Message, on_delete=models.CASCADE, verbose_name='сообщение')
    recipients = models.ManyToManyField(Client, verbose_name='клиенты')

    def __str__(self):
        return f'{self.time}--{self.periodicity}--{self.status}: {self.message}'

    class Meta:
        verbose_name = 'рассылка'
        verbose_name_plural = 'рассылки'


class MailingTry(models.Model):
    """Mailing try."""
    MAILING_TRY_STATUS = [
        ('OK', 'Выполнено'),
        ('Err', 'Ошибка')
    ]

    mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE, verbose_name='рассылка')
    try_datetime = models.DateTimeField(auto_now_add=True, verbose_name='время попытки')
    try_status = models.CharField(max_length=3,
                                  choices=MAILING_TRY_STATUS,
                                  verbose_name='статус')
    mail_service_response = models.TextField(verbose_name='ответ почтового сервиса')

    def __str__(self):
        return f'{self.try_datetime}--{self.try_status}--{self.mailing}: {self.mail_service_response}'

    class Meta:
        verbose_name = 'попытка рассылки'
        verbose_name_plural = 'попытки рассылки'
