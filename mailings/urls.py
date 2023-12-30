from django.urls import path
from mailings.views import index, SettingsListView, SettingsCreateView, send_email_to_client, success, no_success

from mailings.views import ClientListView, ClientDetailView, ClientUpdateView, ClientDeleteView, ClientCreateView
from mailings.views import MessageListView, MessageDetailView, MessageUpdateView, MessageDeleteView, MessageCreateView

urlpatterns = [
    path("", index),

    path("client_list_view/", ClientListView.as_view(), name='client_list_view'),
    path("client_detail/<int:pk>/", ClientDetailView.as_view(), name="client_detail"),
    path("client_update/<int:pk>/", ClientUpdateView.as_view(), name="client_update"),
    path("client_delete/<int:pk>/", ClientDeleteView.as_view(), name="client_delete"),
    path("client_create/", ClientCreateView.as_view(), name="client_create"),

    path("message_list_view/", MessageListView.as_view(), name='message_list_view'),
    path("message_detail/<int:pk>/", MessageDetailView.as_view(), name="message_detail"),
    path("message_update/<int:pk>/", MessageUpdateView.as_view(), name="message_update"),
    path("message_delete/<int:pk>/", MessageDeleteView.as_view(), name="message_delete"),
    path("message_create/", MessageCreateView.as_view(), name="message_create"),

    path("settings_list_view/", SettingsListView.as_view(), name="settings_list_view"),
    path("settings_create/", SettingsCreateView.as_view(), name="settings_create"),

    path('send_email/<int:client_id>/', send_email_to_client, name='send_email_to_client'),
    path("email_success/", success, name='success'),
    path("email_no_success/", no_success, name='no success'),
]
