from django.urls import path
from . import views

from .views import (
    index,
    publication_list,
    create,
    edit_publication,
    delete_publication,

    
    
)

from Author.views import (
    login_view,
    register_view,
    
    
)

urlpatterns = [
    path('', index, name='index'),
    path('publication_list/', publication_list, name='publication_list'),
    path('create/', create, name='create'),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('publications/<pk>/edit/', edit_publication, name='edit_publication'),
    path('publications/<pk>/delete/', delete_publication, name='delete_publication'),
    
]
