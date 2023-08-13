from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from app_mailing.forms import MailingForm, MessageForm, ClienteForm
from app_mailing.models import Mailing, Message, MailingTry, Client


def index(request):
    return render(request, template_name='app_mailing/index.html')


class MailingListView(generic.ListView):
    model = Mailing
    template_name = 'app_mailing/mailing_list.html'


class MailingDetailView(generic.DetailView):
    model = Mailing
    template_name = 'app_mailing/mailing_detail.html'


class MailingDeleteView(generic.DeleteView):
    model = Mailing
    success_url = reverse_lazy('app_mailing:mailing_list')
    template_name = 'app_mailing/mailing_delete.html'


class MailingCreateView(generic.CreateView):
    model = Mailing
    template_name = 'app_mailing/mailing_create.html'
    form_class = MailingForm
    success_url = reverse_lazy('app_mailing:mailing_list')


class MailingUpdateView(generic.UpdateView):
    model = Mailing
    template_name = 'app_mailing/mailing_create.html'
    form_class = MailingForm
    success_url = reverse_lazy('app_mailing:mailing_list')


class MessageListView(generic.ListView):
    model = Message
    template_name = 'app_mailing/message_list.html'


class MessageCreateView(generic.CreateView):
    model = Message
    template_name = 'app_mailing/message_create.html'
    form_class = MessageForm
    success_url = reverse_lazy('app_mailing:message_list')


class MessageUpdateView(generic.UpdateView):
    model = Message
    template_name = 'app_mailing/message_create.html'
    form_class = MessageForm
    success_url = reverse_lazy('app_mailing:message_list')


class MessageDeleteView(generic.DeleteView):
    model = Message
    success_url = reverse_lazy('app_mailing:message_list')
    template_name = 'app_mailing/message_delete.html'

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)


class ClientListView(generic.ListView):
    model = Client
    template_name = 'app_mailing/client_list.html'


class ClientCreateView(generic.CreateView):
    model = Client
    template_name = 'app_mailing/client_create.html'
    form_class = ClienteForm
    success_url = reverse_lazy('app_mailing:client_list')


