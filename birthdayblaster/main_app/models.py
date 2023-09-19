from django.db import models
from django.urls import reverse

from django.contrib.auth.models import User

from django.db.models import Model

# Create your models here.

class GiftIdea(models.Model):
    ideas= models.TextField(max_length=250, blank=True)

    def __str__(self):
        return(self.ideas)
    
    def get_absolute_url(self):
        return reverse('gifts_detail', kwargs={'pk': self.id})
    

class Birthday(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True)
    date =models.DateField('birthday')
    relationship =models.CharField(max_length=50, blank=True)
    address =models.CharField(max_length=200, blank=True)
    phone_number = models.CharField(max_length=50, blank=True)
    email =models.CharField(max_length=50, blank=True)
    delivery_method=models.TextField(max_length=250, blank=True)
    alert = models.CharField(max_length=50, blank=True)

    ideas = models.ManyToManyField(GiftIdea, blank=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.first_name}'s birthday"
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'birthday_id': self.id})
    

class Photo(models.Model):
    url = models.CharField(max_length=200)
    birthday = models.ForeignKey(Birthday, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for birthday_id: {self.birthday_id} @{self.url}"

    
    

    
