from django.shortcuts import render, redirect, get_object_or_404
# from userapp.models import PlantList
from .forms import *


def userhomepage(request):
    return render(request,'userapp/userhomepage.html')

from .forms import *
from .models import Task

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('userapp:add_task')

    else:
        form = TaskForm()
    tasks = Task.objects.all()
    return render(request,'userapp/add_task.html',{'form': form,'tasks':tasks})

def delete_task(request,pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('userapp:add_task')

def gardeningtips(request):
    return render(request,'userapp/gardeningtips.html')

def contactsupport(request):
    return render(request,'userapp/contactsupport.html')

def gardeningplanning(request):
    return render(request,'userapp/gardeningplanning.html')