from rest_framework.serializers import ModelSerializer
from endereco.models import Endereco

class EnderecoSerializer(ModelSerializer):
    class Meta:
        model = Endereco
        fields = ('id', 'cidade', 'estado') #Não inserir muitos campos pois o serializer vai ficar muito pesado e fica lento de abrir no celular ou outro dispositivo.
