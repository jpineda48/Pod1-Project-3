from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView 
from django.views.generic import ListView, DetailView

from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from.models import Birthday, GiftIdea

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
  giftideas = GiftIdea.objects.all()

  return render(request, 'birthdays/detail.html', { 'birthday': birthday, 'giftideas': giftideas })


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
  fields = '__all__'

class BirthdayDelete(LoginRequiredMixin, DeleteView):
  model = Birthday
  success_url = '/birthdays'

class GiftList(LoginRequiredMixin, ListView):
   model=GiftIdea

class GiftDetail(LoginRequiredMixin, DeleteView):
   model=GiftIdea

class GiftCreate(LoginRequiredMixin, CreateView):
   model= GiftIdea
   fields = '__all__'

class GiftUpdate(LoginRequiredMixin, UpdateView):
   model=GiftIdea
   fields= '__all__'

class GiftDelete(LoginRequiredMixin, DeleteView):
   model = GiftIdea
   success_url = '/gifts'
               

# Create your views here.
