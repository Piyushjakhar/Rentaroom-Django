from django.db import models

# Create your models here.
class User(models.Model):
    user_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)

    def __str__(self):
        return self.user_name

class Property(models.Model):
    property_name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    owner_name = models.CharField(max_length=200)
    phone_no = models.CharField(max_length=200)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.property_name