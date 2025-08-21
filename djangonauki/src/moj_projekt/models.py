from django.db import models
#from django.utils import timezone

class Item(models.Model):
    content = models.TextField()
#    date_posted = models.DateTimeField(default=timezone.now)
