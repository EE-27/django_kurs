from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.utils import timezone
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView

from mailings.models import Client, Message, Settings


def index(request):
    return render(request, "mailings/index.html")


### Client
class ClientListView(ListView):
    """ show all Clients """
    model = Client
    template_name = 'mailings/client_list_view.html'


def send_email_to_client(request, client_id):
    client = get_object_or_404(Client, pk=client_id)

    if request.method == 'POST':
        settings_obj = client.settings.get()  # dostat setting pro clienta
        start_date = settings_obj.start_date  # datum kdy se to zadalo
        days_passed = (timezone.now().date() - start_date).days  # dnešní datum - dny kdy se to zadalo
        periodicity = settings_obj.periodicity  # jestli: daily, weekly nebo monthly

        if periodicity == 'daily':
            send_e_mail(client)
            return HttpResponse("SEND")

        elif periodicity == 'weekly':
            if days_passed % 7 == 0:
                send_e_mail(client)
                return HttpResponse("SEND")
            else:
                return HttpResponse("IT HAS NOT BEEN A WEEK")

        elif periodicity == 'monthly':  # srát na jinak dlouhý měsíce monthly je prostě 30 dní
            if days_passed % 30 == 0:   # bacha 0 / 30 == 0, takže se to pošle i dneska
                send_e_mail(client)
                return HttpResponse("SEND")
            else:
                return HttpResponse("IT HAS NOT BEEN A MONTH")

    context = {'client': client}
    return render(request, 'mailings/send_email_form.html', context)


def send_e_mail(client):
    message = client.messages.latest('id')
    subject = message.subject
    body = message.body

    send_mail(
        f"{subject}",
        f"{body}",
        settings.EMAIL_HOST_USER,
        [client.email]
    )


class ClientDetailView(DetailView):
    """ show one Client """
    model = Client
    template_name = "mailings/client_detail.html"


class ClientUpdateView(UpdateView):
    """ update Client """
    model = Client
    fields = ("email", "name", "surname", "comment")
    template_name = "mailings/client_form.html"

    def get_success_url(self):
        """ come back to client list view """
        return reverse('client_list_view')


class ClientDeleteView(DeleteView):
    """ delete Client """
    model = Client
    template_name = "mailings/client_confirm_delete.html"

    def get_success_url(self):
        """ come back to client list view """
        return reverse('client_list_view')


class ClientCreateView(CreateView):
    """ create Client """
    model = Client
    fields = ("email", "name", "surname", "comment")
    template_name = "mailings/client_form.html"

    def get_success_url(self):
        """ come back to client list view """
        return reverse('client_list_view')


class MessageListView(ListView):
    """ show all Messages """
    model = Message
    template_name = 'mailings/message_list_view.html'


### Message
class MessageDetailView(DetailView):
    """ show one Message """
    model = Message
    template_name = "mailings/message_detail.html"


class MessageUpdateView(UpdateView):
    """ update Message """
    model = Message
    fields = ("subject", "body",)
    template_name = "mailings/message_form.html"

    def get_success_url(self):
        """ come back to message list view """
        return reverse('message_list_view')


class MessageDeleteView(DeleteView):
    """ delete Message """
    model = Message
    template_name = "mailings/message_confirm_delete.html"

    def get_success_url(self):
        """ come back to message list view """
        return reverse('message_list_view')


class MessageCreateView(CreateView):
    """ create Message """
    model = Message
    fields = ("subject", "body",)
    template_name = "mailings/message_form.html"

    def get_success_url(self):
        """ come back to message list view """
        return reverse('message_list_view')


### Setings
class SettingsListView(ListView):
    """ shows all settings"""
    model = Settings
    template_name = 'mailings/settings_list_view.html'


class SettingsCreateView(CreateView):
    model = Settings
    fields = "__all__"
    template_name = 'mailings/settings_form.html'

    def get_success_url(self):
        return reverse("settings_list_view")


def client_detail(request, client_id):
    client = get_object_or_404(Client, pk=client_id)

    if request.method == 'POST' and 'send_email' in request.POST:
        # Assuming you have a function to search for a client by name and surname
        # Modify this based on your actual database schema
        searched_client = Client.objects.filter(name=client.name, surname=client.surname).first()

        if searched_client:
            # Assuming you have a function to send an email
            send_email_to_client(searched_client)
            return render(request, 'mailings/email_sent.html')

    context = {'client': client}
    return render(request, 'mailings/client_detail.html', context)
