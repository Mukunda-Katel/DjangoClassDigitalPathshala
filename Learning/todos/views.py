from django.shortcuts import render, redirect
from .models import  Todo

# Create your views here.
def todo_list(request):
    todos = Todo.objects.all()
    return render(request, 'todo_list.html', {'todo':todos})

def add_todo(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            Todo.objects.create(title=title)
        return redirect('todo_list')
    return render(request, 'add_todo.html')

def complete_todo(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.completed = True
    todo.save()
    return render('todo_list')
