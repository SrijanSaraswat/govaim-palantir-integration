from django.db import models
class DataConnection(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    connection_string = models.TextField()
