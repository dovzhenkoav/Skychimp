from django.urls import path

from app_mailing import views

app_name = 'app_mailing'

urlpatterns = [
    path('', views.index, name='index'),
    path('mailing/', views.MailingListView.as_view(), name='mailing_list'),
    path('mailing/<int:pk>', views.MailingDetailView.as_view(), name='mailing_detail'),
    path('mailing/delete/<int:pk>', views.MailingDeleteView.as_view(), name='mailing_delete'),
    path('mailing/create/', views.MailingCreateView.as_view(), name='mailing_create'),
    path('mailing/update/<int:pk>', views.MailingUpdateView.as_view(), name='mailing_update'),
    path('mailing/message/', views.MessageList.as_view(), name='message_list'),
]
