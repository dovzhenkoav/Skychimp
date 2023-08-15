from django.urls import path

from app_manager import views


app_name = 'app_manager'

urlpatterns = [
    path('mailings/', views.ManagerMailingListView.as_view(), name='mailing_list'),
    path('mailings/stop_mailing/<int:pk>', views.stop_mailing_view, name='stop_mailing'),
    path('clients/', views.ManagerClientListView.as_view(), name='client_list'),
    path('clients/ban_user/<int:pk>', views.ban_user_view, name='ban_user'),
]
