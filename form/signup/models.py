from django.db import models

# Create your models here.

class UserProfile(models.Model):

    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.IntegerField()
    cpassword = models.IntegerField()


