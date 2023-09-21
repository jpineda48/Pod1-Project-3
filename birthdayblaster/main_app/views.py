

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView 
from django.views.generic import ListView, DetailView

from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from.models import Birthday, GiftIdea, Photo
from.forms import GiftIdeaForm

import uuid
import boto3
import os

#  -----------------------------------------

def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')

@login_required
def birthdays_index(request):
  birthdays= Birthday.objects.filter(user=request.user)
  # We pass data to a template very much like we did in Express!
  return render(request, 'birthdays/index.html', {
    'birthdays': birthdays
  })

@login_required
def birthdays_detail(request, birthday_id):
  birthday = Birthday.objects.get(id=birthday_id)
  giftidea_form = GiftIdeaForm()
  
  

  return render(request, 'birthdays/detail.html', { 'birthday': birthday, 'giftidea_form': giftidea_form})


def signup(request):
    error_message = ''
    if request.method == 'POST':
        # This is how to create a 'user' form object
        # that includes the data from the browser
        form = UserCreationForm(request.POST)
        if form.is_valid():
        # This will add the user to the database
            user = form.save()
        # This is how we log a user in via code
            login(request, user)
            return redirect('index')
    else:
        error_message = 'Invalid sign up - try again'
    # A bad POST or a GET request, so render signup.html with an empty form
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

#  CBVs -----------------------------------------

class BirthdayCreate(LoginRequiredMixin, CreateView):
  model = Birthday
  fields = ['first_name', 'last_name', 'date', 'relationship', 'address', 'phone_number', 'email', 'notes', 'alert']
  # fields = '__all__'

  def form_valid(self, form):
    form.instance.user = self.request.user 
    return super().form_valid(form)

class BirthdayUpdate(LoginRequiredMixin, UpdateView):
  model = Birthday
  # Let's disallow the renaming of a cat by excluding the name field!
  fields = ['first_name', 'last_name', 'date', 'relationship', 'address', 'phone_number', 'email', 'notes', 'alert']

class BirthdayDelete(LoginRequiredMixin, DeleteView):
  model = Birthday
  success_url = '/birthdays'            

# Create your views here.

def add_photo(request, birthday_id):
    # photo-file will be the "name" attribute on the <input type="file">
    photo_file = request.FILES.get('photo-file', None)
    AWS_ACCESS_KEY = os.environ['AWS_ACCESS_KEY']
    AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
    if photo_file:
        s3 = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY, aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
        # need a unique "key" for S3 / needs image file extension too
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        # just in case something goes wrong
        try:
            bucket = os.environ['S3_BUCKET']
            s3.upload_fileobj(photo_file, bucket, key)
            # build the full url string
            url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
            # we can assign to cat_id or cat (if you have a cat object)
            Photo.objects.create(url=url, birthday_id=birthday_id)
        except Exception as e:
            print('An error occurred uploading file to S3')
            print(e)
    return redirect('detail', birthday_id=birthday_id)

def add_giftidea(request, birthday_id):
  # create a ModelForm instance using the data in request.POST
  form = GiftIdeaForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the cat_id assigned
    new_giftidea= form.save(commit=False)
    new_giftidea.birthday_id = birthday_id
    new_giftidea.save()
  return redirect('detail', birthday_id=birthday_id)
