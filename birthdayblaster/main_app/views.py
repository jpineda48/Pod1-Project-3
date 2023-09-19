from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView 
from django.views.generic import ListView, DetailView



from.models import Birthday, GiftIdea


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
  giftideas = GiftIdea.objects.all()

  return render(request, 'birthdays/detail.html', { 'birthday': birthday, 'giftideas': giftideas })

class BirthdayCreate(CreateView):
  model = Birthday
  fields = ['first_name', 'last_name','date', 'relationship', 'address', 'phone_number', 'email', 'delivery_method' ]

class BirthdayUpdate(UpdateView):
  model = Birthday
  # Let's disallow the renaming of a cat by excluding the name field!
  fields = '__all__'

class BirthdayDelete(DeleteView):
  model = Birthday
  success_url = '/birthdays'

#views for gifts

class GiftIdeaList(ListView):
   model=GiftIdea 
   template_name = 'gifts/index.html'

class GiftIdeaDetail(DetailView):
   model=GiftIdea
   template_name = 'gifts/detail.html'

class GiftIdeaCreate(CreateView):
   model= GiftIdea
   fields = '__all__'

class GiftIdeaUpdate(UpdateView):
   model=GiftIdea
   fields= '__all__'

class GiftIdeaDelete(DeleteView):
   model = GiftIdea
   success_url = '/gifts/'
               

# Create your views here.
