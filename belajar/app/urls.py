from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.User.register, name='post'),
    path('update/', views.User.getdata, name='update'),
    path('addbook/', views.User.addbook, name='post'),
    path('login/', views.User.login, name='post'),
]