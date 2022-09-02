from __future__ import unicode_literals

from django.db import models
from . import choices


class Estado(models.Model):
    uf =  models.CharField(max_length=2)
    estado = models.CharField(max_length=100)
    
    def __str__(self):
        return self.uf

class Comarca(models.Model):
    descricao = models.CharField(max_length=100)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.descricao

