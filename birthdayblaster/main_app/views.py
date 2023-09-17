from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView 
from django.views.generic import ListView, DetailView



from.models import Birthday, GiftIdeas


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')

def birthdays_index(request):
  birthdays= Birthday.objects.all()
  # We pass data to a template very much like we did in Express!
  return render(request, 'birthdays/index.html', {
    'birthdays': birthdays
  })

def birthdays_detail(request, birthday_id):
  birthday = Birthday.objects.get(id=birthday_id)
  return render(request, 'birthdays/detail.html', { 'birthday': birthday })

class BirthdayCreate(CreateView):
  model = Birthday
  fields = '__all__'

class BirthdayUpdate(UpdateView):
  model = Birthday
  # Let's disallow the renaming of a cat by excluding the name field!
  fields = '__all__'

class BirthdayDelete(DeleteView):
  model = Birthday
  success_url = '/birthdays'

class GiftList(ListView):
   model=GiftIdeas  

class GiftDetail(DeleteView):
   model=GiftIdeas

class GiftCreate(CreateView):
   model= GiftIdeas
   fields = '__all__'

class GiftUpdate(UpdateView):
   model=GiftIdeas
   fields= '__all__'

class GiftDelete(DeleteView):
   model = GiftIdeas
   success_url = '/gifts'
               

# Create your views here.
