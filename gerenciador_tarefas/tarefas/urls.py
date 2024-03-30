from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Crie um roteador
router = DefaultRouter()

# Registre os viewsets com o roteador
router.register(r'tarefa', views.TarefaViewSet, basename='tarefas')
router.register(r'status', views.StatusViewSet, basename='status')

urlpatterns = [
    # Inclua as URLs do roteador
    path('', include(router.urls)),
    # Adicione outras URL patterns se necessário
]
