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
    #need several urls for ideas to work
    path('gifts/', views.GiftIdeaList.as_view(), name='gifts_index'),
    path('gifts/<int:pk>/', views.GiftIdeaDetail.as_view(), name='gifts_detail'),
    path('gifts/create/', views.GiftIdeaCreate.as_view(), name='gifts_create'),
    path('gifts/<int:pk>/update/', views.GiftIdeaUpdate.as_view(), name='gifts_update'),
    path('gifts/<int:pk>/delete/', views.GiftIdeaDelete.as_view(), name='gifts_delete')
    
]