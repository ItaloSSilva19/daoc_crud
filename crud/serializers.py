from rest_framework import serializers
from .models import Pessoa

class PessoaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Pessoa
        field = '__all__'

