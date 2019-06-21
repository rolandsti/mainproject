from django.urls import path
from . import views

urlpatterns = [
    path('', views.numbers_main_view,),
  ]