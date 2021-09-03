from django.db import models
from django.db.models.fields import TextField

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_created',]
    def __str__(self):
        return self.title

    def snippest(self):
        text = "continue reading"
        return self.body[:50]+'...'+ text