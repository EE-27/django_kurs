from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView

from mailings.models import Client, Message


def index(request):
    return render(request, "mailings/index.html")


class ClientListView(ListView):
    """ show all Clients """
    model = Client
    template_name = 'mailings/client_list_view.html'


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


###
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
