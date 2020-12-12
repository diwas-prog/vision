
from django.contrib import admin
from django.urls import path
from homepage import views

urlpatterns = [
    path('', views.home, name="home"),
    path('admin/', admin.site.urls),
    path('login/', views.login, name="login"),
   
]
