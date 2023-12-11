from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, DetailView, UpdateView, DeleteView

from mailings.models import Client


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
    model = Client
    template_name = "mailings/client_confirm_delete.html"

    def get_success_url(self):
        """ come back to client list view """
        return reverse('client_list_view')
