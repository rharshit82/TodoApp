from . import views
from django.urls import path

urlpatterns = [
    path('', views.todo, name ='index'),
    path('addTodo/', views.addTodo, name ='addTodo'),
    path('deleteTodo/<int:Todo_id>', views.deleteTodo, name='deleteTodo')
    
]