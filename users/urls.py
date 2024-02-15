from django.urls import path, include
from django.contrib.auth import views
from users import views

app_name = 'users'
urlpatterns = [
    # включить url  авторизации по умолчанию
    path('', include('django.contrib.auth.urls')),

    path('logout', views.logout_view, name='logout'),
    # страница регистрации
    path('register/', views.register, name='register')
]
