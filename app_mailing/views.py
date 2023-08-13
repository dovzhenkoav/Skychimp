from django.shortcuts import render
from django.views import generic

from app_mailing.models import Mailing


def index(request):
    return render(request, template_name='app_mailing/index.html')


class MailingListView(generic.ListView):
    model = Mailing
    template_name = 'app_mailing/mailing_list.html'


class MailingDetailView(generic.DetailView):
    model = Mailing
    template_name = 'app_mailing/mailing_detail.html'
