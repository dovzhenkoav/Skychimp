from django.contrib import admin

from app_mailing.models import Client, Mailing, Message, MailingTry


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    """Register clients model in django admin."""
    list_display = ('email', 'full_name', 'comment')
    list_filter = ('email',)
    search_fields = ('email', 'full_name', 'comment')


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    """Register mailing model in django admin."""
    list_display = ('name', 'time', 'periodicity', 'status')
    list_filter = ('time', 'periodicity', 'status')
    search_fields = ('name', 'message',)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    """Register message model in django admin."""
    list_display = ('title', 'body')
    list_filter = ('title', 'body')
    search_fields = ('title', 'body')


@admin.register(MailingTry)
class MailingTryAdmin(admin.ModelAdmin):
    """Register mailing try model in django admin."""
    list_display = ('mailing', 'try_datetime', 'try_status', 'mail_service_response')
    list_filter = ('mailing', 'try_datetime', 'try_status')
    search_fields = ('mail_service_response',)
