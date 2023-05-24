from rest_framework.serializers import ModelSerializer
from avaliacoes.models import Avaliacao

class AvaliacoesSerializer(ModelSerializer):
    class Meta:
        model = Avaliacao
        fields = ('id', 'usuario', 'nota', 'data') #Não inserir muitos campos pois o serializer vai ficar muito pesado e fica lento de abrir no celular ou outro dispositivo.