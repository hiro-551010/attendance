from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from . import views
from django.contrib.auth.views import LogoutView

app_name = 'accounts'

urlpatterns = [  
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('mypage/', views.mypage, name='mypage'),
]