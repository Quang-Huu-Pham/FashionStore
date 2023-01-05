from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name="core/login.html"), name="login"),
    path('logout/', auth_views.LogoutView.as_view(next_page='/login'), name='logout'),
    path('myprofile/', views.myprofile, name='myprofile'),
    path('myprofile/edit_myprofile', views.edit_myprofile, name='edit_myprofile'),
]
