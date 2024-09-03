from django.urls import path
from . import views

urlpatterns = [
    path('login', views.user_login, name='login'),
    path('register', views.user_register, name='register'),
    path('logout', views.user_logout, name='logout'),
    path('', views.index, name='home'),
    path('user-profile', views.user_profile, name='user-profile'),
    path('user-update', views.user_update, name='user-update'),
]