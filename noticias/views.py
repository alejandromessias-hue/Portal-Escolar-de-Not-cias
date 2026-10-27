from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models.deletion import ProtectedError
from .models import Categoria, Tag
from .forms import CategoriaForm, TagForm

# --- GERENCIAMENTO DE CATEGORIAS ---

def listar_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'noticias/listar_categorias.html', {'categorias': categorias})

def criar_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Categoria cadastrada com sucesso!")
            return redirect('listar_categorias')
    else:
        form = CategoriaForm()
    return render(request, 'noticias/form_categoria.html', {'form': form, 'titulo': 'Cadastrar Categoria'})

def editar_categoria(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            messages.success(request, "Categoria atualizada com sucesso!")
            return redirect('listar_categorias')
    else:
        form = CategoriaForm(instance=categoria)
    return render(request, 'noticias/form_categoria.html', {'form': form, 'titulo': 'Editar Categoria'})

def excluir_categoria(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    if request.method == 'POST':
        try:
            categoria.delete()
            messages.success(request, "Categoria excluída com sucesso!")
            return redirect('listar_categorias')
        except ProtectedError:
            messages.error(
                request, 
                "Não é possível excluir esta categoria, pois existem notícias vinculadas a ela."
            )
            return redirect('listar_categorias')
            
    return render(request, 'noticias/confirmar_exclusao_categoria.html', {'categoria': categoria})


# --- GERENCIAMENTO DE TAGS ---

def listar_tags(request):
    tags = Tag.objects.all()
    return render(request, 'noticias/listar_tags.html', {'tags': tags})

def criar_tag(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Tag cadastrada com sucesso!")
            return redirect('listar_tags')
    else:
        form = TagForm()
    return render(request, 'noticias/form_tag.html', {'form': form, 'titulo': 'Cadastrar Tag'})

def editar_tag(request, pk):
    tag = get_object_or_404(Tag, pk=pk)
    if request.method == 'POST':
        form = TagForm(request.POST, instance=tag)
        if form.is_valid():
            form.save()
            messages.success(request, "Tag atualizada com sucesso!")
            return redirect('listar_tags')
    else:
        form = TagForm(instance=tag)
    return render(request, 'noticias/form_tag.html', {'form': form, 'titulo': 'Editar Tag'})

def excluir_tag(request, pk):
    tag = get_object_or_404(Tag, pk=pk)
    if request.method == 'POST':
        tag.delete()
        messages.success(request, "Tag excluída com sucesso!")
        return redirect('listar_tags')
        
    return render(request, 'noticias/confirmar_exclusao_tag.html', {'tag': tag})