from django.urls import path
from . import views

urlpatterns = [
    path('', views.submit_vault_letter, name='submit_vault_letter'),
]