from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()


router.register(r'tarefa', views.TarefaViewSet, basename='tarefas')
router.register(r'status', views.StatusViewSet, basename='status')


urlpatterns = [
    path('', include(router.urls)),
    
]
