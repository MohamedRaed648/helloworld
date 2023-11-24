from django.db import models

# Create your models here.


class post(models.Model):
    post=models.TextField()
    def __str__(self):
        return self.post[0:50]