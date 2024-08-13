from django.urls import path
from . import views

from .views import (
    index,
    publication_list,
    create,
    
    
)

urlpatterns = [
    path('', index, name='index'),
    path('publication_list/', publication_list, name='publication_list'),
    path('create/', create, name='create'),
    
]
