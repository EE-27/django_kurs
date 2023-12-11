from django.urls import path

from mailings.views import ClientListView, index, ClientDetailView, ClientUpdateView

urlpatterns = [
    path("", index),
    path("client_list_view/", ClientListView.as_view(), name='client_list_view'),
    path("client_detail/<int:pk>/", ClientDetailView.as_view(), name="client_detail"),
    path("client_update/<int:pk>/", ClientUpdateView.as_view(), name="client_update"),
]
