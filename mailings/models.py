from django.db import models
from django.utils import timezone


# pip3 install psycopg2-binary
# py manage.py migrate
# py manage.py makemigrations


class Client(models.Model):
    email = models.EmailField(verbose_name="E-mail")
    name = models.CharField(max_length=64, verbose_name="Name")
    surname = models.CharField(max_length=64, verbose_name="Surname")
    comment = models.TextField(verbose_name="Comment")

    def __str__(self):
        return f"{self.name} {self.surname} --- {self.email}"

    class Meta:
        verbose_name = "Client"
        verbose_name_plural = "Clients"
        ordering = ("email",)


class Message(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='messages', verbose_name="Client", null=True)
    # pokud je odstraněn Client, měly by být odstraněny i všechny související zprávy v MailingMessage.

    subject = models.CharField(max_length=256, verbose_name="E-mail subject")
    body = models.TextField(verbose_name="E-mail body")

    class Meta:
        verbose_name = "Mailing message"
        verbose_name_plural = "Mailing messages"


class Settings(models.Model):
    PERIODICITY_CHOICES = [  # CapsLock
        ("daily", "Once a day"),  # Prvním prvkem každého tuplu je skutečná hodnota,
        ("weekly", "Once a week"),  # která má být nastavena v modelu,
        ("monthly", "Once a month")  # a druhým prvkem je lidsky čitelný název.
    ]

    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='settings', verbose_name="Client")

    mailing_time = models.TimeField(verbose_name="Mailing time")
    periodicity = models.CharField(max_length=12, choices=PERIODICITY_CHOICES, verbose_name="Periodicity")
    mailing_status = models.CharField(max_length=24, verbose_name="Mailing status")

    class Meta:
        verbose_name = "Settings"
        verbose_name_plural = "Settings"

# class MailingLog(models.Model):
#     mailing_list = models.ForeignKey(MailingList, on_delete=models.CASCADE)
#
#     date_time = models.DateTimeField(default=timezone.now, verbose_name="Date & Time")
#     status = models.CharField(max_length=24, verbose_name="Status")
#     server_response = models.TextField(verbose_name="Server response")
#
#     class Meta:
#         verbose_name = "Mailing log"
#         verbose_name_plural = "Mailing logs"
