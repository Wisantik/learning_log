from django.urls import path, include
from django.contrib.auth import views as auth_views

app_name = 'users'
urlpatterns = [
    #включить url  авторизации по умолчанию
    path('', include('django.contrib.auth.urls')),
    path('/logout/', auth_views.LogoutView.as_view(), name='logout'),
]
