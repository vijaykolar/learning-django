from django.db import models

# Create your models here.


class Post(models.Model):
    text = models.TextField()
    id = models.IntegerField(primary_key=True)

    def __str__(self):
        return self.text
