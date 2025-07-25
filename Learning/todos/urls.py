from django.urls import path
from . import views


urlpatterns = [
    path('', views.todo_list, name='todo_list'),
    path('add/', views.add_todo, name='add_todo'),
    path('complete/<int:todo_id>/', views.complete_todo, name='complete_todo'),
]


