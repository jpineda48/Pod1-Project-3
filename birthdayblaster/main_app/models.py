from django.db import models
from django.urls import reverse

# Create your models here.

class GiftIdeas(models.Model):
    ideas= models.TextField(max_length=250)

    def __str__(self):
        return(self.ideas)
    
    def get_absolute_url(self):
        return reverse('birthdays_detail', kwargs={'pk': self.id})
    

class Birthday(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date =models.DateField('birthday')
    relationship =models.CharField(max_length=50)
    address =models.CharField(max_length=200)
    phone_number = models.CharField(max_length=50)
    email =models.CharField(max_length=50)
    delivery_method=models.TextField(max_length=250)
    alert =models.CharField(max_length=50)

    ideas = models.ManyToManyField(GiftIdeas)


    def __str__(self):
        return f"{self.first_name}'s birthday"
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'birthday_id': self.id})

    
    

    
