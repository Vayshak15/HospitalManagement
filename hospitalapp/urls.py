from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
    path('',views.index,name='home'),
    path('about/',views.about,name='about'),
    path('booking/',views.Booking,name='booking'),
    path('doctors/',views.Doctorspage,name='doctors'),
    path('contact/',views.Contact,name='contact'),
    path('department/',views.Department,name='department'),
]

