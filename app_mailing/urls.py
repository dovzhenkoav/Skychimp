from django.urls import path
from django.views.decorators.cache import cache_page

from app_mailing import views

app_name = 'app_mailing'

urlpatterns = [
    path('', cache_page(0)(views.index), name='index'),
    path('mailing/', views.MailingListView.as_view(), name='mailing_list'),
    path('mailing/<int:pk>', views.MailingDetailView.as_view(), name='mailing_detail'),
    path('mailing/delete/<int:pk>', views.MailingDeleteView.as_view(), name='mailing_delete'),
    path('mailing/create/', views.MailingCreateView.as_view(), name='mailing_create'),
    path('mailing/update/<int:pk>', views.MailingUpdateView.as_view(), name='mailing_update'),
    path('mailing_try/<int:pk>', views.MailingTryListView.as_view(), name='mailing_try_list'),

    path('mailing/message/', views.MessageListView.as_view(), name='message_list'),
    path('mailing/message/create/', views.MessageCreateView.as_view(), name='message_create'),
    path('mailing/message/update/<int:pk>', views.MessageUpdateView.as_view(), name='message_update'),
    path('mailing/message/delete/<int:pk>', views.MessageDeleteView.as_view(), name='message_delete'),

    path('mailing/client/', views.ClientListView.as_view(), name='client_list'),
    path('mailing/client/create/', views.ClientCreateView.as_view(), name='client_create'),
    path('mailing/client/update/<int:pk>', views.ClientUpdateView.as_view(), name='client_update'),
    path('mailing/client/delete/<int:pk>', views.ClientDeleteView.as_view(), name='client_delete'),
]
