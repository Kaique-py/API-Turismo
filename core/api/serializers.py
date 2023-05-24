from rest_framework.serializers import ModelSerializer
from core.models import PontoTuristico

class PontoTuristicoSerializer(ModelSerializer):
    class Meta:
        model = PontoTuristico
        fields = ('id', 'nome', 'descricao', 'aprovado', 'foto') #Não inserir muitos campos pois o serializer vai ficar muito pesado e fica lento de abrir no celular ou outro dispositivo.
