from django.db import models

class Analysis(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
