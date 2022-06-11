from django.contrib import admin
from products.models import Produto


class ProdutoAdmin(admin.ModelAdmin):  # registra em admin, o conteudo do app product
    list_display = 'nome', 'preco', 'quantidade'


admin.site.register(Produto, ProdutoAdmin)
