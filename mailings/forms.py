from django import forms

from mailings.models import Client, Message, Settings


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = "__all__"


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = "__all__"


class SettingsForm(forms.ModelForm):
    class Meta:
        model = Settings
        exclude = ("mailing_status",)
