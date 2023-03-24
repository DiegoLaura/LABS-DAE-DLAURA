from django.urls import path
from . import views

urlpatterns = [
    path('sumar/<int:num1>/<int:num2>/', views.suma),
    path('restar/<int:num1>/<int:num2>/', views.resta),
    path('multiplicar/<int:num1>/<int:num2>/', views.multiplicacion),
]
