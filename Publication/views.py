from django.shortcuts import render, redirect
from .models import Publication
from .forms import PublicationForm, LoginForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm

def index(request):
    return render(request, 'index.html')

def publication_list(request):
    publications = Publication.objects.all()  # Recupera todos os objetos Publication
    return render(request, 'publication_list.html', {'publications': publications}) 

def create(request):
    if request.method == 'POST':
        form = PublicationForm(request.POST, request=request)
        if form.is_valid():
            form.save()
            return redirect('publication_list.html')  # Redireciona para a lista de publicações após criar uma nova publicação
    else:
        form = PublicationForm(request=request)
    return render(request, 'create.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('create')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})