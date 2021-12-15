from django.db import models

# Create your models here.

class Pessoa(models.Model):
    nome = models.CharField(max_length=150)
    idade = models.CharField(max_length=3)
