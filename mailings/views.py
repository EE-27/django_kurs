from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, DetailView, UpdateView

from mailings.models import Client


# Create your views here.

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
        return reverse('client_list_view')
