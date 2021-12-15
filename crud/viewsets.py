from rest_framework import viewsets
from . import models
from . import serializers

class PessoaViewSets(viewsets.ModelViewSet):
    queryset = models.Pessoa.objects.all()
    serializers_class = serializers.PessoaSerializers