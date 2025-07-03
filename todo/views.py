from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm


# Create your views here.


def task_list(request):
    active_tasks = Task.objects.filter(completed=False).order_by('-created')
    completed_tasks = Task.objects.filter(completed=True).order_by('-created')
    return render(request, 'todo/task_list.html',{
        'active_tasks':active_tasks,
        'completed_tasks':completed_tasks
    })


def add_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'todo/add_task.html', {'form':form})

def complete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.completed = not task.completed
    task.save()
    return redirect('task_list')


def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('task_list')