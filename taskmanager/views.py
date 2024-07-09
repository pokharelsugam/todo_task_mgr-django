from django.shortcuts import render,redirect, HttpResponse
from .models import Task
from django.urls import reverse

# Create your views here.
def task_list(request):
    task_objs = Task.objects.all()
    return render(request,'index.html',{'tasks': task_objs})

def task_add(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        status = request.POST.get('status')
        Task.objects.create(
            name= name,
            description = description,
            status = status,
        )
        return redirect('task_list')
    return render(request, 'add-task.html')

def task_edit(request, pk):
    task_objs = Task.objects.get(id=pk)
    if request.method == "POST":
        name = request.POST.get('name')
        description = request.POST.get('description')
        status = request.POST.get('status')
        task_objs.name = name
        task_objs.description = description
        task_objs.status = status
        task_objs.save()
        return redirect('task_list')
    return render(request, 'edit-task.html', {'task':task_objs})

def task_delete(request, pk):
    task_objs = Task.objects.get(id=pk)
    task_objs.delete() 
    return HttpResponse(f'The task {task_objs.name} deleted <a href="{reverse('task_list')}">Go back to the task list</a>')
