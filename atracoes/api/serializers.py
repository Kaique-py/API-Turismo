from rest_framework.serializers import ModelSerializer
from atracoes.models import Atracao

class AtracaoSerializer(ModelSerializer):
    class Meta:
        model = Atracao
        fields = ('id', 'nome', 'descricao') #Não inserir muitos campos pois o serializer vai ficar muito pesado e fica lento de abrir no celular ou outro dispositivo.
