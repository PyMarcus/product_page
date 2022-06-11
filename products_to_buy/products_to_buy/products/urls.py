from django.urls import path
from products.views import index, contato, produto, produtos


urlpatterns = [
    path('', index, name='index'),
    path('contato', contato, name='contato'),
    path('produto/<int:id>', produto, name='produto'),
    path('produtos', produtos, name='produtos'),
]



