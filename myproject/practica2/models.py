from django.db import models

# Create your models here.

class url_type (models.Model):
    url_long = models.TextField()
    url_short = models.TextField()
