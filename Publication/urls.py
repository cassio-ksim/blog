from django.urls import path
from . import views

from .views import (
    index,
    Publication,
    
)

urlpatterns = [
    path('', index, name='index'),
    path('publications/', views.PublicationList(), name='publication_list'),
    path('publications/<int:pk>/', views.PublicationDetail(), name='publication_detail'),
    path('publications/create/', views.PublicationCreate(), name='publication_create'),
    path('publications/<int:pk>/update/', views.PublicationUpdate, name='publication_update'),
    path('publications/<int:pk>/delete/', views.PublicationDelete(), name='publication_delete'),
]
