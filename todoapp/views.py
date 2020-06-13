from django.shortcuts import render
from .models import Todo
from django.http import HttpResponseRedirect

def todo(request):
    data = Todo.objects.all()
    context= {
        'items' : data
    }
    return render(request,'index.html', context)

def addTodo(request):
    new_item = Todo (title= request.POST['title'], desc= request.POST['desc'])
    new_item.save()
    return HttpResponseRedirect('/')

def deleteTodo(request,Todo_id):
    todo_item=Todo.objects.get(id=Todo_id)
    todo_item.delete()
    return HttpResponseRedirect('/')

