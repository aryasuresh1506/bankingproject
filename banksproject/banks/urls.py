from django.urls import path
from . import views

app_name='banks'

urlpatterns = [
    path('',views.home,name='home'),
    path('login/', views.login, name='login'),
    path('register/',views.register,name='register'),
    path('forum/',views.forum,name='forum'),
    path('fill/',views.fill,name='fill'),
    path('accept/',views.accept,name='accept'),
]