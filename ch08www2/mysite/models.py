from django.db import models


# Create your models here.

class Mood(models.Model):
    status = models.CharField(max_length=10, null=False)

    def __str__(self):
        return self.status


class Post(models.Model):
    mood = models.ForeignKey("Mood", on_delete=models.CASCADE)
    nickName = models.CharField(max_length=10, default="A mystery man")
    message = models.TextField(null=False)
    delPass = models.CharField(max_length=10, default="123")
    pubDate = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)

    def __str__(self):
        return self.message
