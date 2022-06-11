from typing import Any

from django.db import models


class Produto(models.Model):
    nome = models.CharField('Nome', max_length=100)
    preco = models.DecimalField('Preço', decimal_places=2, max_digits=5)
    quantidade = models.IntegerField('Quantidade')

    def __str__(self) -> str:  # melhora a exibição no endpoint /admin
        return str(self.nome)
