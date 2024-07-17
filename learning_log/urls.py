
from django.contrib import admin
from django.urls import path
from django.conf.urls import include


urlpatterns = [

    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('', include('learning_logs.urls')),
]
