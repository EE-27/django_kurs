from django.urls import path

from mailings.views import ClientListView, index, ClientDetailView

urlpatterns = [
    path("", index),
    path("client_list_view/", ClientListView.as_view(), name='client_list_view'),
    path("client_detail/<int:pk>/", ClientDetailView.as_view(), name="client_detail")
]
