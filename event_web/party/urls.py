from django.urls import path
from .views import *

urlpatterns = [
    path('', GetUser.as_view(), name='home_url'),
    path('new/<int:pk>/', PersonDetailView.as_view(), name='new_url'),
    path('all', UserAll.as_view(), name='all_url'),
]
