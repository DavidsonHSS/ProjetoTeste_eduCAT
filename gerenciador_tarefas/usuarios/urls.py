from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()


router.register(r'usuario', views.UsuarioViewSet, basename='usuarios')


urlpatterns = [
    path('', include(router.urls)),
    
]
