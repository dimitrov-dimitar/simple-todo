from django.urls import path

from base import views

urlpatterns = [
    path('', views.todos, name='todos'),
    path('<int:pk>/', views.todo, name='todo'),
]
