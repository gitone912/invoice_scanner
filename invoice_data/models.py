from django.db import models

# Create your models here.
from django.db import models

class Invoice(models.Model):
    image = models.ImageField(upload_to='invoices/')
    scheduled_time = models.DateTimeField()
