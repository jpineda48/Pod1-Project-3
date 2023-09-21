from django.forms import ModelForm
from .models import GiftIdea

class GiftIdeaForm(ModelForm):
  class Meta:
    model = GiftIdea
    fields = ['ideas']