from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.TextField()
    # ForeignKey - allows many to one relation - one author can post may blog
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    body = models.TextField()

    def __str__(self):
        return self.title
