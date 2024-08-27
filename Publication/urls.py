from django.urls import path
from . import views

from .views import (
    index,
    publication_list,
    create,
    post_detail,
    
    
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
    path('post/<pk>/', post_detail, name='post_detail')
    
]
