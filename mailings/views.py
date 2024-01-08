from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.utils import timezone
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView

from mailings.models import Client, Message, Settings, Log


def index(request):
    logs = Log.objects.all()
    context = {"logs": logs}
    return render(request, "mailings/index.html", context)


def success(request):
    return render(request, "mailings/email_success.html")


def no_success(request):
    return render(request, "mailings/email_no_success.html")


### Client
class ClientListView(ListView):
    """ show all Clients """
    model = Client
    template_name = 'mailings/client_list_view.html'


def send_email_to_client(request, client_id):
    client = get_object_or_404(Client, pk=client_id)

    messages = client.messages.all()
    settings = client.settings.all()

    if request.method == 'POST':
        selected_message_id = request.POST.get('selected_message')
        selected_setting_id = request.POST.get('selected_setting')
        # settings_obj = client.settings.get()  # dostat setting pro clienta
        # start_date = settings_obj.start_date  # datum kdy se to zadalo
        # days_passed = (timezone.now().date() - start_date).days  # dnešní datum - dny kdy se to zadalo
        # periodicity = settings_obj.periodicity  # jestli: daily, weekly nebo monthly
        if selected_message_id and selected_setting_id:
            selected_message = get_object_or_404(Message, id=selected_message_id)
            selected_setting = get_object_or_404(Settings, id=selected_setting_id)
            periodicity = selected_setting.periodicity
            start_date = selected_setting.start_date
            days_passed = (timezone.now().date() - start_date).days
            if periodicity == 'daily':
                send_e_mail(client, selected_message, selected_setting)
                return redirect("success")

            elif periodicity == 'weekly':
                if days_passed % 7 == 0:
                    send_e_mail(client, selected_message, selected_setting)
                    return redirect("success")
                else:
                    return redirect("no success")

            elif periodicity == 'monthly':  # srát na jinak dlouhý měsíce monthly je prostě 30 dní
                if days_passed % 30 == 0:  # bacha 0 / 30 == 0, takže se to pošle i dneska
                    send_e_mail(client, selected_message, selected_setting)
                    return redirect("success")
                else:
                    return redirect("no success")

    context = {'client': client, 'messages': messages, 'settings': settings}
    return render(request, 'mailings/send_email_form.html', context)


def send_e_mail(client, selected_message, selected_settings):
    subject = selected_message.subject
    body = selected_message.body

    send_mail(
        f"{subject}",
        f"{body}",
        settings.EMAIL_HOST_USER,
        [client.email]
    )
    log_entry = Log.objects.create(
        client=client,
        status="finished",
        server_response="Email sent successfully",
        email_subject=subject,
        email_body=body
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

        searched_client = Client.objects.filter(name=client.name, surname=client.surname).first()

        if searched_client:
            send_email_to_client(searched_client)
            return render(request, 'mailings/email_sent.html')

    context = {'client': client}
    return render(request, 'mailings/client_detail.html', context)
