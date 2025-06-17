from django.db import models
class Workflow(models.Model):
    name = models.CharField(max_length=100)
    definition = models.JSONField()
    status = models.CharField(max_length=50)
