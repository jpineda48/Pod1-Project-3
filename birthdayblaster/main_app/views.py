

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView 
from django.views.generic import ListView, DetailView

from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from.models import Birthday, GiftIdea, Photo

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
  id_list = birthday.ideas.all().values_list('id')
  ideas_to_add = GiftIdea.objects.exclude(id__in=id_list)
  print(id_list)
  

  return render(request, 'birthdays/detail.html', { 'birthday': birthday, 'ideas':ideas_to_add })


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
  fields = ['first_name', 'last_name', 'date', 'relationship', 'address', 'phone_number', 'email', 'delivery_method', 'alert']
  # fields = '__all__'

  def form_valid(self, form):
    form.instance.user = self.request.user 
    return super().form_valid(form)
  
  

class BirthdayUpdate(LoginRequiredMixin, UpdateView):
  model = Birthday
  # Let's disallow the renaming of a cat by excluding the name field!
  fields = ['first_name', 'last_name', 'date', 'relationship', 'address', 'phone_number', 'email', 'delivery_method', 'alert']

class BirthdayDelete(LoginRequiredMixin, DeleteView):
  model = Birthday
  success_url = '/birthdays'


class GiftList(LoginRequiredMixin, ListView):
   model=GiftIdea
   template_name= 'gifts/detail.html'

class GiftDetail(LoginRequiredMixin, DeleteView):
   model=GiftIdea

class GiftCreate(LoginRequiredMixin, CreateView):
   model= GiftIdea
   fields = '__all__'
   success_url = '/birthdays'

   def form_valid(self, form):
    form.instance.user = self.request.user 
    birthday_id = self.kwargs['birthday_id']
    new_gift= form.save(commit=False)
    print('FORM', new_gift)
    Birthday.objects.get(id=birthday_id).ideas.add(7
                                                   )
    # form.instance.ideas = self.request.birthday
    return super().form_valid(form)

class GiftUpdate(LoginRequiredMixin, UpdateView):
   model=GiftIdea
   fields= '__all__'
   success_url = '/gifts'


class GiftDelete(LoginRequiredMixin, DeleteView):
   model = GiftIdea
   success_url = '/gifts'
               

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


def assoc_idea(request, birthday_id, giftideas_id):
  # Note that you can pass a toy's id instead of the whole toy object
    Birthday.objects.get(id=birthday_id).ideas.add(giftideas_id)
    return redirect('detail', birthday_id=birthday_id)
