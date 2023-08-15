from django.shortcuts import redirect
from django.views import generic

from app_mailing.models import Mailing
from app_users.models import User


class ManagerMailingListView(generic.ListView):
    model = Mailing
    template_name = 'app_manager/mailing_list.html'


def stop_mailing_view(request, pk):
    mailing = Mailing.objects.get(pk=pk)
    mailing.status = 'stopped'
    mailing.save()
    return redirect('app_manager:mailing_list')


class ManagerClientListView(generic.ListView):
    model = User
    template_name = 'app_manager/client_list.html'


def ban_user_view(request, pk):
    user = User.objects.get(pk=pk)
    user.is_active = False
    user.save()
    return redirect('app_manager:client_list')
