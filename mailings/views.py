from django.shortcuts import render
from django.views.generic import ListView, DetailView

from mailings.models import Client


# Create your views here.

def index(request):
    return render(request, "mailings/index.html")


class ClientListView(ListView):
    model = Client
    template_name = 'mailings/client_list_view.html'


class ClientDetailView(DetailView):
    model = Client
    template_name = "mailings/client_detail.html"
