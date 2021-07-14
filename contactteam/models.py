from django.db import models
from datetime import datetime
# Create your models here.

class ContactTeam(models.Model):
    full_name = models.CharField(max_length=225)
    phone = models.IntegerField()
    email = models.CharField(max_length=225)
    company_name = models.CharField(max_length=225)
    subject = models.CharField(max_length=225)
    message = models.CharField(max_length=225)
    contact_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name