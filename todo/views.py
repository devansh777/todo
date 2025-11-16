from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import Task

def addTask(request):
    task = request.POST['task']
    Task.objects.create(task=task)
    return redirect('home')

def completeTask(request,pk):
    task = get_object_or_404(Task,pk=pk)
    task.is_completed = True
    task.save()
    return redirect('home')

def incomplatedTask(request,pk):
    task = get_object_or_404(Task,pk=pk)
    task.is_completed = False
    task.save()
    return redirect('home')

def deleteTask(request,pk):
    task= get_object_or_404(Task,pk=pk)
    task.delete()
    return redirect('home')

def editTask(request,pk):
    task = get_object_or_404(Task,pk=pk)
    context = {
        'task':task
    }
    return render(request,'edit_task.html',context)

def saveTask(request):
    id = request.POST['id']
    updatedTask = request.POST['task']
    task = get_object_or_404(Task,pk=id)
    task.task = updatedTask
    task.save()
    return redirect('home')