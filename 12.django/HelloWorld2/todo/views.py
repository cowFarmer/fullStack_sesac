from django.shortcuts import render, redirect, get_object_or_404
from .models import Task


def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'todo/task_list.html', {'tasks': tasks})

def task_create(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        task = Task.objects.create(title=title, description=description)
        return redirect('task_detail', task.pk)
    return render(request, 'todo/task_create.html')

def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'todo/task_detail.html', {'task': task})

def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)
    # 수정 코드 추가
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        task.title = title
        task.description = description
        task.save()
        return redirect('task_detail', task.pk)
    return render(request, 'todo/task_update.html', {'task': task})

def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('task_list')

# def task_detail(request, pk):
#     if request.method == 'GET':
#         _task_read(request, pk)
#     elif request.method == 'PUT':
#         _task_update(request, pk)
#     elif request.method == 'DELETE':
#         _task_delete(request, pk)

# def _task_read(request, pk):
#     task = get_object_or_404(Task, pk=pk)
#     return render(request, 'todo/task_detail.html', {'task': task})

# def _task_update(request, pk):
#     task = get_object_or_404(Task, pk=pk)
#     # 수정 코드 추가
#     if request.method == 'POST':
#         title = request.POST['title']
#         description = request.POST['description']
#         task.title = title
#         task.description = description
#         task.save()
#         return redirect('task_detail', task.pk)
#     return render(request, 'todo/task_update.html', {'task': task})

# def _task_delete(request, pk):
#     task = get_object_or_404(Task, pk=pk)
#     task.delete()
#     return redirect('task_list')