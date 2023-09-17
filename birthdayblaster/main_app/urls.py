from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('birthdays/', views.birthdays_index, name='index'),
    path('birthdays/<int:birthday_id>/', views.birthdays_detail, name='detail'),
    path('birthdays/create/', views.BirthdayCreate.as_view(), name='birthdays_create'),
    path('birthdays/<int:pk>/update/', views.BirthdayUpdate.as_view(), name='birthdays_update'),
    path('birthdays/<int:pk>/delete/', views.BirthdayDelete.as_view(), name='birthdays_delete'),
]