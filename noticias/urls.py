from django.urls import path
from . import views

urlpatterns = [
    # Categorias
    path('', views.listar_categorias, name='listar_categorias'),
    path('categorias/nova/', views.criar_categoria, name='criar_categoria'),
    path('categorias/<int:pk>/editar/', views.editar_categoria, name='editar_categoria'),
    path('categorias/<int:pk>/excluir/', views.excluir_categoria, name='excluir_categoria'),

    # Tags
    path('tags/', views.listar_tags, name='listar_tags'),
    path('tags/nova/', views.criar_tag, name='criar_tag'),
    path('tags/<int:pk>/editar/', views.editar_tag, name='editar_tag'),
    path('tags/<int:pk>/excluir/', views.excluir_tag, name='excluir_tag'),
]