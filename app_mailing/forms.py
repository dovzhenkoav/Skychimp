from django import forms

from app_mailing.models import Mailing, Message, Client


class MailingForm(forms.ModelForm):
    """Form for mailing create/update."""
    class Meta:
        model = Mailing
        exclude = ['author']


class MessageForm(forms.ModelForm):
    """Form for message create/update."""
    class Meta:
        model = Message
        exclude = ['author']


class ClienteForm(forms.ModelForm):
    """Form for client create/update."""
    class Meta:
        model = Client
        exclude = ['author']
