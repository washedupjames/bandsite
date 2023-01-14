from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('videos/', views.videos, name='videos'),
    path('gigs/', views.gigs, name='gigs'),
]
