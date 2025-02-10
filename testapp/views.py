from django.shortcuts import render, get_object_or_404, redirect
from .models import Task
from .forms import TaskForm

# View to list all tasks
def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'testapp/task_list.html', {'tasks': tasks})

# View to create a new task
def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'testapp/task_form.html', {'form': form})

# View to edit an existing task
def task_edit(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'testapp/task_form.html', {'form': form})

# View to delete a task
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('task_list')
