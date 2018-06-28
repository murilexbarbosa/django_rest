from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from core.models import PontoTuristico
from .serializers import PontoTuristicoSerializer
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter


class PontoTuristicoViewSet(ModelViewSet):
    serializer_class = PontoTuristicoSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('nome', 'descricao', '=endereco__linha1')
    lookup_field = ('nome')

    def get_queryset(self):
        id = self.request.query_params.get('id', None)
        nome = self.request.query_params.get('nome', None)
        descricao = self.request.query_params.get('descricao', None)

        queryset = PontoTuristico.objects.all()
        if id:
            queryset = queryset.filter(id=id)
        if nome:
            queryset = queryset.filter(nome__iexact=nome)
        if descricao:
            queryset = queryset.filter(nome__iexact=descricao)
        return queryset

    def list(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).destroy(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).partial_update(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).retrieve(request, *args, **kwargs)

    @action(methods=['get','post'], detail=True)
    def teste(self, request, pk=None):
        pass
