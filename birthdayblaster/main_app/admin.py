from django.contrib import admin

from .models import Birthday, GiftIdea, Photo

# Register your models here.

admin.site.register(Birthday)
admin.site.register(GiftIdea)
admin.site.register(Photo)
