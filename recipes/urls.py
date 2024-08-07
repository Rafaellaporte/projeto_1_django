from django.urls import path
from . import views

# path('recipes/', home),  # Exemplo de home

urlpatterns = [
    path('', views.home),
    path('recipes/<int:id>/', views.recipe),
]
