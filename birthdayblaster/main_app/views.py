from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView 
from django.views.generic import ListView, DetailView

from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from.models import Birthday, GiftIdeas

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
  return render(request, 'birthdays/detail.html', { 'birthday': birthday, 'BirthdayCreate' : BirthdayCreate })

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
  fields = '__all__'

  def form_valid(self, form):
    form.instance.user = self.request.user 
    return super().form_valid(form)

class BirthdayUpdate(LoginRequiredMixin, UpdateView):
  model = Birthday
  # Let's disallow the renaming of a cat by excluding the name field!
  fields = '__all__'

class BirthdayDelete(LoginRequiredMixin, DeleteView):
  model = Birthday
  success_url = '/birthdays'

class GiftList(LoginRequiredMixin, ListView):
   model=GiftIdeas  

class GiftDetail(LoginRequiredMixin, DeleteView):
   model=GiftIdeas

class GiftCreate(LoginRequiredMixin, CreateView):
   model= GiftIdeas
   fields = '__all__'

class GiftUpdate(LoginRequiredMixin, UpdateView):
   model=GiftIdeas
   fields= '__all__'

class GiftDelete(LoginRequiredMixin, DeleteView):
   model = GiftIdeas
   success_url = '/gifts'
               

# Create your views here.
