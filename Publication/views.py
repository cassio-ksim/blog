from django.shortcuts import render, redirect
from .models import Publication, Author
from .forms import PublicationForm

def index(request):
    return render(request, 'base.html')

def publication_list(request):
    publications = Publication.objects.all()  # Recupera todos os objetos Publication
    return render(request, 'publication_list.html', {'publications': publications}) 

def create(request):
    if request.method == 'POST':
        form = PublicationForm(request.POST)  # Passa o request.user como parâmetro
        if form.is_valid():
            author = request.user
            publication = form.save(commit=False)
            publication.user = author
            publication.save()
            return redirect('publication_list')
    else:
        form = PublicationForm(request.user)  # Passa o request.user como parâmetro
    return render(request, 'create.html', {'form': form})
