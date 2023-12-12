from django.contrib import admin

from mailings.models import Client, Message, Settings


# py manage.py createsuperuser UN:admin PW:12345

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'surname', 'comment')
    list_filter = ('name', 'surname')
    search_fields = ('email', 'name', 'surname')


@admin.register(Settings)
class MailingListAdmin(admin.ModelAdmin):
    list_display = ('mailing_time', 'periodicity', 'mailing_status')
    search_fields = ('mailing_time', 'periodicity', 'mailing_status')
    list_filter = ('mailing_time', 'periodicity', 'mailing_status')


@admin.register(Message)
class MailingMessageAdmin(admin.ModelAdmin):
    list_display = ( 'subject', 'body')
    search_fields = ('subject', 'body')

# @admin.register(MailingLog)
# class MailingLogAdmin(admin.ModelAdmin):
#     list_display = ('mailing_list', 'date_time', 'status', 'server_response')
#     list_filter = ('date_time', 'status')
#     search_fields = ('date_time', 'status', 'server_response')
