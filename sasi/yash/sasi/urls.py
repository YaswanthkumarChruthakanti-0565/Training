from django.urls import path
from . import views

urlpatterns = [
    path('me/', views.sasi, name='home'),

]

# Create your models here.
