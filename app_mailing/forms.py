from django import forms

from app_mailing.models import Mailing, Message


class MailingForm(forms.ModelForm):
    class Meta:
        model = Mailing
        fields = '__all__'


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = '__all__'
