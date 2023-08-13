from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from app_mailing.forms import MailingForm
from app_mailing.models import Mailing


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
