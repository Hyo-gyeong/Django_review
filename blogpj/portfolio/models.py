from django.db import models

class Portfolio(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    body = models.TextField()
    date = models.DateTimeField('date published')

    def __str__(self):
        return self.title
    
    def summ(self):
        return self.body[:50]