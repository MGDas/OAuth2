from django.urls import path
from .views import index_oauth

urlpatterns = [
    path('', index_oauth)
]
