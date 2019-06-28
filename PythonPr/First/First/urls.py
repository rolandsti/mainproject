"""First URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from tryout import views as thing
from tryout.views import stuff_create_view as numb


urlpatterns = [
    path('admin/', admin.site.urls),
    path('stuff', thing.index_view, name='index'),
    path('1a/', thing.about_view, name='about'),
    path('1b/', thing.home_view, name='home'),
    path('strings/', thing.string_view, name="view"),
    path('numbers/', numb, name="numbers"),
## down for main project stuff
    path('', thing.numbers_main_view, name="main"),
    path('create/', thing.numbers_create_view, name="create"),
    path('<int:entry_id>/delete/', thing.numbers_delete_view, name="delete"),
    path('<int:entry_id>/save/', thing.numbers_edit_view, name="save"),
    path('<int:entry_id>/', thing.numbers_entry_view, name="entry"),
]
