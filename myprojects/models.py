from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=200)
    language = models.CharField(max_length=100)
    desc = models.CharField(max_length=500)

    def __str__(self):
        return self.name