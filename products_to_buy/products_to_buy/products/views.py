from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from typing import Any
from products.models import Produto
from django.template import Context, loader


def index(request: Any) -> HttpResponse:
    context: dict[int or str] = {
        "curso": "python",
        "preco": 100.00,
        "quantidade": 10
    }
    return render(request,'index.html', context)


def contato(request: Any) -> HttpResponse:
    return render(request, 'contato.html')


def produto(request: Any, id: int) -> HttpResponse:
    # product = Produto.objects.get(id=id)
    product = get_object_or_404(Produto, id=id)  # obtem um produto ou retorna 404 (tipo do retorno, e o que vai buscar)
    context: dict[str, Produto] = {
        "produto": product,
    }
    return render(request, 'produto.html', context)


def produtos(request: Any) -> HttpResponse:
    product = Produto.objects.all()
    context: dict[str, Produto] = {
        "produtos": product,
    }
    return render(request, 'produtos.html', context)

def error404(request, exception): # desse modo, são renderizadas páginas de erro no django
    template = loader.get_template('notfound.html')
   
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf-8', status=404) 

def error500(request, exception): # desse modo, são renderizadas páginas de erro no django
    template = loader.get_template('notfound.html')
   
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf-8', status=500)   
"""
def error404(request, exception):
   context = {}
   return render(request,'notfound.html', context)
"""
