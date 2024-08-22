from django.shortcuts import render, redirect
from .models import Publication
from .forms import PublicationForm

def index(request):
    return render(request, 'base.html')

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

