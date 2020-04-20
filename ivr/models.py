from django.db import models


# Create your models here.
class Session(models.Model):
    session_id = models.CharField(max_length=50)
    caller_number = models.CharField(max_length=20)
    dtmfDigits = models.CharField(max_length=10)
    recordingUrl = models.CharField(max_length=100)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.caller_number

