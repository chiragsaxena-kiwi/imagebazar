from unicodedata import category
from django.urls import  path
from .import views

urlpatterns = [
    path('', views.home,name='home'),
    path('category/<int:cid>',views.category) 
]
