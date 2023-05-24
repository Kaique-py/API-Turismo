from rest_framework.viewsets import ModelViewSet
from atracoes.models import Atracao
from .serializers import AtracaoSerializer
from django_filters.rest_framework import DjangoFilterBackend

class AtracaoViewSet(ModelViewSet):
    queryset = Atracao.objects.all()
    serializer_class = AtracaoSerializer
    #filter_backends = [DjangoFilterBackend] #Isso aqui é desnecessário porque temos aquele campo REST_FRAMEWORK no arquivo settings da Pasta Principal do projeto.
    filterset_fields = ['nome', 'descricao']