from django.urls import path

from mailings.views import ClientListView

urlpatterns = [
    path("", ClientListView.as_view(), name='index'),
]
