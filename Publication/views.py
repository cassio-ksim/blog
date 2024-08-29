from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Publication
from .forms import PublicationForm


def index(request):
    publications = Publication.objects.all()
    return render(request, 'base.html', {'publications': publications})


def publication_list(request):
    posts = Publication.objects.all()  # Recupera todos os objetos Publication
    return render(request, 'publication_list.html', {'posts': posts}) 

def create(request):
    if request.method == 'POST':
        form = PublicationForm(request.POST)
        if form.is_valid():
            publication = form.save(commit=False)
            publication.user = request.user
            publication.save()
            return redirect('publication_list')
    else:
        form = PublicationForm()  # Crie uma instância do formulário sem parâmetros
    return render(request, 'create.html', {'form': form})

@login_required
def edit_publication(request, pk):
    publication = Publication.objects.get(pk=pk)
    if request.method == 'POST':
        publication.title = request.POST['title']
        publication.content = request.POST['content']
        publication.save()
        return redirect('publication_list')
    return render(request, 'edit_publication.html', {'publication': publication})

@login_required
def delete_publication(request, pk):
    publication = Publication.objects.get(pk=pk)
    if request.method == 'POST':
        publication.delete()
        return redirect('publication_list')
    return render(request, 'delete_publication.html', {'publication': publication})

    


