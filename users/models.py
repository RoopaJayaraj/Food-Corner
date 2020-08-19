from django.db import models
from django.contrib.auth.models import User

class Address(models.Model):
    street_address = models.CharField(max_length=50, blank=False)
    city = models.CharField(max_length= 50)
    state = models.CharField(max_length=20)
    zipcode = models.IntegerField()
    
    

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    address = models.ManyToManyField(Address)

    def get_address_list(self):
        return self.address.all()






