from django.db import models


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    photo = models.ImageField(blank=True)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

class Comment(models.Model):
    post = models.ForeignKey(Blog, on_delete=models.CASCADE, null=True, related_name='comments')
    contents = models.CharField(max_length = 200)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.contents
