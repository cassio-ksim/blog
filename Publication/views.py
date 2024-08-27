from django.shortcuts import render, redirect, get_object_or_404
from .models import Publication
from .forms import PublicationForm, CommentForm


def index(request):
    return render(request, 'base.html')

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
    
def post_detail(request, pk):
    post = get_object_or_404(Publication, pk=pk)
    comments = post.comment_set.all()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=pk)
    else:
        form = CommentForm()
    return render(request, 'post_detail.html', {'post': post, 'comments': comments, 'form': form})