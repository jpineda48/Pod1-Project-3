from django.db import models
from django.urls import reverse

from django.contrib.auth.models import User

from django.db.models import Model

# Create your models here.

class GiftIdeas(models.Model):
    ideas= models.TextField(max_length=250)

    def __str__(self):
        return(self.ideas)
    
    def get_absolute_url(self):
        return reverse('birthdays_detail', kwargs={'pk': self.id})
    

class Birthday(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    date =models.DateField('birthday')
    relationship =models.CharField(max_length=50, null=True, blank=True)
    address =models.CharField(max_length=200, null=True, blank=True)
    phone_number = models.CharField(max_length=50, null=True, blank=True)
    email =models.CharField(max_length=50, null=True, blank=True)
    delivery_method=models.TextField(max_length=250, null=True, blank=True)
    alert = models.CharField(max_length=50, null=True, blank=True)

    ideas = models.ManyToManyField(GiftIdeas)

    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.first_name}'s birthday"
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'birthday_id': self.id})

    
    

    
