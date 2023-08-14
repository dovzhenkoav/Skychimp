from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from app_mailing.forms import MailingForm, MessageForm, ClienteForm
from app_mailing.models import Mailing, Message, MailingTry, Client


def index(request):
    return render(request, template_name='app_mailing/index.html')


class MailingListView(LoginRequiredMixin, generic.ListView):
    login_url = reverse_lazy('app_users:login')
    redirect_field_name = "redirect_to"

    model = Mailing
    template_name = 'app_mailing/mailing_list.html'

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(author=self.request.user)
        return queryset


class MailingDetailView(LoginRequiredMixin, generic.DetailView):
    login_url = reverse_lazy('app_users:login')
    redirect_field_name = "redirect_to"

    model = Mailing
    template_name = 'app_mailing/mailing_detail.html'


class MailingDeleteView(LoginRequiredMixin, generic.DeleteView):
    login_url = reverse_lazy('app_users:login')
    redirect_field_name = "redirect_to"

    model = Mailing
    success_url = reverse_lazy('app_mailing:mailing_list')
    template_name = 'app_mailing/mailing_delete.html'


class MailingCreateView(LoginRequiredMixin, generic.CreateView):
    login_url = reverse_lazy('app_users:login')
    redirect_field_name = "redirect_to"

    model = Mailing
    template_name = 'app_mailing/mailing_create.html'
    form_class = MailingForm
    success_url = reverse_lazy('app_mailing:mailing_list')

    def form_valid(self, form):
        if form.is_valid():
            new_form = form.save()
            new_form.author = self.request.user
            new_form.save()
        return super().form_valid(form)

    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)
        form.fields['recipients'].queryset = Client.objects.filter(
            author=self.request.user
        )
        return form


class MailingUpdateView(LoginRequiredMixin, generic.UpdateView):
    login_url = reverse_lazy('app_users:login')
    redirect_field_name = "redirect_to"

    model = Mailing
    template_name = 'app_mailing/mailing_create.html'
    form_class = MailingForm
    success_url = reverse_lazy('app_mailing:mailing_list')


class MessageListView(LoginRequiredMixin, generic.ListView):
    login_url = reverse_lazy('app_users:login')
    redirect_field_name = "redirect_to"

    model = Message
    template_name = 'app_mailing/message_list.html'

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(author=self.request.user)
        return queryset


class MessageCreateView(LoginRequiredMixin, generic.CreateView):
    login_url = reverse_lazy('app_users:login')
    redirect_field_name = "redirect_to"

    model = Message
    template_name = 'app_mailing/message_create.html'
    form_class = MessageForm
    success_url = reverse_lazy('app_mailing:message_list')

    def form_valid(self, form):
        if form.is_valid():
            new_form = form.save()
            new_form.author = self.request.user
            new_form.save()
        return super().form_valid(form)


class MessageUpdateView(LoginRequiredMixin, generic.UpdateView):
    login_url = reverse_lazy('app_users:login')
    redirect_field_name = "redirect_to"

    model = Message
    template_name = 'app_mailing/message_create.html'
    form_class = MessageForm
    success_url = reverse_lazy('app_mailing:message_list')


class MessageDeleteView(LoginRequiredMixin, generic.DeleteView):
    login_url = reverse_lazy('app_users:login')
    redirect_field_name = "redirect_to"

    model = Message
    success_url = reverse_lazy('app_mailing:message_list')
    template_name = 'app_mailing/message_delete.html'


class ClientListView(LoginRequiredMixin, generic.ListView):
    login_url = reverse_lazy('app_users:login')
    redirect_field_name = "redirect_to"

    model = Client
    template_name = 'app_mailing/client_list.html'

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(author=self.request.user)
        return queryset


class ClientCreateView(LoginRequiredMixin, generic.CreateView):
    login_url = reverse_lazy('app_users:login')
    redirect_field_name = "redirect_to"

    model = Client
    template_name = 'app_mailing/client_create.html'
    form_class = ClienteForm
    success_url = reverse_lazy('app_mailing:client_list')

    def form_valid(self, form):
        if form.is_valid():
            new_form = form.save()
            new_form.author = self.request.user
            new_form.save()
        return super().form_valid(form)


class ClientUpdateView(LoginRequiredMixin, generic.UpdateView):
    login_url = reverse_lazy('app_users:login')
    redirect_field_name = "redirect_to"

    model = Client
    template_name = 'app_mailing/client_update.html'
    form_class = ClienteForm
    success_url = reverse_lazy('app_mailing:client_list')


class ClientDeleteView(LoginRequiredMixin, generic.DeleteView):
    login_url = reverse_lazy('app_users:login')
    redirect_field_name = "redirect_to"

    model = Client
    success_url = reverse_lazy('app_mailing:client_list')
    template_name = 'app_mailing/client_delete.html'
