from django.shortcuts import render
from django.views.generic import ListView

from mailings.models import Client


# Create your views here.

# def index(request):
#     return render(request, "mailings/index.html")


class ClientListView(ListView):
    model = Client
    template_name = 'mailings/index.html'
