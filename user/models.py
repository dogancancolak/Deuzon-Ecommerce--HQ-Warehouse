from django.db import models

# Create your models here.



class User(models.Model):

    email = models.CharField(max_length=30, default="nil", null=True)
    username = models.CharField(max_length=30, default="nil", null=True)
    password = models.CharField(max_length=30, default="nil", null=True)
    isAdmin = models.BooleanField(default=False)
