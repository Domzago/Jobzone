from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db.models import Q

from .models import Job
from .forms import CreateForm, SignupForm, LoginForm

def home(request):
    
    p = Paginator(Job.objects.all(), 8)
    page = request.GET.get('page')
    jobs = p.get_page(page)

    search = request.GET.get('search')

    if search:
        jobs = Job.objects.filter(Q(name__icontains=search) | Q(description__icontains=search))

    return render(request, 'home.html', {'jobs':jobs, 'search':search})

def detail(request, pk):
    job = get_object_or_404(Job, pk=pk)
    return render(request, 'detail.html', {'job': job})

def create(request):
    form = CreateForm()

    if request.method == 'POST':
        form = CreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your Job Was Created Successfully')
            return redirect('home')
    else:
        form = CreateForm()
    return render(request, 'create.html', {'form':form})

def update(request, pk):
    job = get_object_or_404(Job, pk=pk)
    form = CreateForm()

    if request.method == 'POST':
        form = CreateForm(request.POST, request.FILES, instance=job)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your Job Was Updated Successfully')
            return redirect('detail', pk=pk)
    else:
        form = CreateForm(instance=job)
    return render(request, 'create.html', {'job':job,'form':form})


def delete(request, pk):
    job = get_object_or_404(Job, pk=pk)
    if request.method == 'POST':
        job.delete()
        messages.success(request, 'The job was deleted')
        return redirect('home')
    return render(request, 'delete.html', {'job': job})


def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        
        if form.is_valid(): 
            form.save()
            
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)       
            messages.success(request, f'Welcome {username} your account was created successfully')
            return redirect('home')
        else:
            return redirect('signup')


def loginuser(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    
    if request.method == 'POST':    
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f'Hello {username} Welcome Back')
            return redirect('home')
        else:
            return redirect('login')

def apply(request):
    if request.method == 'POST':
        get_item = request.POST.get('get-item')
        
        if get_item:
            get_item_object = Job.objects.get(name=get_item)
            get_item_object.created = request.user
            get_item_object.save()
            messages.success(request, f'Congratulations {request.user.username} you have applied for {get_item} expect Goodnews')
        return redirect('home')

    else:
        return render(request, 'apply.html', {})


