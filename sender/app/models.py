from django.db import models


class SentSMS(models.Model):
    phone_number = models.CharField(max_length=15)
    verification_code = models.CharField(max_length=6)
    sent_at = models.DateTimeField(auto_now_add=True)
