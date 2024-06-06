from django.urls import path
from .views import ClientListCreate, ClientDetail, ProjectListCreate, ProjectDetail

urlpatterns = [
    path('clients/', ClientListCreate.as_view(), name='client-list-create'),
    path('clients/<int:pk>/', ClientDetail.as_view(), name='client-detail'),
    path('projects/', ProjectListCreate.as_view(), name='project-list-create'),
    path('projects/<int:pk>/', ProjectDetail.as_view(), name='project-detail'),
]
