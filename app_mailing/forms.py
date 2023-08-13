from django import forms

from app_mailing.models import Mailing, Message, Client


class MailingForm(forms.ModelForm):
    class Meta:
        model = Mailing
        fields = '__all__'


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = '__all__'


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
