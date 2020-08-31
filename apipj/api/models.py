from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    mapPoint = models.CharField(blank=True, null=True, max_length=50)

    def __str__(self):
        return self.title