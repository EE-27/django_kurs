from django.urls import path

from mailings.views import index

urlpatterns = [
    path("", index),
]
