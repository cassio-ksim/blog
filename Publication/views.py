from django.shortcuts import render
from .models import Publication
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView,CreateView, UpdateView, DeleteView

def index(request):
    return render(request, 'index.html')


class PublicationList(ListView):
    model = Publication
    template_name = 'publication_list.html'  # Especifique o nome do template
    context_object_name = 'publications'  # Nome do objeto no contexto do template


class PublicationDetail(DetailView):
    model = Publication
    template_name = 'publications/detail.html'


class PublicationCreate(CreateView):
    model = Publication
    form_class = Publication
    template_name = 'publications/create.html'
    success_url = '/publications/'  # URL para redirecionar após criar uma nova publicação


class PublicationUpdate(UpdateView):
    model = Publication
    form_class = Publication
    template_name = 'publications/update.html'
    success_url = '/publications/'  # URL para redirecionar após atualizar uma publicação


class PublicationDelete(DeleteView):
    model = Publication
    template_name = 'publications/delete.html'
    success_url = reverse_lazy('publication_list')  # URL para redirecionar após deletar uma publicação