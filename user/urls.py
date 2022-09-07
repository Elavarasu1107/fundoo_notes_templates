from django.urls import path
from . import views

urlpatterns = [
    path('', views.UserLogin.as_view(), name='login'),
    path('register/', views.UserRegistration.as_view(), name='register'),
    path('profile/', views.UserProfile.as_view(), name='profile'),
    path('logout/', views.UserLogout.as_view(), name='logout')
]
