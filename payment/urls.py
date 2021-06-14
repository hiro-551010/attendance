from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from . import views

app_name = 'payment'

urlpatterns = [
    path('att/', views.IndexView.as_view(), name='att'),
    path('result/', views.ResultView.as_view(), name="result")
    # path('pay/', views.pay, name="pay"),
]