from django.urls import path
from . import views

app_name = 'boards'


urlpatterns = [
    path('create_theme', views.create_theme, name='create_theme'),
]